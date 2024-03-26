from board import board

path = [0]

print("Calculating...")

def get_space(num:int) -> dict:
    for space in board:
        if space['num'] == num:
            return space
        
def backspace():
    num = path.pop()
    del_space = get_space(num)
    del_space['visited'] = False
    del_space['attempted'] = True
    for space in del_space['moves']:
        get_space(space)['attempted'] = False


def step():
    max_index = len(path)-1
    last_space = path[max_index]
    moves = get_space(last_space)['moves']
    path_found = False
    for space in moves:
        if get_space(space)['visited'] is False and get_space(space)['attempted'] is False:
            path.append(space)
            get_space(space)['visited'] = True
            path_found = True
            break
    if path_found is False:
        backspace()

while len(path) < 25:
    step()

print(path)