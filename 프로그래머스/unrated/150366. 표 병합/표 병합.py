def find_root(cell, i, j):
    ni, nj = i, j
    while True:
        if type(cell[ni][nj]) != tuple:
            return (ni, nj)
        ni, nj = cell[ni][nj][0], cell[ni][nj][1]

def Update(cell, i, j, value):
    root_i, root_j = find_root(cell, i, j)
    cell[root_i][root_j] = value

def Merge(cell, i1, j1, i2, j2):
    root_i1, root_j1 = find_root(cell, i1, j1)
    root_i2, root_j2 = find_root(cell, i2, j2)
    if cell[root_i1][root_j1]:
        for tmp_i in range(50):
            for tmp_j in range(50):
                if cell[tmp_i][tmp_j] == (root_i2, root_j2):
                    cell[tmp_i][tmp_j] = (root_i1, root_j1)
        cell[root_i2][root_j2] = (root_i1, root_j1)
    else:
        for tmp_i in range(50):
            for tmp_j in range(50):
                if cell[tmp_i][tmp_j] == (root_i1, root_j1):
                    cell[tmp_i][tmp_j] = (root_i2, root_j2)
        cell[root_i1][root_j1] = (root_i2, root_j2)

def UNMERGE(cell, i, j):
    root_i, root_j = find_root(cell, i, j)
    val = cell[root_i][root_j]
    for tmp_i in range(50):
        for tmp_j in range(50):
            if cell[tmp_i][tmp_j] == (root_i, root_j):
                cell[tmp_i][tmp_j] = ''
    cell[root_i][root_j] = ''
    cell[i][j] = val

def func(lst, cell):
    if lst[0] == 'UPDATE':
        if len(lst) == 4:
            i, j = int(lst[1])-1, int(lst[2])-1
            Update(cell, i, j, lst[3])
        else:
            for i in range(50):
                for j in range(50):
                    if cell[i][j] == lst[1]:
                        cell[i][j] = lst[2]

    elif lst[0] == 'MERGE':
        i1, j1, i2, j2 = map(int, lst[1:])
        i1, j1, i2, j2 = i1-1, j1-1, i2-1, j2-1
        ci1, cj1 = find_root(cell, i1, j1)
        ci2, cj2 = find_root(cell, i2, j2)
        if ci1 == ci2 and cj1 == cj2:
            return
        Merge(cell, ci1, cj1, ci2, cj2)

    elif lst[0] == 'UNMERGE':
        i, j = int(lst[1])-1, int(lst[2])-1
        UNMERGE(cell, i, j)

    elif lst[0] == 'PRINT':
        i, j = int(lst[1])-1, int(lst[2])-1
        i, j = find_root(cell, i, j)
        return cell[i][j] if cell[i][j] else "EMPTY"


def solution(commands):
    answer = []
    cell = [[''] * 50 for _ in range(50)]
    for command in commands:
        lst = list(command.split(' '))
        res = 0
        res = func(lst, cell)
        if res:
            answer.append(res)

    return answer