from Models.trends import *


def read_trend_data(file_path: str) -> TrendData:
    file = open(file_path, 'r')
    data = file.readline().split()
    return TrendData(N=int(data[0]), a=float(data[1]), b=float(data[2]))


def read_linear_trend_data(file_path: str) -> LinearTrendData:
    trend = read_trend_data(file_path)
    return LinearTrendData(N=trend.N, a=trend.a, b=trend.b)


def read_exp_trend_data(file_path: str) -> ExpTrendData:
    trend = read_trend_data(file_path)
    return ExpTrendData(N=trend.N, a=trend.a, b=trend.b)
