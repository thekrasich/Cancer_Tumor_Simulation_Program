class ReadinessFlags:
    def __init__(
        self,
        is_area_set: bool = False,
        is_mesh_generated: bool = False,
        is_model_set: bool = False,
    ) -> None:
        self.is_area_set = is_area_set
        self.is_mesh_generated = is_mesh_generated
        self.is_model_set = is_model_set
