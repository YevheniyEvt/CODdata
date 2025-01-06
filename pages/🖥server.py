import streamlit as st
import pandas as pd
from load_data import data_alliance_power, data_alliance_merits, server_names, server_list, last_date

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
    show_alliance_servers = st.sidebar.toggle(name)
    if show_alliance_servers:
        st.sidebar.write(pd.Series(server_number).values)


def server(server_all, name, parameter, data_alliance_parameter):
    data_list = []
    data_date = data_alliance_parameter['date']
    for i in data_date:
        if i not in data_list:
            data_list.append(i)
    server_list1 = []
    for date in data_list:
        data = data_alliance_parameter[data_alliance_parameter['date'] == date]
        stat = 0
        for alliance in server_all:
            stat += data.loc[data['name'] == alliance, parameter].iloc[0]
        server_list1.append((name, stat, date))
    df_server = pd.DataFrame(server_list1, columns=['name', parameter, 'date'])
    return df_server

st.subheader("Power graph for servers", divider=True)
st.caption(f"Expand to full screen for a better view. Update date:{last_date}")
chosen_server = st.multiselect(label="Chose servers", options =server_names, default=server_names[:3])
st.divider()

try:
    servers_data_power = []
    for index in range(len(server_list)):
        if server_names[index] in chosen_server:
            servers_data_power.append(server(server_list[index], server_names[index], 'power', data_alliance_power))
except Exception:
    st.exception(Exception("Something going wrong.🤷‍♂️"))
else:
    try:
        df_power = pd.concat(servers_data_power, axis=0)
    except ValueError:
        st.exception(ValueError("No servers chosen"))
    else:
        st.line_chart(df_power, x='date', y='power', color='name')


st.subheader("Merits graph for servers", divider=True)
st.caption(f"Expand to full screen for a better view. Update date:{last_date}")
chosen_server = st.multiselect(label="Chose servers", options =server_names, default=server_names[:1])
st.divider()
try:
    servers_data_merits = []
    for index in range(len(server_list)):
        if server_names[index] in chosen_server:
            servers_data_merits.append(server(server_list[index], server_names[index], 'merits', data_alliance_merits))
except Exception:
    st.exception(Exception("Something going wrong.🤷‍♂️"))
else:
    try:
        df_merits = pd.concat(servers_data_merits, axis=0)
    except ValueError:
        st.exception(ValueError("No servers chosen"))
    else:
        st.line_chart(df_merits, x='date', y='merits', color='name')


for index in range(len(server_list)):
    write_show_servers_alliance(server_names[index], server_list[index])