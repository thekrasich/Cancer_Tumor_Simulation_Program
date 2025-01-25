import numpy

from services.fem_local_matrix_service import FiniteElementLocalMatrixService


class FEMService:
    @staticmethod
    def contribute_to_global_matrix(
        global_matrix: numpy.ndarray,
        stiffness_matrix: numpy.ndarray,
        triangle: numpy.ndarray,
    ) -> numpy.ndarray:
        for i in range(3):
            for j in range(3):
                global_matrix[triangle[i], triangle[j]] += stiffness_matrix[i, j]
        return global_matrix

    @staticmethod
    def contribute_to_rhs(
        internal_force_vector: numpy.ndarray,
        triangle: numpy.ndarray,
        rhs: numpy.ndarray,
        order_of_elements: int = 1,
    ) -> numpy.ndarray:
        for i in range(3 * order_of_elements):
            rhs[triangle[i]] += internal_force_vector[i]
        return rhs

    @staticmethod
    def assemble_system(
        vertices, triangles, triangle_vertices, boundary_points, math_model
    ):
        assembled_system = numpy.zeros((len(vertices), len(vertices)))
        rhs = numpy.zeros(len(vertices))

        for i in range(len(triangles)):
            ke = numpy.array(
                FiniteElementLocalMatrixService.compute_stiffness_matrix(
                    triangle_vertices[i],
                    a_11=math_model.diffusion_coefficient,
                    a_22=math_model.diffusion_coefficient,
                )
            )
            me = FiniteElementLocalMatrixService.compute_mass_matrix(
                triangle_vertices[i]
            )
            qe = FiniteElementLocalMatrixService.compute_inertial_force_vector(
                me, [0.1, 0.1, 0.1]
            )

            assembled_system = FEMService.contribute_to_global_matrix(
                assembled_system, ke, triangles[i]
            )
            rhs = FEMService.contribute_to_rhs(qe, triangles[i], rhs)

        ## TODO. Move it?
        for i in range(len(vertices)):
            if i in boundary_points or i in boundary_points:
                assembled_system[i, :] = 0
                assembled_system[i, i] = 1e7
                rhs[i] = 1e7
        return assembled_system, rhs

    @staticmethod
    def solve_system(
        assembled_global_matrix: numpy.ndarray, rhs_column: numpy.ndarray
    ) -> numpy.ndarray:
        numpy.linalg.solve(assembled_global_matrix, rhs_column)
