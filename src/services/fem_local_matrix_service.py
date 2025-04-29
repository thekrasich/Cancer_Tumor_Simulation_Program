import numpy

from services.math_service import MathService


class FiniteElementLocalMatrixService:
    @staticmethod
    def compute_stiffness_matrix(
        triangle_vertices: numpy.ndarray,
        x_axis_elastic_coefficient: float,
        y_axis_elastic_coefficient: float,
        order_of_elements: int = 1,
    ) -> numpy.ndarray:

        if order_of_elements == 1:
            i = 0
            j = 1
            m = 2
            x1 = 0
            x2 = 1
            ke = [
                [
                    x_axis_elastic_coefficient
                    * (triangle_vertices[j, x2] - triangle_vertices[m, x2]) ** 2
                    + y_axis_elastic_coefficient
                    * (triangle_vertices[m, x1] - triangle_vertices[j, x1]) ** 2,
                    x_axis_elastic_coefficient
                    * (triangle_vertices[j, x2] - triangle_vertices[m, x2])
                    * (triangle_vertices[m, x2] - triangle_vertices[i, x2])
                    + y_axis_elastic_coefficient
                    * (triangle_vertices[m, x1] - triangle_vertices[j, x1])
                    * (triangle_vertices[i, x1] - triangle_vertices[m, x1]),
                    x_axis_elastic_coefficient
                    * (triangle_vertices[j, x2] - triangle_vertices[m, x2])
                    * (triangle_vertices[i, x2] - triangle_vertices[j, x2])
                    + y_axis_elastic_coefficient
                    * (triangle_vertices[m, x1] - triangle_vertices[j, x1])
                    * (triangle_vertices[j, x1] - triangle_vertices[i, x1]),
                ],
                [
                    x_axis_elastic_coefficient
                    * (triangle_vertices[j, x2] - triangle_vertices[m, x2])
                    * (triangle_vertices[m, x2] - triangle_vertices[i, x2])
                    + y_axis_elastic_coefficient
                    * (triangle_vertices[m, x1] - triangle_vertices[j, x1])
                    * (triangle_vertices[i, x1] - triangle_vertices[m, x1]),
                    x_axis_elastic_coefficient
                    * (triangle_vertices[m, x2] - triangle_vertices[i, x2]) ** 2
                    + y_axis_elastic_coefficient
                    * (triangle_vertices[i, x1] - triangle_vertices[m, x1]) ** 2,
                    x_axis_elastic_coefficient
                    * (triangle_vertices[m, x2] - triangle_vertices[i, x2])
                    * (triangle_vertices[i, x2] - triangle_vertices[j, x2])
                    + y_axis_elastic_coefficient
                    * (triangle_vertices[i, x1] - triangle_vertices[m, x1])
                    * (triangle_vertices[j, x1] - triangle_vertices[i, x1]),
                ],
                [
                    x_axis_elastic_coefficient
                    * (triangle_vertices[j, x2] - triangle_vertices[m, x2])
                    * (triangle_vertices[i, x2] - triangle_vertices[j, x2])
                    + y_axis_elastic_coefficient
                    * (triangle_vertices[m, x1] - triangle_vertices[j, x1])
                    * (triangle_vertices[j, x1] - triangle_vertices[i, x1]),
                    x_axis_elastic_coefficient
                    * (triangle_vertices[m, x2] - triangle_vertices[i, x2])
                    * (triangle_vertices[i, x2] - triangle_vertices[j, x2])
                    + y_axis_elastic_coefficient
                    * (triangle_vertices[i, x1] - triangle_vertices[m, x1])
                    * (triangle_vertices[j, x1] - triangle_vertices[i, x1]),
                    x_axis_elastic_coefficient
                    * (triangle_vertices[i, x2] - triangle_vertices[j, x2]) ** 2
                    + y_axis_elastic_coefficient
                    * (triangle_vertices[j, x1] - triangle_vertices[i, x1]) ** 2,
                ],
            ]
            area = MathService.compute_area_of_triangle(triangle_vertices)
            ke = numpy.array(ke)
            return (1 / (2 * area)) * ke

        elif order_of_elements == 2:
            pass

    @staticmethod
    def compute_mass_matrix(
        triangle_vertices,
        order_of_elements: int = 1,
    ) -> numpy.ndarray:
        if order_of_elements == 1:
            mass_matrix = numpy.array([[2, 1, 1], [1, 2, 1], [1, 1, 2]])
            return (
                MathService.compute_area_of_triangle(triangle_vertices) / 24
            ) * mass_matrix

        elif order_of_elements == 2:
            area = MathService.compute_area_of_triangle(triangle_vertices)
            factor = area / 60.0
            mass_matrix = numpy.array(
                [
                    [4, 2, 1, 2, 1, 2],
                    [2, 4, 2, 1, 2, 1],
                    [1, 2, 4, 2, 1, 2],
                    [2, 1, 2, 4, 2, 1],
                    [1, 2, 1, 2, 4, 2],
                    [2, 1, 2, 1, 2, 4],
                ]
            )

            return factor * mass_matrix

    @staticmethod
    def compute_inertial_force_vector(
        mass_matrix: numpy.ndarray, load_vector: numpy.ndarray
    ) -> numpy.ndarray:
        return numpy.dot(mass_matrix, numpy.transpose(numpy.array(load_vector)))
