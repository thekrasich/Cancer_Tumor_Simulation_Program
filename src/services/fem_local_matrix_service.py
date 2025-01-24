import numpy


class FiniteElementLocalMatrixService:
    def __init__(self) -> None:
        pass

    @staticmethod
    def compute_stiffness_matrix(
        triangle_vertices: numpy.ndarray,
        x_axis_elastic_coefficient: float,
        y_axis_elastic_coefficient: float,
        order_of_elements: int,
    ) -> numpy.ndarray:
        pass

    @staticmethod
    def compute_mass_matrix(
        triangle_vertices: numpy.ndarray,
        order_of_elements: int,
    ) -> numpy.ndarray:
        pass

    @staticmethod
    def compute_inertial_force_vector(
        mass_matrix: numpy.ndarray, load_vector: numpy.ndarray
    ) -> numpy.ndarray:
        pass
