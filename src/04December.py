import requests
import re
from dotenv import load_dotenv
import os

load_dotenv()
session_cookie = os.getenv('session_cookie')

def get_input():
    response = requests.get(
        "https://adventofcode.com/2024/day/4/input", cookies={"session": session_cookie}
    )
    data = response.text
    lines = data.strip().split("\n")
    return lines

def count_horizontal():
    lines = get_input()
    count = 0
    for line in lines:
        if "XMAS" or "SAMX" in line:
            occurences_xmas = line.count("XMAS")
            occurences_samx = line.count("SAMX")
            count += (occurences_samx + occurences_xmas)
    return count

def generate_subsets(lines, n=4):
    for i in range(len(lines) - n + 1):
        yield lines[i:i+n]

def count_vertical():
    lines = get_input()
    xmas_indices = []  
    for subset in generate_subsets(lines):
        for i in range(len(subset[0])): 
            word = ''.join(line[i] for line in subset)
            if word == "XMAS" or word == "SAMX":
                xmas_indices.append(i)

    return len(xmas_indices)

def count_diagonal():
    lines = get_input()
    xmas_indices = []  
    for subset in generate_subsets(lines):
        for i in range(len(subset[0])):
            if i + 3 < len(subset[0]):
                downward = ''.join(subset[j][i + j] for j in range(4))
                if downward == "XMAS" or downward == "SAMX":
                    xmas_indices.append(("downward", i))    

            if i - 3 >= 0:
                upward = ''.join(subset[j][i - j] for j in range(4))
                if upward == "XMAS" or upward == "SAMX":
                    xmas_indices.append(("upward", i))

    return len(xmas_indices)
               

def count_x_mas_part_one():
    lines = get_input()
    xmas_indices = []
    for subset in generate_subsets(lines, n=3):
        for i in range(len(subset[0])):
            if i + 2 < len(subset[0]):
                downward = ''.join(subset[j][i + j] for j in range(3))
                if downward == "MAS" or downward == "SAM":
                    x = i + 2
                    upward = ''.join(subset[j][x - j] for j in range(3))
                    if upward == "MAS" or upward == "SAM":
                        xmas_indices.append((i))

    return len(xmas_indices)


if __name__ == "__main__":
    horizontal_occurences = count_horizontal()
    vertical_occurences = count_vertical()
    diagonal_occurences = count_diagonal()
    total_occurences = horizontal_occurences + vertical_occurences + diagonal_occurences
    print(total_occurences, "<<< part 1")

    print(count_x_mas_part_one(), "<<< part 2")