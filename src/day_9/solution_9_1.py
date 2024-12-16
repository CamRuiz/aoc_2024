from src.utilities.timer import run_timed


def get_compacted_disk_map(disk_map: str) -> list[int]:

    disk_map = [int(x) for x in disk_map]
    start_index = 0
    end_index = len(disk_map) - 1

    compacted_disk = []
    while start_index < end_index:
        if start_index % 2 == 0:
            compacted_disk += [start_index // 2] * disk_map[start_index]
            start_index += 1
        else:
            spaces_to_fill = disk_map[start_index]
            values_to_add_from_end = disk_map[end_index]

            if values_to_add_from_end < spaces_to_fill:
                compacted_disk += [end_index // 2] * values_to_add_from_end
                disk_map[start_index] -= values_to_add_from_end
                end_index -= 2
            elif values_to_add_from_end == spaces_to_fill:
                compacted_disk += [end_index // 2] * values_to_add_from_end
                start_index += 1
                end_index -= 2
            else:
                compacted_disk += [end_index // 2] * spaces_to_fill
                disk_map[end_index] -= spaces_to_fill
                start_index += 1

    return compacted_disk


def solution() -> None:
    with open('src/day_9/input_9_1.txt', 'r') as file:
        input_text = file.read()

    compacted_disk_map = get_compacted_disk_map(input_text)

    print(sum(file_id * i for i, file_id in enumerate(compacted_disk_map)))


def main() -> None:
    run_timed(solution)


if __name__ == "__main__":
    main()