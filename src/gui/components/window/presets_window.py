import customtkinter as ctk

from gui.helpers.window_geometry_helper import center_window_to_display


class PresetWindow(ctk.CTkToplevel):
    def __init__(self, parent) -> None:
        super().__init__()

        self.title("Presets")
        self.geometry(center_window_to_display(self, 500, 400))
        self.resizable(False, False)
        self.attributes("-topmost", True)
