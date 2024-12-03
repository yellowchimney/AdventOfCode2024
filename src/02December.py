import requests
from dotenv import load_dotenv
import os

load_dotenv()
session_cookie = os.getenv('session_cookie')

def is_safe(lst):
    return all(0 < (lst[i + 1] - lst[i]) <= 3 for i in range(len(lst) - 1)) or all(
        0 < (lst[i] - lst[i + 1]) <= 3 for i in range(len(lst) - 1)
    )

def count_safe_reports():
    response = requests.get(
        "https://adventofcode.com/2024/day/2/input", cookies={"session": session_cookie}
    )
    data = response.text
    lines = data.strip().split("\n")
    list_of_reports = [line.split() for line in lines]
    list_of_numbers = []
    for lst in list_of_reports:
        numbers = [int(n) for n in lst]
        list_of_numbers.append(numbers)
    list_of_safe_reports = []
    list_of_unsafe_reports = []
    for numbers in list_of_numbers:
        if is_safe(numbers):
            list_of_safe_reports.append(numbers)
        else:
            list_of_unsafe_reports.append(numbers)
    for numbers in list_of_unsafe_reports:
        for i in range(len(numbers)):
            temp_list = numbers[:i] + numbers[i + 1 :]
            if is_safe(temp_list):
                list_of_safe_reports.append(lst)
                break
    return len(list_of_safe_reports)
