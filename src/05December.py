import csv
from collections import defaultdict, deque


def get_data():
    with open("./data/reports.txt", "r") as f:
        contents_txt = f.read()
        reports = contents_txt.split("\n")
        lines = []
        for report in reports:
            line = report.split(",")
            lines.append(line)

    with open("./data/report_rules.csv", "r") as f:
        contents = csv.reader(f)
        rules = [tuple(row) for row in contents]
    return lines, rules


def sum_middles(list_of_manuals):
    middles = []
    for manual in list_of_manuals:
        x = int(len(manual) / 2)
        middles.append(manual[x])
    num_middles = [int(n) for n in middles]
    return sum(num_middles)


def get_safe_manuals():
    lines, rules = get_data()

    safe = []
    need_sorting = []
    for line in lines:
        indices = {num: i for i, num in enumerate(line)}
        valid = True
        for a, b in rules:
            if a in indices.keys() and b in indices.keys():
                if indices[a] >= indices[b]:
                    valid = False

        if valid:
            safe.append(line)
        else:
            need_sorting.append(line)

        list_of_sorted = []

    for line in need_sorting:
        graph = defaultdict(list)
        dependencies = defaultdict(int)

        for number in line:
            dependencies[number] = 0

        for a, b in rules:
            if a in line and b in line:
                graph[a].append(b)
                dependencies[b] += 1
        print(dependencies)


        queue = deque([num for num in line if dependencies[num] == 0])
        sorted_list = []
        print(line)
        while queue:
            current = queue.popleft()
            sorted_list.append(current)

            for neighbor in graph[current]:
                dependencies[neighbor] -= 1
                if dependencies[neighbor] == 0:
                    queue.append(neighbor)


        list_of_sorted.append(sorted_list)

    part_1 = sum_middles(safe)
    part_2 = sum_middles(list_of_sorted)

    print(part_1)
    print(part_2)


get_safe_manuals()
