import os

def add_score(difficulty_level=0):
    score_to_add = (int(difficulty_level) * 3) +5
    if os.path.isfile('score.txt'):
        current_score = open('score.txt','r').read()

        new_score = score_to_add + int(current_score)
        open('score.txt','w').write(str(new_score))

    else:
        open('score.txt','w').write(str(0))
        add_score(difficulty_level)