import struct

from Models.trends import *


def read_trend_data(file_path: str) -> TrendData:
    with open(file_path, 'r') as file:
        data = file.readline().split()
        return TrendData(N=int(data[0]), a=float(data[1]), b=float(data[2]))


def read_linear_trend_data(file_path: str) -> LinearTrendData:
    trend = read_trend_data(file_path)
    return LinearTrendData(N=trend.N, a=trend.a, b=trend.b)


def read_exp_trend_data(file_path: str) -> ExpTrendData:
    trend = read_trend_data(file_path)
    return ExpTrendData(N=trend.N, a=trend.a, b=trend.b)


def read_byte_file(file_path: str, elem_type: str, elem_size: int, count: int) -> tuple:
    with open(file_path, 'rb') as file:
        data = []
        for i in range(count):
            data.append(struct.unpack(elem_type, file.read(elem_size))[0])
        return tuple(data)


def read_float_byte_array_file(file_path: str, count: int) -> tuple:
    return read_byte_file(file_path, 'f', 4, count)
