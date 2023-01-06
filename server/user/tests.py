from rest_framework.test import APIClient
from rest_framework import status

from medperf.tests import MedPerfTest


class UserTest(MedPerfTest):
    """Test module for users APIs"""

    def setUp(self):
        super(UserTest, self).setUp()

        username = "admin"
        password = "admin"
        self.client = APIClient()
        response = self.client.post(
            "/api/v1/auth-token/", {"username": username, "password": password}, format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.token = response.data["token"]
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token)

    def test_unauthenticated_user(self):
        client = APIClient()
        response = client.get("/api/v1/users/1/")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        response = client.delete("/api/v1/users/1/")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        response = client.put("/api/v1/users/1/")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        response = client.post("/api/v1/users/", {})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        response = client.get("/api/v1/users/")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_crud_user(self):
        testuser = {
            "username": "testdataowner",
            "email": "testdo@example.com",
            "password": "test",
            "first_name": "testdata",
            "last_name": "owner",
        }

        response = self.client.post("/api/v1/users/", testuser, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        uid = response.data["id"]
        response = self.client.get("/api/v1/users/{0}/".format(uid))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        for k, v in response.data.items():
            if k in testuser:
                self.assertEqual(testuser[k], v)

        response = self.client.get("/api/v1/users/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["results"]), 2)

        response = self.client.delete("/api/v1/users/{0}/".format(uid))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        response = self.client.get("/api/v1/users/{0}/".format(uid))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_duplicate_usernames(self):
        testuser = {
            "username": "testdataowner",
            "email": "testdo@example.com",
            "password": "test",
            "first_name": "testdata",
            "last_name": "owner",
        }

        response = self.client.post("/api/v1/users/", testuser, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        response = self.client.post("/api/v1/users/", testuser, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_duplicate_emails(self):
        testuser = {
            "username": "testdataowner",
            "email": "testdo@example.com",
            "password": "test",
            "first_name": "testdata",
            "last_name": "owner",
        }

        response = self.client.post("/api/v1/users/", testuser, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        testuser = {
            "username": "newdataowner",
            "email": "testdo@example.com",
            "password": "test",
            "first_name": "newtestdata",
            "last_name": "owner",
        }

        response = self.client.post("/api/v1/users/", testuser, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_invalid_user(self):
        invalid_uid = 9999
        response = self.client.get("/api/v1/users/{0}/".format(invalid_uid))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_optional_fields(self):
        pass
