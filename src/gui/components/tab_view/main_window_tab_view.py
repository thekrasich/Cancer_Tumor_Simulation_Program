import customtkinter as ctk
from common.constants import (
    AREA_TAB_BOUNDARY_CONDITION_BUTTON_TEXT,
    AREA_TAB_CLEAR_AREA_BUTTON_TEXT,
    AREA_TAB_FILE_BUTTON_TEXT,
    AREA_TAB_MAIN_TITLE,
    AREA_TAB_BOUNDARY_CONDITION_LABEL_TEXT,
    AREA_TAB_MANUAL_INPUT_BUTTON_TEXT,
    AREA_TAB_PRESETS_BUTTON_TEXT,
    AREA_TAB_WRITE_FORMULA_BUTTON_TEXT,
    MAIN_WINDOW_TAB_AREA_TITLE,
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

        def mesh_area_button_click() -> None:
            print("test")
            pass

        def start_simulation_button_click() -> None:
            print("test")
            pass

        def set_model_button_click() -> None:
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
        general_area_label.configure(text=AREA_TAB_MAIN_TITLE)
        general_area_label.place(relx=0, rely=0)

        boundary_condition_label = ctk.CTkLabel(
            area_tab, width=MAIN_WINDOW_TAB_GENERIC_BUTTON_WIDTH, font=("Helvetica", 28)
        )
        boundary_condition_label.configure(text=AREA_TAB_BOUNDARY_CONDITION_LABEL_TEXT)
        boundary_condition_label.place(relx=0, rely=0.57)

        presets_button = GenericTabButton(
            area_tab, AREA_TAB_PRESETS_BUTTON_TEXT, presets_button_click, 0, 0.05
        )
        file_button = GenericTabButton(
            area_tab, AREA_TAB_FILE_BUTTON_TEXT, file_button_click, 0, 0.15
        )
        formula_button = GenericTabButton(
            area_tab, AREA_TAB_WRITE_FORMULA_BUTTON_TEXT, formula_button_click, 0, 0.25
        )
        manual_input_button = GenericTabButton(
            area_tab,
            AREA_TAB_MANUAL_INPUT_BUTTON_TEXT,
            manual_input_button_click,
            0,
            0.35,
        )
        boundary_condition_button = GenericTabButton(
            area_tab,
            AREA_TAB_BOUNDARY_CONDITION_BUTTON_TEXT,
            configure_boundary_conditions_button_click,
            0,
            0.62,
        )
        clear_area_button = WarningGenericTabButton(
            area_tab,
            AREA_TAB_CLEAR_AREA_BUTTON_TEXT,
            clear_area_button_click,
            0,
            0.9,
        )

        ### Mesh tab.
        general_mesh_label = ctk.CTkLabel(
            mesh_tab, width=MAIN_WINDOW_TAB_GENERIC_BUTTON_WIDTH, font=("Helvetica", 28)
        )
        general_mesh_label.configure(text="Meshing options")
        general_mesh_label.place(relx=0, rely=0)

        mesh_type_label = ctk.CTkLabel(
            mesh_tab, width=MAIN_WINDOW_TAB_GENERIC_BUTTON_WIDTH, font=("Helvetica", 16)
        )
        mesh_type_label.configure(text="Mesh Type")
        mesh_type_label.place(relx=0, rely=0.05)

        mesh_type_combobox = ctk.CTkComboBox(
            mesh_tab,
            MAIN_WINDOW_TAB_GENERIC_BUTTON_WIDTH,
            height=50,
            corner_radius=20,
            values=["Triangular"],
            state="readonly",
            font=("Helvetica", 16),
            dropdown_font=("Helvetica", 16),
        )
        mesh_type_combobox.place(relx=0, rely=0.11)
        mesh_type_combobox.set("Triangular")

        nodes_order_label = ctk.CTkLabel(
            mesh_tab, width=MAIN_WINDOW_TAB_GENERIC_BUTTON_WIDTH, font=("Helvetica", 16)
        )
        nodes_order_label.configure(text="Nodes Order")
        nodes_order_label.place(relx=0, rely=0.19)

        nodes_order_combobox = ctk.CTkComboBox(
            mesh_tab,
            MAIN_WINDOW_TAB_GENERIC_BUTTON_WIDTH,
            height=50,
            corner_radius=20,
            values=["Linear"],
            state="readonly",
            font=("Helvetica", 16),
            dropdown_font=("Helvetica", 16),
        )
        nodes_order_combobox.place(relx=0, rely=0.25)
        nodes_order_combobox.set("Linear")

        ### TODO. Improve sliders
        minimum_angle_label = ctk.CTkLabel(
            mesh_tab, width=MAIN_WINDOW_TAB_GENERIC_BUTTON_WIDTH, font=("Helvetica", 16)
        )
        minimum_angle_label.configure(text="Minimum anlge ( 20 - 60 )")
        minimum_angle_label.place(relx=0, rely=0.34)

        minimum_angle_slider = ctk.CTkSlider(
            mesh_tab, from_=20, to=60, width=MAIN_WINDOW_TAB_GENERIC_BUTTON_WIDTH
        )
        minimum_angle_slider.place(relx=0, rely=0.39)

        maximum_area_label = ctk.CTkLabel(
            mesh_tab, width=MAIN_WINDOW_TAB_GENERIC_BUTTON_WIDTH, font=("Helvetica", 16)
        )
        maximum_area_label.configure(text="Maximum area of element ( 0 - 1 )")
        maximum_area_label.place(relx=0, rely=0.43)

        maximum_area_slider = ctk.CTkSlider(
            mesh_tab, from_=20, to=60, width=MAIN_WINDOW_TAB_GENERIC_BUTTON_WIDTH
        )
        maximum_area_slider.place(relx=0, rely=0.49)

        mesh_area_button = GenericTabButton(
            mesh_tab,
            "Generate mesh",
            mesh_area_button_click,
            0,
            0.9,
        )

        ### Mathematical model tab.
        general_math_model_label = ctk.CTkLabel(
            math_model_tab,
            width=MAIN_WINDOW_TAB_GENERIC_BUTTON_WIDTH,
            font=("Helvetica", 28),
        )
        general_math_model_label.configure(text="Mathematical model settings")
        general_math_model_label.place(relx=0, rely=0)

        diffusion_coefficient_label = ctk.CTkLabel(
            math_model_tab,
            width=MAIN_WINDOW_TAB_GENERIC_BUTTON_WIDTH,
            font=("Helvetica", 16),
        )
        diffusion_coefficient_label.configure(text="Diffusion Coefficient (D)")
        diffusion_coefficient_label.place(relx=0, rely=0.05)

        diffusion_coefficient_entry = ctk.CTkEntry(
            math_model_tab,
            width=MAIN_WINDOW_TAB_GENERIC_BUTTON_WIDTH,
            font=("Helvetica", 16),
            corner_radius=20,
            height=50,
        )
        diffusion_coefficient_entry.place(relx=0, rely=0.11)

        measure_adhesion_label = ctk.CTkLabel(
            math_model_tab,
            width=MAIN_WINDOW_TAB_GENERIC_BUTTON_WIDTH,
            font=("Helvetica", 16),
        )
        measure_adhesion_label.configure(text="Measure of adhesion (G)")
        measure_adhesion_label.place(relx=0, rely=0.19)

        measure_adhesion_entry = ctk.CTkEntry(
            math_model_tab,
            width=MAIN_WINDOW_TAB_GENERIC_BUTTON_WIDTH,
            font=("Helvetica", 16),
            corner_radius=20,
            height=50,
        )
        measure_adhesion_entry.place(relx=0, rely=0.25)

        measure_apoptosis_label = ctk.CTkLabel(
            math_model_tab,
            width=MAIN_WINDOW_TAB_GENERIC_BUTTON_WIDTH,
            font=("Helvetica", 16),
        )
        measure_apoptosis_label.configure(text="Measure of apoptosis (A)")
        measure_apoptosis_label.place(relx=0, rely=0.34)

        measure_apoptosis_entry = ctk.CTkEntry(
            math_model_tab,
            width=MAIN_WINDOW_TAB_GENERIC_BUTTON_WIDTH,
            font=("Helvetica", 16),
            corner_radius=20,
            height=50,
        )
        measure_apoptosis_entry.place(relx=0, rely=0.39)

        set_model_button = GenericTabButton(
            math_model_tab,
            "Set Model Values",
            set_model_button_click,
            0,
            0.9,
        )

        ### Start panel tab.
        general_start_label = ctk.CTkLabel(
            start_panel_tab,
            width=MAIN_WINDOW_TAB_GENERIC_BUTTON_WIDTH,
            font=("Helvetica", 28),
        )
        general_start_label.configure(text="Start Panel")
        general_start_label.place(relx=0, rely=0)

        is_area_set_label = ctk.CTkLabel(
            start_panel_tab,
            width=MAIN_WINDOW_TAB_GENERIC_BUTTON_WIDTH,
            font=("Helvetica", 16),
        )
        is_area_set_label.configure(text="Area Set: ")
        is_area_set_label.place(relx=0, rely=0.05)

        is_mesh_generated_label = ctk.CTkLabel(
            start_panel_tab,
            width=MAIN_WINDOW_TAB_GENERIC_BUTTON_WIDTH,
            font=("Helvetica", 16),
        )
        is_mesh_generated_label.configure(text="Mesh Generated: ")
        is_mesh_generated_label.place(relx=0, rely=0.11)

        is_model_set_label = ctk.CTkLabel(
            start_panel_tab,
            width=MAIN_WINDOW_TAB_GENERIC_BUTTON_WIDTH,
            font=("Helvetica", 16),
        )
        is_model_set_label.configure(text="Model Set: ")
        is_model_set_label.place(relx=0, rely=0.19)

        start_simulation_button = GenericTabButton(
            start_panel_tab,
            "Start",
            start_simulation_button_click,
            0,
            0.9,
        )
