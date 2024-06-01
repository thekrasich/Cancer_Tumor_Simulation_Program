from matplotlib import pyplot as plt
import numpy as np
from simulation_solver.math_helper import (
    assemble_global_matrix,
    assemble_rhs,
    compute_ke,
    compute_qe,
    compute_pressure,
)


def start_simulation(triangulation_results, segments, math_model):
    vertices = triangulation_results["vertices"]
    triangles = triangulation_results["triangles"]

    edges = set()
    for tri in triangles:
        edges.add(tuple(sorted((tri[0], tri[1]))))
        edges.add(tuple(sorted((tri[1], tri[2]))))
        edges.add(tuple(sorted((tri[0], tri[2]))))

    all_edges = set(map(tuple, map(sorted, segments)))

    boundary_points = {pt for edge in all_edges for pt in edge}

    triangle_vertices = np.array([[vertices[j] for j in i] for i in triangles])

    assembled_system = np.zeros((len(vertices), len(vertices)))
    rhs = np.zeros(len(vertices))

    for i in range(len(triangles)):
        ke = np.array(
            compute_ke(
                triangle_vertices[i],
                a_11=math_model.diffusion_coefficient,
                a_22=math_model.diffusion_coefficient,
            )
        )

        ## Question about math model
        qe = compute_qe(triangle_vertices[i], fe=[1, 1, 1])

        assembled_system = assemble_global_matrix(assembled_system, ke, triangles[i])
        rhs = assemble_rhs(qe, triangles[i], rhs)

    for i in range(len(vertices)):
        if i in boundary_points or i in boundary_points:
            # assembled_system[i, :] = 0
            assembled_system[i, i] = 1e21
            rhs[i] = 1e21

    solution = np.linalg.solve(assembled_system, rhs)

    X_concentration = triangulation_results["vertices"][:, 0]
    Y_concentration = triangulation_results["vertices"][:, 1]
    Z_concentration = solution

    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")
    surf = ax.plot_trisurf(
        X_concentration,
        Y_concentration,
        Z_concentration,
        cmap="viridis",
        edgecolor="none",
    )
    fig.colorbar(surf, shrink=0.5, aspect=5)
    ax.set_title("Concentration")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("u(x, y)")
    plt.show()

    ## pressure
    vertices = triangulation_results["vertices"]
    triangles = triangulation_results["triangles"]

    edges = set()
    for tri in triangles:
        edges.add(tuple(sorted((tri[0], tri[1]))))
        edges.add(tuple(sorted((tri[1], tri[2]))))
        edges.add(tuple(sorted((tri[0], tri[2]))))

    all_edges = set(map(tuple, map(sorted, segments)))

    boundary_points = {pt for edge in all_edges for pt in edge}

    triangle_vertices = np.array([[vertices[j] for j in i] for i in triangles])

    assembled_system = np.zeros((len(vertices), len(vertices)))
    rhs = np.zeros(len(vertices))

    for i in range(len(triangles)):
        ke = np.array(
            compute_ke(
                triangle_vertices[i],
                a_11=math_model.diffusion_coefficient,
                a_22=math_model.diffusion_coefficient,
            )
        )

        qe = compute_qe(triangle_vertices[i], fe=[1, 1, 1])

        assembled_system = assemble_global_matrix(assembled_system, ke, triangles[i])
        rhs = assemble_rhs(qe, triangles[i], rhs)

    for i in range(len(vertices)):
        if i in boundary_points:
            x = vertices[i, 0]
            k = Z_concentration[i]
            pressure_value = compute_pressure(1, 1, Z_concentration[i], 1, x)
            print(pressure_value)
            assembled_system[i, i] = 1e21
            rhs[i] = 1e21 * pressure_value

    return X_concentration, Y_concentration, Z_concentration
