from matplotlib import pyplot as plt
import numpy as np
from simulation_solver.math_helper import (
    assemble_global_matrix,
    assemble_rhs,
    compute_ke,
    compute_qe,
)


def start_simulation(B):
    ## TODO. DO IT NORMAL
    triangles = B["triangles"]

    edges = set()
    for tri in triangles:
        edges.add(tuple(sorted((tri[0], tri[1]))))
        edges.add(tuple(sorted((tri[1], tri[2]))))
        edges.add(tuple(sorted((tri[0], tri[2]))))

    outer_boundary_edges = set(tuple(sorted(edge)) for edge in seg0)
    inner_boundary_edges = set(tuple(sorted(edge)) for edge in seg1)

    outer_boundary = edges & outer_boundary_edges
    inner_boundary = edges & inner_boundary_edges

    outer_boundary_points = set(pt for edge in outer_boundary for pt in edge)
    inner_boundary_points = set(pt for edge in inner_boundary for pt in edge)

    vertices = B["vertices"]
    triangles = B["triangles"]

    triangle_vertices = np.array([[vertices[j] for j in i] for i in triangles])

    assembled_system = np.zeros((len(vertices), len(vertices)))
    rhs = np.zeros(len(vertices))

    for i in range(len(triangles)):
        ke = np.array(compute_ke(triangle_vertices[i], a11=1, a22=1))
        qe = compute_qe(triangle_vertices[i], fe=[1, 1, 1])

        assembled_system = assemble_global_matrix(assembled_system, ke, triangles[i])
        rhs = assemble_rhs(qe, triangles[i], rhs)

    for i in range(len(vertices)):

        if i in outer_boundary_points or i in inner_boundary_points:
            assembled_system[i, i] = 1e21
            rhs[i] = 1e21

    solution = np.linalg.solve(assembled_system, rhs)

    X = B["vertices"][:, 0]
    Y = B["vertices"][:, 1]
    Z = solution
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")
    surf = ax.plot_trisurf(X, Y, Z, cmap="viridis", edgecolor="none")
    fig.colorbar(surf, shrink=0.5, aspect=5)
    ax.set_title("3D графік розв'язку u(x, y)")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("u(x, y)")
    plt.show()
