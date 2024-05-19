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

        canvas = FigureCanvasTkAgg(fig, master=parent)
        canvas.draw()
        canvas.get_tk_widget().place(relx=PLOTTER_X_PLACEMENT, rely=PLOTTER_Y_PLACEMENT)
