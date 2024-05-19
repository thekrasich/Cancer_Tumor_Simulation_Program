import customtkinter as ctk
from common.constants import (
    MAIN_WINDOW_TAB_AREA_TITLE,
    MAIN_WINDOW_TAB_GENERIC_BUTTON_HEIGTH,
    MAIN_WINDOW_TAB_GENERIC_BUTTON_WIDTH,
    MAIN_WINDOW_TAB_MATH_MODEL_TITLE,
    MAIN_WINDOW_TAB_MESH_TITLE,
    MAIN_WINDOW_TAB_START_TITLE,
)
from gui.components.tab_view.generic_tab_button import (
    GenericTabButton,
    WarningGenericTabButton,
)


class MainWindowTabView(ctk.CTkTabview):
    def __init__(self: ctk.CTkTabview, parent) -> None:
        super().__init__(
            parent,
            parent.application_settings.current_width - 50,
            parent.application_settings.current_heigth - 50,
            20,
        )
        self.pack()

        def presets_button_click() -> None:
            print("test")
            pass

        def file_button_click() -> None:
            print("test")
            pass

        def formula_button_click() -> None:
            print("test")
            pass

        def manual_input_button_click() -> None:
            print("test")
            pass

        def configure_boundary_conditions_button_click() -> None:
            print("test")
            pass

        def clear_area_button_click() -> None:
            print("test")
            pass

        ### Tabs initialization.
        area_tab = self.add(MAIN_WINDOW_TAB_AREA_TITLE)
        mesh_tab = self.add(MAIN_WINDOW_TAB_MESH_TITLE)
        math_model_tab = self.add(MAIN_WINDOW_TAB_MATH_MODEL_TITLE)
        start_panel_tab = self.add(MAIN_WINDOW_TAB_START_TITLE)

        ### Area tab.
        general_area_label = ctk.CTkLabel(
            area_tab, width=MAIN_WINDOW_TAB_GENERIC_BUTTON_WIDTH, font=("Helvetica", 28)
        )
        general_area_label.configure(text="Generate the area")
        general_area_label.place(relx=0, rely=0)

        boundary_condition_label = ctk.CTkLabel(
            area_tab, width=MAIN_WINDOW_TAB_GENERIC_BUTTON_WIDTH, font=("Helvetica", 28)
        )
        boundary_condition_label.configure(text="Boundary Conditions")
        boundary_condition_label.place(relx=0, rely=0.57)

        presets_button = GenericTabButton(
            area_tab, "Choose from Presets", presets_button_click, 0, 0.05
        )
        file_button = GenericTabButton(
            area_tab, "Select file", file_button_click, 0, 0.15
        )
        formula_button = GenericTabButton(
            area_tab, "Write a formula", formula_button_click, 0, 0.25
        )
        manual_input_button = GenericTabButton(
            area_tab, "Manual points input", manual_input_button_click, 0, 0.35
        )
        boundary_condition_button = GenericTabButton(
            area_tab,
            "Configure boundary conditions",
            configure_boundary_conditions_button_click,
            0,
            0.62,
        )
        clear_area_button = WarningGenericTabButton(
            area_tab,
            "Clear area",
            clear_area_button_click,
            0,
            0.9,
        )

        ### Mesh tab.

        ### Mathematical model tab.

        ### Start panel tab.
