from medperf.ui import UI
from medperf.comms import Comms
from medperf.utils import pretty_error
from medperf.commands.mlcube.associate import AssociateCube
from medperf.commands.dataset.associate import AssociateDataset


class AssociateBenchmark:
    @classmethod
    def run(
        cls, benchmark_uid: str, model_uid: str, data_uid: str, comms: Comms, ui: UI
    ):
        """Associates a dataset or model to the given benchmark

        Args:
            benchmark_uid (str): UID of benchmark to associate entities with
            model_uid (str): UID of model to associate with benchmark
            data_uid (str): UID of dataset to associate with benchmark
            comms (Comms): _description_
            ui (UI): _description_
        """
        if model_uid and data_uid:
            pretty_error(
                "Can only associate one entity at a time. Pass a model or a dataset only",
                ui,
            )
        if model_uid is not None:
            comms.associate_cube(model_uid, benchmark_uid)
            ui.print("Association request to MLCube created")

        if data_uid is not None:
            AssociateDataset.run(data_uid, benchmark_uid, comms, ui)

