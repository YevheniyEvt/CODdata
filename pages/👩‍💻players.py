import streamlit as st
import pandas as pd
from load_data import data_players_statistic, data_name_id

st.sidebar.markdown("# PLayer statistic")
names = []
for i in data_name_id['name']:
    if i not in names:
        names.append(i)

player = st.sidebar.selectbox(
    "Choose player:",
    names
)

def parameter_stat(player_id, parameter):

    data_player = data_players_statistic[data_players_statistic['id'] == player_id]
    parameter_player = data_player[[parameter, 'date']]
    parameter_data = pd.Series(parameter_player[parameter].values, parameter_player['date']) #.astype(str)
    widget = st.bar_chart(parameter_data, y_label=parameter.upper(), x_label='date'.upper())        #parameter_data.apply(lambda x:f"{x:,}") спробувати потім

    return widget


st.title('Players statistic')
st.write("Select the player's name on the left panel")
st.write('Units killed, units dead, units healed are total for flayer, :green-background[not for the season]🗂')

st.divider()
st.caption('Here you can see how the data changed over a period of time. Dates are the dates the data was updated.📊')

player_id = data_name_id.loc[data_name_id['name'] == player, 'id'].iloc[0]
st.subheader(f" Name: {player}, (id:{player_id})", divider=True)

power, merits, killed, dead, healed = st.columns(5)
if power.button('Power', use_container_width=True):
    parameter_stat(player_id, 'power')

if merits.button('Merits', use_container_width=True):
    parameter_stat(player_id, 'merits')

if killed.button('Units killed', use_container_width=True):
    parameter_stat(player_id, 'killed')

if dead.button('Units dead', use_container_width=True):
    parameter_stat(player_id, 'dead')

if healed.button('Units healed', use_container_width=True):
    parameter_stat(player_id, 'healed')
