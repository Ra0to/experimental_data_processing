from dataclasses import dataclass


@dataclass
class PlotData:
    xs: tuple[float]
    ys: tuple[float]

    def __init__(self, xs, ys):
        self.xs = tuple(xs)
        self.ys = tuple(ys)

    def __len__(self):
        return len(self.xs)
