def read_array_data(file_path: str) -> tuple[float]:
    file = open(file_path, 'r')
    size = file.readline()
    array = tuple(map(float, file.readline().split()))
    return array
