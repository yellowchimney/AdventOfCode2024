import requests
from dotenv import load_dotenv
import os

load_dotenv()
session_cookie = os.getenv('session_cookie')

def get_input():
    response = requests.get(
        "https://adventofcode.com/2024/day/6/input", cookies={"session": session_cookie}
    )
    data = response.text
    lines = data.strip().split("\n")
    return lines

def find_visited():
    grid = get_input()
    rows, cols = len(grid), len(grid[0])
    for i, row in enumerate(grid):
        if "^" in row:
            current_position = (row.index("^"), i)
            x = row.index("^")
            y = i
            break
    directions = {
        "up" : 
        {
            "next" : "right",
            "calc" : (0,-1)
        },
        "right" :
        {
            "next" : "down",
            "calc" : (1,0)
        },
        "down" :
        {
            "next" : "left",
            "calc" : (0,1)
        },
        "left" :
        {
            "next" : "up",
            "calc" : (-1,0)
        }
    }
    
    current_direction = directions["up"]
    list_of_visited = [current_position]

    while True:
        dx, dy = current_direction["calc"]
        next_x, next_y = x + dx, y + dy
        
        # Check if we're about to leave the grid
        if not (0 <= next_y < rows and 0 <= next_x < cols):
            break  # Exit without adding the out-of-bounds position
            
        # Then check for wall if we're in bounds
        if grid[next_y][next_x] == '#':
            current_direction = directions[current_direction["next"]]
        else:
            x, y = next_x, next_y
            current_position = (x, y)
            list_of_visited.append(current_position)

    unique_positions = set(list_of_visited)
    print(len(list_of_visited))
    print(len(unique_positions))






find_visited()

def check_if_loops(grid, test_x, test_y):
    test_grid = [list(row) for row in grid]
    test_grid[test_y][test_x] = '#'
    
    for i, row in enumerate(test_grid):
        if "^" in row:
            x = row.index("^")
            y = i
            break
    
    directions = {
        "up": {"next": "right", "calc": (0,-1)},
        "right": {"next": "down", "calc": (1,0)},
        "down": {"next": "left", "calc": (0,1)},
        "left": {"next": "up", "calc": (-1,0)}
    }
    
    current_direction = directions["up"]
    visited_states = set()
    current_state = (x, y, "up")
    
    while True:
        dx, dy = current_direction["calc"]
        next_x, next_y = x + dx, y + dy
        
        if not (0 <= next_y < len(test_grid) and 0 <= next_x < len(test_grid[0])):
            return False
            
        if test_grid[next_y][next_x] == '#':
            current_direction = directions[current_direction["next"]]
            current_dir_name = [k for k,v in directions.items() if v == current_direction][0]
            current_state = (x, y, current_dir_name)
            
            if current_state in visited_states:
                return True
            visited_states.add(current_state)
        else:
            x, y = next_x, next_y
            current_dir_name = [k for k,v in directions.items() if v == current_direction][0]
            current_state = (x, y, current_dir_name)
            
            if current_state in visited_states:
                return True
            visited_states.add(current_state)
    
def find_loop_positions():
    grid = get_input()
    loop_positions = []
    
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == '.': 
                if check_if_loops(grid, x, y):
                    loop_positions.append((x, y))
    
    return loop_positions

positions = find_loop_positions()
print(f"Found {len(positions)} positions that create loops:")

