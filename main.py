import streamlit as st
from PIL import Image
import pandas as pd
import os
from datetime import date
import classes

today = date.today()
a = str(today)
a = a.split('-')
today = ('/'.join(a))

sss = 'fifa'
# data = pd.read_csv(r'C:\Users\emils\PycharmProjects\worldCup\' + {sss} + '.csv')
data = pd.read_csv(r'a' + sss + '.csv')
# workdata = pd.read_csv(r'C:\Users\emils\PycharmProjects\worldCup\nepredhorata.csv')
# internaldata = pd.read_csv(r'C:\Users\emils\PycharmProjects\worldCup\a' + sss + '.csv')
# predictiontable = pd.read_csv(r'C:\Users\emils\PycharmProjects\worldCup\PREDICTIONTABLE.csv')
# predictiontable1 = pd.read_csv(r'C:\Users\emils\PycharmProjects\worldCup\PREDICTIONTABLE.csv')


image = Image.open(r'flags/7068215.jpg')

st.sidebar.header('Какво ти трябва')
selected  = st.sidebar.selectbox('', ['Начало','Искам да видя мачовете','Искам да видя на кое място съм','Другите ко са казали']) # , 'Тоя път ще ги уцеля брат'

if selected == 'Начало':
    st.image(image, use_column_width=True)
    variable = 'Следващ Мач'
    st.markdown(""" <style> .font {
    font-size:50px ; font-family: 'Cooper Black'; color: #000000;} 
    </style> """, unsafe_allow_html=True)
    st.markdown(f'<p class="font">{variable}</p>', unsafe_allow_html=True)
    nextgame = classes.next_game(data)
    ngsplit = nextgame.split(' - ')
    st.markdown(f'<p class="font">{nextgame}</p>', unsafe_allow_html=True)
    flag1,flag2 = classes.get_flag(ngsplit[0].lower(),ngsplit[1].lower())
    st.image([flag1,flag2],width=300)

if selected == 'Искам да видя мачовете':
    predictiontable1 = pd.read_csv(r'gamessimplified.csv')
    st.dataframe(data=predictiontable1,width=1000,height=2000)

if selected == 'Искам да видя на кое място съм':
    leader = pd.read_csv('leaderboard.csv')
    leader = leader.sort_values('Точки', ascending=False)
    b = [x for x in range(1, 13)]
    leader['Място'] = b
    leader.set_index('Място', inplace=True)
    st.dataframe(data=leader,width=1000,height=450)

if selected == 'Другите ко са казали':
    preds = pd.read_csv('predictions.csv')
    preds.set_index('Мачове',inplace=True)
    st.dataframe(data=preds,width=1500,height=2000)
# if selected == 'Тоя път ще ги уцеля брат':
#     # st.image(image, use_column_width=True)
#     name = st.text_input('Кой си ти?')
#     res, breaker = classes.check_if_participating(name)
#     st.markdown(f'<p class="font">{res}</p>', unsafe_allow_html=True)
#     if breaker:
#         date_input = st.date_input('Кой ден')
#         date_input = str(date_input)
#         date_input = date_input.split('-')
#         date_input = ('/'.join(date_input))
#         if date_input < today:
#             st.write('Тъп ли си, закъсня')
#         else:
#             st.write('Ай хуу, как ги мислиш')
#             todaysgames = workdata.loc[workdata['Comparator'] == date_input]
#             todaysgames.drop('Comparator',axis=1,inplace=True)
#
#             # todaysgames.index = todaysgames['Date']
#             if len(todaysgames['Date'] == 0):
#                 st.write(todaysgames)
#                 preds = []
#
#                 for i in range(len(todaysgames['Home Team'])):
#                     prediction = st.text_input(label=("Мач " + str(i+1)))
#                     preds.append(prediction)
#                 if len(preds) == len(todaysgames['Home Team']):
#                     start = todaysgames.index[0]
#                     end = todaysgames.index[-1]
#                     predictiontable.iloc[start:end + 1][name] = preds
#                     butt = st.button('Готов ли си?',on_click=predictiontable.to_csv('PREDICTIONTABLE1.csv',index=False))
#                     classes.update_dataframe(predictiontable1, predictiontable, name=name)
#                     predictiontable.to_csv('PREDICTIONTABLE1.csv',index=False)
#                     st.write(predictiontable)
#
#                     # predictiontable.update(predictiontable)
#                     # predictiontable1[name] = predictiontable[name]
#                     # predictiontable.to_csv('PREDICTIONTABLE.csv',index=False)
#             else:
#                 st.write('Няма мачове')