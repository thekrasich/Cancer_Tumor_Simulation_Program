import customtkinter as ctk
from common.constants import (
    MAIN_WINDOW_TITLE,
    MAIN_WINDOW_INITIAL_HEIGHT,
    MAIN_WINDOW_INITIAL_WIDTH,
)
from gui.helpers.window_geometry_helper import center_window_to_display

ctk.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


class MainWindow(ctk.CTk):
    def __init__(self: ctk.CTk, parent, *args, **kwargs):
        super().__init__()

        self.title(MAIN_WINDOW_TITLE)
        self.geometry(
            center_window_to_display(
                self, MAIN_WINDOW_INITIAL_WIDTH, MAIN_WINDOW_INITIAL_HEIGHT
            )
        )
