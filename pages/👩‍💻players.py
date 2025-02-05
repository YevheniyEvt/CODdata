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

def parameter_stat(data, p_id, parameter):

    data_player = data[data['id'] == p_id]
    parameter_player = data_player[[parameter, 'date']]
    parameter_data = pd.Series(parameter_player[parameter].values, parameter_player['date'].astype(str))

    return parameter_data


st.title('Players statistic')
st.write("Select the player's name on the left panel")
st.write('Units killed, units dead, units healed are total for player, :green-background[not for the season]🗂')

st.divider()
st.caption('Here you can see how the data changed over a period of time. Dates are the dates the data was updated.📊')

player_id = data_name_id.loc[data_name_id['name'] == player, 'id'].iloc[0]
st.subheader(f" Name: {player}, (id:{player_id})", divider=True)

power, merits, killed, dead, healed = st.columns(5)
if power.button('Power', use_container_width=True):
    widget_power = parameter_stat(data_players_statistic, player_id, 'power')
    st.bar_chart(widget_power, y_label='power'.upper(), x_label='date'.upper())

if merits.button('Merits', use_container_width=True):
    widget_merits = parameter_stat(data_players_statistic, player_id, 'merits')
    st.bar_chart(widget_merits, y_label='merits'.upper(), x_label='date'.upper())

if killed.button('Units killed', use_container_width=True):
    widget_killed = parameter_stat(data_players_statistic, player_id, 'killed')
    st.bar_chart(widget_killed, y_label='killed'.upper(), x_label='date'.upper())

if dead.button('Units dead', use_container_width=True):
    widget_dead = parameter_stat(data_players_statistic, player_id, 'dead')
    st.bar_chart(widget_dead, y_label='dead'.upper(), x_label='date'.upper())

if healed.button('Units healed', use_container_width=True):
    widget_healed = parameter_stat(data_players_statistic, player_id, 'healed')
    st.bar_chart(widget_healed, y_label='healed'.upper(), x_label='date'.upper())
