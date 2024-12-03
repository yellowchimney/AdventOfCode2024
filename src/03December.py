import requests
import re
from dotenv import load_dotenv
import os

load_dotenv()
session_cookie = os.getenv('session_cookie')

def get_input():
    response = requests.get(
        "https://adventofcode.com/2024/day/3/input", cookies={"session": session_cookie}
    )
    data = response.text
    return data


def get_enabled():
    data = get_input()
    pattern = "do\(\)"
    do_chunks = re.split(pattern, data)
    do_list = []
    for chunk in do_chunks:
        pattern = "don't\(\)"
        dont_chunks = re.split(pattern, chunk)
        do_list.append(dont_chunks[0].strip())

    return do_list


def clean_data():
    do_list = get_enabled()
    full_list_of_muls = []
    for do_chunk in do_list:
        pattern = "mul\(\d+,\d+\)"
        temp_list = re.findall(pattern, do_chunk)
        full_list_of_muls.extend(temp_list)
    return full_list_of_muls


def sum_muls():
    list_of_muls = clean_data()
    results = []
    for mul in list_of_muls:
        pattern = "\d+"
        digits_only = re.findall(pattern, mul)
        results.append(int(digits_only[0]) * int(digits_only[1]))
    return sum(results)
