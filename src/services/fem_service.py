import numpy


class FEMService:
    def __init__(self) -> None:
        pass

    @staticmethod
    def assemble_global_matrix():
        pass

    @staticmethod
    def assemble_rhs():
        pass

    @staticmethod
    def solve_system(
        assembled_global_matrix: numpy.ndarray, rhs_column: numpy.ndarray
    ) -> numpy.ndarray:
        numpy.linalg.solve(assembled_global_matrix, rhs_column)
