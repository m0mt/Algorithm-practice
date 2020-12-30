row = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
move_type = {'R': (1, 0), 'L': (-1, 0), 'B': (0, -1), 'T': (0, 1),
             'RT': (1, 1), 'LT': (-1, 1), 'RB': (1, -1), 'LB': (-1, -1)
            }
king_pos, rock_pos, N = input().split()
N = int(N)
king_pos = (row.index(king_pos[0]), int(king_pos[1]) - 1)
rock_pos = (row.index(rock_pos[0]), int(rock_pos[1]) - 1)
for _ in range(N): 
    move = input()
    _king_pos = tuple(sum(i) for i in zip(king_pos, move_type[move]))
    _rock_pos = rock_pos
    
    if -1 < _king_pos[0] < 8 and -1 < _king_pos[1] < 8:
        if _king_pos == _rock_pos :
            _rock_pos = tuple(sum(j) for j in zip(rock_pos, move_type[move]))
            if -1 < _rock_pos[0] < 8 and -1 < _rock_pos[1] < 8:
                king_pos = _king_pos
                rock_pos = _rock_pos
        else :
            king_pos = _king_pos


king_pos = row[king_pos[0]] + str(king_pos[1] + 1)
rock_pos = row[rock_pos[0]] + str(rock_pos[1] + 1)
print(king_pos, rock_pos, sep='\n')
            

    # if -1 < _king_pos[0] < 8 and -1 < _king_pos[1] < 8 and -1 < _rock_pos[0] < 8 and -1 < _rock_pos[0] < 8:
    #     king_pos = _king_pos
    #     rock_pos = _rock_pos
