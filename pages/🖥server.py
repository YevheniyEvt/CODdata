import streamlit as st
import pandas as pd
from load_data import data_alliance_power, data_alliance_merits, server_names, server_list

st.sidebar.markdown("# Server statistic")
st.title(" Server statistic")
st.write('On the left you can see which alliances were taken into account when calculating🧮')
st.write("Here you see two graphs - merits and power, which show the change in this data by day.📉")
st.divider()
servers = []
for i in data_alliance_power['name']:
    if i not in servers:
        servers.append(i)

def write_show_servers_alliance(name, server_number):
    serverses = st.sidebar.checkbox(name)
    if serverses:
        st.sidebar.write(pd.Series(server_number).values)


def server(server_all, name, parameter, data_alliance_n):
    data_list = []
    data_date = data_alliance_n['date']
    for i in data_date:
        if i not in data_list:
            data_list.append(i)
    server_list1 = []
    for date in data_list:
        data = data_alliance_n[data_alliance_n['date'] == date]
        stat = 0
        for alliance in server_all:
            stat += data.loc[data['name'] == alliance, parameter].iloc[0]
        server_list1.append((name, stat, date))
    df_server = pd.DataFrame(server_list1, columns=['name', parameter, 'date'])
    return df_server

st.subheader("Power graph for servers", divider=True)
st.caption("Expand to full screen for a better view")
try:
    servers_data_power = [server(server_list[i], server_names[i], 'power', data_alliance_power) for i in
                    range(len(server_list))]
except Exception:
    st.exception(Exception("Something going wrong.🤷‍♂️"))
else:
    df_power = pd.concat(servers_data_power, axis=0)
    st.line_chart(df_power, x='date', y='power', color='name')


st.subheader("Merits graph for servers", divider=True)
st.caption("Expand to full screen for a better view")

try:
    servers_data_merits = [server(server_list[i], server_names[i], 'merits', data_alliance_merits) for i in
                    range(len(server_list))]
except Exception:
    st.exception(Exception("Something going wrong.🤷‍♂️"))
else:
    df_merits = pd.concat(servers_data_merits, axis=0)
    st.line_chart(df_merits, x='date', y='merits', color='name')


for index in range(len(server_list)):
    write_show_servers_alliance(server_names[index], server_list[index])