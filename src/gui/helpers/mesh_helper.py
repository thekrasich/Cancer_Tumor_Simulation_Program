import triangle as tr


def create_triangulation_options_string(
    mesh_type, nodes_order, minimum_angle=20, maximum_area=1
) -> str:
    ## MESHTYPE AND ORDER CURRENTLY IS UNSUPPORTED
    ## TODO. Add support of a0.0000+
    return "pq" + str(minimum_angle) + "a0." + str(maximum_area)


def triangulate_given_area(points, segments, triangulation_options):
    print(triangulation_options)
    area = dict(vertices=points, segments=segments)
    triangulation_results = tr.triangulate(area, triangulation_options)

    return triangulation_results
