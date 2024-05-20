import customtkinter as ctk

from common.constants import (
    MAIN_WINDOW_TAB_GENERIC_BUTTON_WIDTH,
    SETTINGS_WINDOW_INITIAL_HEIGHT,
    SETTINGS_WINDOW_INITIAL_WIDTH,
    SETTINGS_WINDOW_TITLE,
)
from gui.components.tab_view.generic_tab_button import GenericSettingsButton
from gui.helpers.window_geometry_helper import center_window_to_display


class SettingsWindow(ctk.CTkToplevel):
    def __init__(self: ctk.CTkToplevel, parent) -> None:
        super().__init__()

        def save_settings_button_click() -> None:
            pass

        def cancel_save_settings_button_click() -> None:
            pass

        self.title(SETTINGS_WINDOW_TITLE)
        self.geometry(
            center_window_to_display(
                self, SETTINGS_WINDOW_INITIAL_WIDTH, SETTINGS_WINDOW_INITIAL_HEIGHT
            )
        )
        self.resizable(False, False)
        self.attributes("-topmost", True)

        self.appearance_mode_label = ctk.CTkLabel(
            self,
            text="Appearance Mode",
            width=50,
            font=("Helvetica", 20),
        )
        self.appearance_mode_label.pack(anchor="nw", padx=10, pady=10)

        self.appearance_mode_combobox = ctk.CTkComboBox(
            self,
            width=MAIN_WINDOW_TAB_GENERIC_BUTTON_WIDTH,
            height=50,
            corner_radius=20,
            values=["system", "dark", "light"],
            state="readonly",
            font=("Helvetica", 16),
            dropdown_font=("Helvetica", 16),
        )
        self.appearance_mode_combobox.set("system")

        self.appearance_mode_combobox.pack(anchor="nw", padx=10, pady=10)

        self.color_theme_label = ctk.CTkLabel(
            self,
            text="Color Theme",
            width=50,
            font=("Helvetica", 20),
        )
        self.color_theme_label.pack(anchor="nw", padx=10, pady=10)

        self.color_theme_combobox = ctk.CTkComboBox(
            self,
            width=MAIN_WINDOW_TAB_GENERIC_BUTTON_WIDTH,
            height=50,
            corner_radius=20,
            values=["blue", "dark-blue", "green"],
            state="readonly",
            font=("Helvetica", 16),
            dropdown_font=("Helvetica", 16),
        )
        self.color_theme_combobox.set("blue")

        self.color_theme_combobox.pack(anchor="nw", padx=10, pady=10)

        self.language_label = ctk.CTkLabel(
            self,
            text="Language",
            width=50,
            font=("Helvetica", 20),
        )
        self.language_label.pack(anchor="nw", padx=10, pady=10)

        self.language_combobox = ctk.CTkComboBox(
            self,
            width=MAIN_WINDOW_TAB_GENERIC_BUTTON_WIDTH,
            height=50,
            corner_radius=20,
            values=["English", "Ukrainian"],
            state="readonly",
            font=("Helvetica", 16),
            dropdown_font=("Helvetica", 16),
        )
        self.language_combobox.set("English")

        self.language_combobox.pack(anchor="nw", padx=10, pady=10)

        self.start_simulation_button = GenericSettingsButton(
            self,
            "Cancel",
            save_settings_button_click,
            0.23,
            0.9,
        )
        self.start_simulation_button = GenericSettingsButton(
            self,
            "Save",
            cancel_save_settings_button_click,
            0.62,
            0.9,
        )
