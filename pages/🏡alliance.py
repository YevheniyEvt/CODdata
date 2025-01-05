import datetime
import streamlit as st
import pandas as pd
from load_data import data_alliance_power, data_alliance_merits
# st.write(datetime.date.today())
# st.write(datetime.date.today().strftime('%m.%d.%y'))


st.sidebar.markdown("# Alliance statistic")
st.title(" Alliance statistic")
st.divider()
st.write("On the left sidebar, you can select an alliance and see the graphs of changes in strength and merits for this alliance below.📊")
st.write("There are two graphs - merits and power, which show the change in this data by day.📉")

alliances = []
for i in data_alliance_power['name']:
    if i not in alliances:
        alliances.append(i)
dates = []
for i in data_alliance_power['date']:
    if i not in dates:
        dates.append(i)

alliance = st.sidebar.selectbox(
    "Choose alliance:",
    alliances
)

def alliance_stat(parameter, data_alliance):
    alliance_statistic = data_alliance[(data_alliance['name'] == alliance)]
    alliance_series = pd.Series(alliance_statistic[parameter].values, alliance_statistic['date'])
    return st.bar_chart(alliance_series)

def calculate(parameter, data_alliance):
    data_alliance_start = data_alliance.loc[
        (data_alliance["name"] == alliance) & (data_alliance['date'] == start_date),
        parameter].iloc[0]

    data_alliance_end = data_alliance.loc[
        (data_alliance["name"] == alliance) & (data_alliance['date'] == end_day),
        parameter].iloc[0]

    return [data_alliance_start, data_alliance_end]


def top_alliance(data_alliance, parameter):
    top_=[]
    last_date = data_alliance['date'].max()
    top_alliances = data_alliance_power[data_alliance['date'] == last_date].sort_values(by=[parameter], ascending=False).head(10)
    for alli in alliances:
        if alli in top_alliances['name'].values:
            top_.append(alli)
    return data_alliance[data_alliance["name"].isin(top_)]


st.divider()
st.caption('You can select two dates and the calculator will show the difference in how much the alliance lost or gained during this period.')

on = st.toggle("Show calculator")
if on:
    start_date = st.selectbox("Chose start date: ", dates)
    end_day = st.selectbox("Chose end date: ", dates)

    try:
        start_power, end_power = calculate('power', data_alliance_power)
        start_merits, end_merits = calculate('merits', data_alliance_merits)

    except IndexError:
        st.exception(IndexError("Not enough data to count. Try to choose a different date or alliance."))
    except Exception:
        st.exception(Exception("Something going wrong.🤷‍♂️"))
    else:
        st.write(f"As of :blue-background[{start_date}] alliance :blue-background[{alliance}] has the following data:")
        st.write(f"Merits: :green-background[{format(start_merits, ',')}], power: :green-background[{format(start_power,',')}]")

        st.write(f"As of :blue-background[{start_date}] alliance :blue-background[{alliance}] has the following data:")
        st.write(f"Merits: :green-background[{format(end_merits,',')}], power: :green-background[{format(end_power,',')}]")

        st.write(f"Difference merits is: :blue[{format((start_merits-end_merits),',')}]")
        st.write(f"Difference power is: :blue[{format((start_power-end_power), ',')}]")
st.divider()

st.subheader("Power and merits graph for chosen alliance", divider=True)

power, merits = st.columns(2)
if power.button('Power', use_container_width=True):
    power.caption(f"{alliance} power statistic ")
    alliance_stat('power', data_alliance_power)

if merits.button('merits', use_container_width=True):
    merits.caption(f"{alliance} merits statistic ")
    alliance_stat('merits', data_alliance_merits)

st.divider()

st.subheader("Alliances power TOP 10", divider=True)
st.caption("Expand to full screen for a better view")
try:
    data_p = top_alliance(data_alliance_power, "power")
except pd.errors.IndexingError:
    st.exception(pd.errors.IndexingError("No data to display.🤷‍♂️"))
except Exception:
    st.exception(Exception("Something going wrong.🤷‍♂️"))
else:
    st.line_chart(data_p, x='date', y='power', color='name')

st.subheader("Alliances merits TOP 10", divider=True)
st.caption("Expand to full screen for a better view")
try:
    data_m = top_alliance(data_alliance_merits, "merits")
except pd.errors.IndexingError:
    st.exception(pd.errors.IndexingError("No data to display.🤷‍♂️"))
except Exception:
    st.exception(Exception("Something going wrong.🤷‍♂️"))
else:
    st.line_chart(data_m, x='date', y='merits', color='name')

st.divider()




