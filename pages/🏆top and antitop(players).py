import streamlit as st
import pandas as pd
from load_data import data_players_statistic, last_date, first_date


st.title("TOP AC-DC")
st.sidebar.markdown("# PLayer statistic")
st.divider()

st.write('Here you can see:')
st.write('1. 10 players from the AC-DC alliances who have the highest merits as of the last data update date📈')
st.write('2. 10 players from the AC-DC alliances who have the lowest merits as of the last data update date📉')
st.write('3. 10 players from the AC-DC alliances who have a merit of zero as of the last data update date0️⃣')
st.write("4. How many players have >1M merits, >2M merits, >5M merits, >10M merits, >20M merits📊")
st.write("5. Number of killed units, healed units and dead units :green-background[during the season]📃")

st.divider()

col = ["id", "name", "alliance", "power", "merits", "killed", "dead", "healed", "date"]

data_players_statistic2 = pd.DataFrame(data_players_statistic[col[1:]].values,
                                       index=data_players_statistic['id'],
                                       columns=col[1:])


data_first_day = data_players_statistic2[data_players_statistic2['date'] == first_date]
data_last_day = data_players_statistic2[data_players_statistic2['date'] == last_date]

def top_ten():

    top_player = data_players_statistic2.loc[data_players_statistic2['date'] == last_date].sort_values('merits')
    top_10_merits = top_player.sort_values(by=['merits'], ascending=False)
    top_10_merits_without_zero = top_10_merits.loc[top_10_merits['merits'] != 0]
    top_data = top_10_merits_without_zero[['name', 'alliance', "power", 'merits']]

    return top_data


def percentage(number):

    merit_more_data = data_players_statistic[data_players_statistic['date'] == last_date]
    total = merit_more_data.shape[0]
    merit_more = int(merit_more_data[merit_more_data['merits'] > number].shape[0] / total * 100)

    return merit_more


def calculate_season_data(name_new_col, parameter):

    st.subheader(parameter.title(), divider=True)
    st.caption(f"Update date: {last_date}")
    show_parameter = st.checkbox(f"Click to watch {parameter} ")
    if show_parameter:
        data_players_statistic2[name_new_col] = (data_last_day[parameter] - data_first_day[parameter])
        st.write(data_players_statistic2[["name", name_new_col]])


st.subheader("Merits ", divider=True)
top_10, antitop_10, merits_zero = st.columns(3)
if top_10.button('Top 10', use_container_width=True):
    st.markdown(f"# TOP 10 merits")
    st.caption(f"Update date: {last_date}")
    st.write(top_ten().head(10))

if antitop_10.button('Antitop 10', use_container_width=True):
    st.markdown(f"# Antitop 10 merits")
    st.caption(f"Update date: {last_date}")
    st.caption('Without players with 0 merits')
    st.write(top_ten().tail(10))

if merits_zero.button('ZERO merits', use_container_width=True):
    merits_zero = data_players_statistic2.loc[data_players_statistic2['merits'] == 0]
    st.markdown(f"# 0 merits")
    st.caption(f"Update date: {last_date}")
    st.write(merits_zero[['name', 'alliance', "power", 'merits']])

st.divider()

st.subheader("Merits/players ", divider=True)
st.caption(f'Here you can see statistics in percentages for the merits of players in the AC-DC alliance.📊')
st.caption(f"Update date: {last_date}")

parameters_merits = [1000000, 2000000, 5000000, 10000000, 20000000]
data_merits = [percentage(i) for i in parameters_merits]
data_more = pd.Series(data_merits,
                      ['>1M merits', '>2M merits', '>5M merits', '>10M merits', '>20M merits'])
st.bar_chart(data_more, y_label="percentage of players", x_label="More then N merits")

st.divider()

#TODO try when have more data
#TODO max_kill = data_players_statistic2["kill_season"].max()
#TODO name_killer = data_players_statistic2.loc[data_players_statistic2["kill_season"] == max_kill, "name"]

calculate_season_data('kill_season', "killed")
calculate_season_data('heal_season', "healed")
calculate_season_data('dead_season', "dead")
