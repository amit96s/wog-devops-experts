import os

def clean_screen():
    os.system('cls' if os.name == 'nt' else 'clear')



score_file_name = 'score.txt'



def get_score():
    if os.path.isfile(score_file_name):
        score = open(score_file_name,'r').read()
        return score
    else:
        bad_return_code = 400
        return bad_return_code
