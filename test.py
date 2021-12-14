from pathlib import Path


def calculate_central_position(crab_positions, part2=True):
    crab_distance_to_index = list(map(lambda i: list(map(lambda index: abs(i[0] - index), crab_positions)), enumerate(crab_positions)))
    if part2:
        total_fuel_list = list(map(lambda crabs: sum(int((i**2+i)/2) for i in crabs), crab_distance_to_index))
    else:
        total_fuel_list = list(map(sum, crab_distance_to_index))
    least_fuel = min(total_fuel_list)
    central_position = total_fuel_list.index(least_fuel)
    return central_position, least_fuel


def get_crab_positions(file: Path):
    return list(map(int, file.read_text().strip().split(',')))


if __name__ == '__main__':
    print(calculate_central_position(get_crab_positions(file=Path('./input7.csv'))))