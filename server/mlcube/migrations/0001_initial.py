# Generated by Django 3.2.10 on 2022-03-07 09:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MlCube',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True)),
                ('git_mlcube_url', models.CharField(max_length=256)),
                ('git_parameters_url', models.CharField(max_length=256)),
                ('tarball_url', models.CharField(blank=True, max_length=256)),
                ('tarball_hash', models.CharField(blank=True, max_length=100)),
                ('state', models.CharField(choices=[('DEVELOPMENT', 'DEVELOPMENT'), ('OPERATION', 'OPERATION')], default='DEVELOPMENT', max_length=100)),
                ('is_valid', models.BooleanField(default=True)),
                ('metadata', models.JSONField(blank=True, default=dict, null=True)),
                ('user_metadata', models.JSONField(blank=True, default=dict, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'MlCubes',
                'ordering': ['modified_at'],
            },
        ),
    ]
