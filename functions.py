import streamlit as st


def find_data(name, data, start_day, end_day, parameter):
    try:
        data_start = data.loc[
            (data["name"] == name) & (data['date'] == start_day),
            parameter].iloc[0]
    except IndexError:
        data_start = 0

    try:
        data_end = data.loc[
            (data["name"] == name) & (data['date'] == end_day),
            parameter].iloc[0]
    except IndexError:
        data_end = 0
    print([data_start, data_end])
    return [data_start, data_end]


def calculator(name, data, start_day, end_day, parameter):

    try:
        start_parameter, end_parameter = find_data(name, data, start_day, end_day, parameter)
    except IndexError:
        st.exception(IndexError("Not enough data to count."))
    except Exception:
        st.exception(Exception("Something going wrong.🤷‍♂️"))
    else:
        start, end = st.columns(2)
        with start:
            st.write(f"power: :green-background[{format(start_parameter,',')}]")
        with end:
            st.write(f"power: :green-background[{format(end_parameter,',')}]")
        st.write(f"Difference is: :blue[{format((end_parameter-start_parameter), ',')}]")

        st.divider()



