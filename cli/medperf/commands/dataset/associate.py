from medperf.ui import UI
from medperf.comms import Comms
from medperf.entities import Dataset, Benchmark
from medperf.utils import pretty_error, dict_pretty_print
from medperf.commands.benchmark.compatibility_test import CompatibilityTestExecution


class AssociateDataset:
    @staticmethod
    def run(data_uid: str, benchmark_uid: int, comms: Comms, ui: UI):
        """Associates a registered dataset with a benchmark

        Args:
            data_uid (int): UID of the registered dataset to associate
            benchmark_uid (int): UID of the benchmark to associate with
        """
        dset = Dataset(data_uid, ui)
        benchmark = Benchmark.get(benchmark_uid, comms)

        if dset.preparation_cube_uid != benchmark.data_preparation:
            pretty_error("The specified dataset wasn't prepared for this benchmark", ui)

        # Run compatibility test between benchmark and dataset
        _, _, _, result = CompatibilityTestExecution.run(
            benchmark_uid, comms, ui, data_uid=data_uid,
        )
        ui.print(
            "Results obtained from the compatibility test. These are shared in the association process, and will not be part of the benchmark."
        )
        dict_pretty_print(result.todict())
        approval = dset.request_association_approval(benchmark, ui)

        if approval:
            ui.print("Generating dataset benchmark association")
            comms.associate_dset(dset.uid, benchmark_uid)
        else:
            pretty_error(
                "Dataset association operation cancelled", ui, add_instructions=False
            )
