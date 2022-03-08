from medperf.ui.interface import UI
from medperf.entities.cube import Cube
from medperf.comms.interface import Comms
from medperf.entities.benchmark import Benchmark
from medperf.utils import dict_pretty_print, pretty_error
from medperf.commands.compatibility_test import CompatibilityTestExecution


class AssociateCube:
    @classmethod
    def run(cls, cube_uid: str, benchmark_uid: int, comms: Comms, ui: UI):
        """Associates a cube with a given benchmark

        Args:
            cube_uid (str): UID of model MLCube
            benchmark_uid (int): UID of benchmark
            comms (Comms): Communication instance
            ui (UI): UI instance
        """
        cube = Cube.get(cube_uid, comms, ui)
        benchmark = Benchmark.get(benchmark_uid, comms)

        _, _, _, result = CompatibilityTestExecution.run(
            benchmark_uid, comms, ui, model=cube_uid
        )
        ui.print("These are the results generated by the compatibility test. ")
        ui.print("This will be sent along the association request.")
        ui.print("They will not be part of the benchmark.")
        dict_pretty_print(result.todict(), ui)

        approval = cube.request_association_approval(benchmark, ui)

        if approval:
            ui.print("Generating mlcube benchmark association")
            comms.associate_cube(cube_uid, benchmark_uid)
        else:
            pretty_error(
                "MLCube association operation cancelled", ui, add_instructions=False
            )

