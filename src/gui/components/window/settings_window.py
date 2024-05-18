import customtkinter as ctk

from common.constants import (
    SETTINGS_WINDOW_INITIAL_HEIGHT,
    SETTINGS_WINDOW_INITIAL_WIDTH,
    SETTINGS_WINDOW_TITLE,
)
from gui.helpers.window_geometry_helper import center_window_to_display


class SettingsWindow(ctk.CTkToplevel):
    def __init__(self: ctk.CTkToplevel, parent) -> None:
        super().__init__(parent)

        self.title(SETTINGS_WINDOW_TITLE)
        self.geometry(
            center_window_to_display(
                self, SETTINGS_WINDOW_INITIAL_WIDTH, SETTINGS_WINDOW_INITIAL_HEIGHT
            )
        )
        self.resizable(False, False)
        self.attributes("-topmost", True)
