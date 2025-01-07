import streamlit as st
import pandas as pd
from load_data import data_alliance_power, data_alliance_merits, server_names, server_list, last_date, list_dates
from functions import calculator

st.sidebar.markdown("# Server statistic")
st.title(" Server statistic")
st.write('On the left you can select a server to open the calculator for it.🧮')
st.write("Here you see two graphs - merits and power, which show the change in this data by day.📉")
st.divider()


def create_server_data(server_alliances, server_name, parameter, data_alliance_parameter):
    data_list = []
    data_date = data_alliance_parameter['date']
    for i in data_date:
        if i not in data_list:
            data_list.append(i)
    server_list1 = []
    for date in data_list:
        data = data_alliance_parameter[data_alliance_parameter['date'] == date]
        suma_parameters = 0
        for alliance in server_alliances:
            suma_parameters += data.loc[data['name'] == alliance, parameter].iloc[0]
        server_list1.append((server_name, suma_parameters, date))
    df_server = pd.DataFrame(server_list1, columns=['name', parameter, 'date'])
    return df_server

def create_server_dataframe(list_servers, names_servers, parameter, data):
    list_data = []
    for index in range(len(names_servers)):
        list_data.append(create_server_data(list_servers[index], names_servers[index], parameter, data))
    dataframe_server = pd.concat(list_data, axis=0)
    return dataframe_server


def show_alliances_and_calculator(name, server_number, data, parameter):
    show_alliance_servers = st.sidebar.toggle(name)
    if show_alliance_servers:
        st.sidebar.write(pd.Series(server_number).values)
        start, end = st.columns(2)
        with start:
            start_day = st.selectbox(f"{name}. Chose start date: ", list_dates)
        with end:
            end_day = st.selectbox(f"{name}. Chose end date: ", list_dates)
        calculator(name, data, start_day, end_day, parameter)


st.subheader("Server calculator", divider=True)
st.caption('You can select two dates and the calculator will show the difference in how much the server lost or gained during this period.')
servers_data = None
choose_parameter = st.selectbox("Chose parameter. Chose server in sidebar.", ["power", "merits"])
if choose_parameter == "power":
    servers_data = create_server_dataframe(server_list, server_names, choose_parameter, data_alliance_power)
elif choose_parameter == "merits":
    servers_data = create_server_dataframe(server_list, server_names, choose_parameter, data_alliance_merits)

for index in range(len(server_list)):
    show_alliances_and_calculator(server_names[index], server_list[index], servers_data, choose_parameter)


# def chosen_server_data(server_names, chosen_server, server_list, parameter, data_alliance):
#     chosen_servers_data_power = []
#     for index in range(len(server_names)):
#         if server_names[index] in chosen_server:
#             chosen_servers_data_power.append(create_server_data(server_list[index], server_names[index], parameter, data_alliance))
#     return chosen_servers_data_power


st.subheader("Power graph for servers", divider=True)
st.caption(f"Expand to full screen for a better view. Update date:{last_date}")
chosen_server = st.multiselect(label="Chose servers", options =server_names, default=server_names[:3])
st.divider()
try:
    # chosen_servers_data_power = chosen_server_data(server_names, chosen_server, server_list, 'power', data_alliance_power)
    chosen_servers_data_power = []
    for index in range(len(server_names)):
        if server_names[index] in chosen_server:
            chosen_servers_data_power.append(create_server_data(server_list[index], server_names[index], 'power', data_alliance_power))
except Exception:
    st.exception(Exception("Something going wrong.🤷‍♂️"))
else:
    try:
        df_power = pd.concat(chosen_servers_data_power, axis=0)
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
            servers_data_merits.append(create_server_data(server_list[index], server_names[index], 'merits', data_alliance_merits))
except Exception:
    st.exception(Exception("Something going wrong.🤷‍♂️"))
else:
    try:
        df_merits = pd.concat(servers_data_merits, axis=0)
    except ValueError:
        st.exception(ValueError("No servers chosen"))
    else:
        st.line_chart(df_merits, x='date', y='merits', color='name')



