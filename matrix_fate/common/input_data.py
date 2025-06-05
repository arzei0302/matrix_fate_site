import json

def normalize_input_data(data: dict) -> dict:
    return json.loads(json.dumps(data, sort_keys=True))


def is_fake_date(day: int, month: int, year: int) -> bool:
    return day == 1 and month == 1 and year == 2025


def is_fake_compatibility_input(day1: int, month1: int, year1: int, day2: int, month2: int, year2: int) -> bool:
    return (
        is_fake_date(day1, month1, year1) and
        is_fake_date(day2, month2, year2)
    )

