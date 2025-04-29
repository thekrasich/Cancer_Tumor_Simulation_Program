import numpy


class MathService:
    @staticmethod
    def dot_product():
        pass

    @staticmethod
    def compute_area_of_triangle(triangle_vertices: numpy.ndarray) -> float:
        S = 0.5 * (
            (
                triangle_vertices[0, 0] * triangle_vertices[1, 1]
                + triangle_vertices[1, 0] * triangle_vertices[2, 1]
                + triangle_vertices[2, 0] * triangle_vertices[0, 1]
            )
            - (
                triangle_vertices[0, 1] * triangle_vertices[1, 0]
                + triangle_vertices[1, 1] * triangle_vertices[2, 0]
                + triangle_vertices[2, 1] * triangle_vertices[0, 0]
            )
        )
        return 2 * S
