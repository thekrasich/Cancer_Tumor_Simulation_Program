import customtkinter as ctk

from common.constants import MAIN_WINDOW_TAB_GENERIC_BUTTON_WIDTH
from gui.components.tab_view.generic_tab_button import GenericSettingsButton
from gui.helpers.window_geometry_helper import center_window_to_display


class PresetWindow(ctk.CTkToplevel):
    def __init__(self, parent) -> None:
        super().__init__()

        def generate_area_button_click() -> None:
            pass

        self.title("Presets")
        self.geometry(center_window_to_display(self, 500, 400))
        self.resizable(False, False)
        self.attributes("-topmost", True)

        self.area_types = ctk.CTkLabel(
            self,
            text="Shape: ",
            width=50,
            font=("Helvetica", 20),
        )
        self.area_types.pack(anchor="nw", padx=10, pady=10)

        self.presets_combobox = ctk.CTkComboBox(
            self,
            width=MAIN_WINDOW_TAB_GENERIC_BUTTON_WIDTH,
            height=50,
            corner_radius=20,
            values=[],
            state="readonly",
            font=("Helvetica", 16),
            dropdown_font=("Helvetica", 16),
        )
        self.presets_combobox.set("TEST")

        self.presets_combobox.pack(anchor="nw", padx=10, pady=10)

        self.number_of_points_label = ctk.CTkLabel(
            self,
            text="Initial number of points on boundary: ",
            width=50,
            font=("Helvetica", 20),
        )
        self.number_of_points_label.pack(anchor="nw", padx=10, pady=10)

        self.presets_number_of_points = ctk.CTkEntry(
            self,
            width=MAIN_WINDOW_TAB_GENERIC_BUTTON_WIDTH,
            height=50,
            corner_radius=20,
        )
        self.presets_number_of_points.pack(anchor="nw", padx=10, pady=10)

        self.generate_area = GenericSettingsButton(
            self,
            "Create area",
            generate_area_button_click,
            0.5,
            0.8,
        )
