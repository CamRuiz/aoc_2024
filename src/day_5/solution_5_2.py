import re

from src.day_5.solution_5_1 import PageRule
from src.utilities.timer import run_timed


def check_and_fix_update(update: str, single_page_rule_regex: str) -> tuple[bool, str]:

    if single_page_rule_regex == '':
        return True, update

    matches = re.findall(single_page_rule_regex, update)
    is_valid = len(matches) == 0
    if is_valid:
        return is_valid, update

    for match in matches:
        first_page = match[-4:]
        second_page = match[:4]
        update = update.replace(first_page, second_page)
        update = update.replace(second_page, first_page, 1)

    return is_valid, update


def solution() -> None:
    with open('src/day_5/input_5_1.txt', 'r') as file:
        input_text = file.read()

    page_rules_string, updates_string = input_text.split('\n\n')
    page_rules = [PageRule.from_string(x) for x in page_rules_string.splitlines()]

    middle_page_sum = 0
    single_page_rule_regex = '|'.join(
        page_rule.search_pattern for page_rule in page_rules
    )
    for update in updates_string.splitlines():
        numbers_to_check = update.split(',')
        prepared_update = ',' + update + ','
        attempt = 0
        is_valid = False
        while not is_valid:
            attempt += 1
            is_valid, prepared_update = check_and_fix_update(prepared_update, single_page_rule_regex)

        if attempt > 1:
            update_list = prepared_update[1:-1].split(',')
            middle_page_sum += int(update_list[len(update_list) // 2])

    print(middle_page_sum)


def main() -> None:
    run_timed(solution)


if __name__ == "__main__":
    main()