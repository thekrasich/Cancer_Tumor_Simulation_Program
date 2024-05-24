from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from common.constants import (
    PLOTTER_HEIGTH_INCHES,
    PLOTTER_WIDTH_INCHES,
    PLOTTER_X_PLACEMENT,
    PLOTTER_Y_PLACEMENT,
)


class AreaPlotArea(FigureCanvasTkAgg):
    def __init__(self, parent) -> None:
        fig, ax = plt.subplots()
        fig.set_size_inches(PLOTTER_WIDTH_INCHES, PLOTTER_HEIGTH_INCHES)
        ax.axis("on")
        ax.set_aspect("equal", adjustable="datalim")
        plt.grid(True)

        super().__init__(fig, master=parent)
        self.ax = ax
        self.fig = fig

        self.get_tk_widget().place(relx=PLOTTER_X_PLACEMENT, rely=PLOTTER_Y_PLACEMENT)
        self.draw()

    def update_window(self, parent, points):
        fig, ax = plt.subplots()
        fig.set_size_inches(PLOTTER_WIDTH_INCHES, PLOTTER_HEIGTH_INCHES)

        x = points[:, 0]
        y = points[:, 1]
        ax.scatter(x, y)

        ax.axis("on")
        plt.grid(True)

        self.ax.relim()
        self.ax.autoscale_view()

        fig.subplots_adjust(left=0, right=1, bottom=0, top=1, wspace=0, hspace=0)

        canvas = FigureCanvasTkAgg(fig, master=parent)
        canvas.draw()
        canvas.get_tk_widget().place(relx=PLOTTER_X_PLACEMENT, rely=PLOTTER_Y_PLACEMENT)

        parent.update()

    def clear_area(self, parent):
        fig, ax = plt.subplots()
        fig.set_size_inches(PLOTTER_WIDTH_INCHES, PLOTTER_HEIGTH_INCHES)

        ax.axis("on")
        plt.grid(True)

        self.ax.relim()
        self.ax.autoscale_view()

        fig.subplots_adjust(left=0, right=1, bottom=0, top=1, wspace=0, hspace=0)

        canvas = FigureCanvasTkAgg(fig, master=parent)
        canvas.draw()
        canvas.get_tk_widget().place(relx=PLOTTER_X_PLACEMENT, rely=PLOTTER_Y_PLACEMENT)

        parent.update()
