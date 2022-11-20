import pandas as pd
import numpy as np
from PIL import Image

def next_game(data):
    for i, res in enumerate(data.Result):
        if type(res) == str:
            continue
        if np.isnan(res):
            nextgame = str(data['Home Team'][i]) + ' - '  + str(data['Away Team'][i])
            print(data['Home Team'][i], data['Away Team'][i])
            break
    return nextgame

def get_flag(home,away):
    flag1 = Image.open(r'C:\Users\emils\PycharmProjects\worldCup\flags/a' + home + '.jpg') # C:\Users\emils\PycharmProjects\worldCup\
    flag2 = Image.open(r'C:\Users\emils\PycharmProjects\worldCup\flags/a' + away + '.jpg')
    return flag1,flag2

def check_if_participating(name):
    participants = ['Емил','Адо','Митко','Фахри','Геша','Синан','Попа','Владито','Иво','Коко','Паоло','Стоян']
    if name in participants:
        return 'Давай', True
    else:
        return 'Не участваш, балък', False

def update_dataframe(data1,data2,name):
    data1[name] = data2[name]
    data1.to_csv("PREDICTIONTABLE1.csv",index=False)