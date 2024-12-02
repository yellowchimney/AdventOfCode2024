import requests
from pprint import pprint


def is_safe(lst):
    return (
        all(0 < (lst[i+1] - lst[i]) <= 3 for i in range(len(lst)-1)) or
        all(0 < (lst[i] - lst[i+1]) <= 3 for i in range(len(lst)-1))
    )

def count_safe_reports():
    session_cookie = '53616c7465645f5f723404f1d3280adc652e5aa2b176b948585f390efe6a94d3c8e6ba731084466f8cd96ebe6aad96712a8c0d04330476b6b5def86f2206eaa9'
    response = requests.get('https://adventofcode.com/2024/day/2/input', cookies={'session':session_cookie})
    data = response.text
    lines = data.strip().split('\n')
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
            temp_list = numbers[:i] + numbers[i+1:]
            if is_safe(temp_list):
                list_of_safe_reports.append(lst)
                break
    return len(list_of_safe_reports)      
    


