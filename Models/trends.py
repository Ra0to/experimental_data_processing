from dataclasses import dataclass


@dataclass
class TrendData:
    N: int
    a: float
    b: float


@dataclass
class LinearTrendData(TrendData):
    pass


@dataclass
class ExpTrendData(TrendData):
    pass


@dataclass
class HarmonicTrend:
    N: int
    dt: float
    A: float
    f: float
