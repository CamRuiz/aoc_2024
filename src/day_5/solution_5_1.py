import re

from src.utilities.timer import run_timed


class PageRule:
    def __init__(self, first_page: str, second_page: str) -> None:
        self.first_page = first_page
        self.second_page = second_page
        self.search_pattern = fr',{self.second_page},.*,{self.first_page},'

    @classmethod
    def from_string(cls, page_rule_string: str) -> 'PageRule':
        first_page, second_page = page_rule_string.split('|')
        return cls(first_page, second_page)

    def check_if_rule_violated(self, update: str) -> bool:
        matches = re.search(self.search_pattern, update)
        return matches is not None


def check_all_page_rules(update: str, page_rules: list[PageRule]) -> bool:

    for page_rule in page_rules:
        if page_rule.check_if_rule_violated(update):
            return False
    return True


def check_all_page_rules_with_single_regex(update: str, single_page_rule_regex: str) -> bool:

    matches = re.search(single_page_rule_regex, update)
    return matches is None


def solution() -> None:
    with open('src/day_5/input_5_1.txt', 'r') as file:
        input_text = file.read()

    page_rules_string, updates_string = input_text.split('\n\n')
    page_rules = [PageRule.from_string(x) for x in page_rules_string.splitlines()]

    middle_page_sum = 0
    single_page_rule_regex = '|'.join(page_rule.search_pattern for page_rule in page_rules)
    for update in updates_string.splitlines():
        prepared_update = ',' + update + ','
        # if check_all_page_rules(update, page_rules): # Using a single regex took 0.02 seconds compared to 1.7 seconds
        if check_all_page_rules_with_single_regex(prepared_update, single_page_rule_regex):
            update_list = update.split(',')
            middle_page_sum += int(update_list[len(update_list) // 2])

    print(middle_page_sum)


def main() -> None:
    run_timed(solution)


if __name__ == "__main__":
    main()