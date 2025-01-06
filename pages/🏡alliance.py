import streamlit as st
import pandas as pd
from load_data import data_alliance_power, data_alliance_merits, last_date

st.sidebar.markdown("# Alliance statistic")
st.title(" Alliance statistic")
st.divider()
st.write("On the left sidebar, you can select an alliance and see the graphs of changes in strength and merits for this alliance below.📊")
st.write("There are two graphs - merits and power, which show the change in this data by day.📉")


list_alliances_power = []
for i in data_alliance_power['name']:
    if i not in list_alliances_power:
        list_alliances_power.append(i)

list_alliances_merits = []
for i in data_alliance_merits['name']:
    if i not in list_alliances_merits:
        list_alliances_merits.append(i)

chose_alliance = st.sidebar.selectbox(
    "Choose alliance:",
    list_alliances_power
)

list_dates = []
for i in data_alliance_power['date']:
    if i not in list_dates:
        list_dates.append(i)





def alliance_stat(parameter, data_alliance, chosen_alliance):

    alliance_statistic = data_alliance[(data_alliance['name'] == chosen_alliance)]
    alliance_series = pd.Series(alliance_statistic[parameter].values, alliance_statistic['date'].astype(str))

    return alliance_series


def calculate(parameter, data_alliance, alliance, start, end):

    data_alliance_start = data_alliance.loc[
        (data_alliance["name"] == alliance) & (data_alliance['date'] == start),
        parameter].iloc[0]

    data_alliance_end = data_alliance.loc[
        (data_alliance["name"] == alliance) & (data_alliance['date'] == end),
        parameter].iloc[0]

    return [data_alliance_start, data_alliance_end]

def list_top_alliances(data_alliance, parameter, all_alliances):
    list_top = []
    last_date = data_alliance['date'].max()
    top = data_alliance[data_alliance['date'] == last_date].sort_values(by=[parameter], ascending=False).head(
        10)
    for alliance in all_alliances:
        if alliance in top['name'].values:
            list_top.append(alliance)
    return list_top

st.divider()
st.caption('You can select two dates and the calculator will show the difference in how much the alliance lost or gained during this period.')

on = st.toggle("Show calculator")
if on:
    start_day = st.selectbox("Chose start date: ", list_dates)
    end_day = st.selectbox("Chose end date: ", list_dates)

    try:
        start_power, end_power = calculate('power', data_alliance_power, chose_alliance, start_day, end_day)
        start_merits, end_merits = calculate('merits', data_alliance_merits, chose_alliance, start_day, end_day)

    except IndexError:
        st.exception(IndexError("Not enough data to count. Try to choose a different date or alliance."))
    except Exception:
        st.exception(Exception("Something going wrong.🤷‍♂️"))
    else:
        st.write(f"As of :blue-background[{start_day}] alliance :blue-background[{chose_alliance}] has the following data:")
        st.write(f"Merits: :green-background[{format(start_merits, ',')}], power: :green-background[{format(start_power,',')}]")

        st.write(f"As of :blue-background[{start_day}] alliance :blue-background[{chose_alliance}] has the following data:")
        st.write(f"Merits: :green-background[{format(end_merits,',')}], power: :green-background[{format(end_power,',')}]")

        st.write(f"Difference merits is: :blue[{format((start_merits-end_merits),',')}]")
        st.write(f"Difference power is: :blue[{format((start_power-end_power), ',')}]")
st.divider()

st.subheader("Power and merits graph for chosen alliance", divider=True)

power, merits = st.columns(2)
if power.button('power', use_container_width=True):
    power.caption(f"{chose_alliance} power statistic ")
    alliance_stat('power', data_alliance_power, chose_alliance)
    st.bar_chart(alliance_stat('power', data_alliance_power, chose_alliance))
if merits.button('merits', use_container_width=True):
    merits.caption(f"{chose_alliance} merits statistic ")
    st.bar_chart(alliance_stat('merits', data_alliance_merits, chose_alliance))

st.divider()

st.subheader("Alliances power TOP 10", divider=True)
st.caption(f"Expand to full screen for a better view. Update date:{last_date}")
try:
    list_top_power = list_top_alliances(data_alliance_power, "power", list_alliances_power)
except Exception:
    st.exception(Exception("Something going wrong.🤷‍♂️"))
else:
    chosen_alliances = st.multiselect(label="Chose alliances", options =list_top_power, default=list_top_power[:3])
    #data_alliance_power['date'] = data_alliance_power['date'].astype(str)
    data_power_top_alliances = data_alliance_power[data_alliance_power["name"].isin(chosen_alliances)]
    st.line_chart(data_power_top_alliances, x='date', y='power', color='name')




st.subheader("Alliances merits TOP 10", divider=True)
st.caption(f"Expand to full screen for a better view. Update date:{last_date}")
try:
    list_top_merits = list_top_alliances(data_alliance_merits, "merits", list_alliances_merits)
except Exception:
    st.exception(Exception("Something going wrong.🤷‍♂️"))
else:
    chosen_alliances = st.multiselect(label="Chose alliances", options =list_top_merits, default=list_top_merits[:3])

    data_merits_top_alliance = data_alliance_merits[data_alliance_merits["name"].isin(chosen_alliances)]
    st.line_chart(data_merits_top_alliance, x='date', y='merits', color='name')

st.divider()




