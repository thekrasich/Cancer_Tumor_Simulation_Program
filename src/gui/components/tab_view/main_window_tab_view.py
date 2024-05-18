import customtkinter as ctk


class MainWindowTabView(ctk.CTkTabview):
    def __init__(self: ctk.CTkTabview, parent) -> None:
        super().__init__(
            parent,
            parent.application_settings.current_width - 50,
            parent.application_settings.current_heigth - 50,
            20,
        )
        print(parent)
        self.pack()

        area_tab = self.add("Area")
        mesh_tab = self.add("Mesh")
        math_model_tab = self.add("Mathematical Model")
        start_panel_tab = self.add("Start Panel")
