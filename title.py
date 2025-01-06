import streamlit as st
from load_data import first_date, last_date
# st.set_page_config(
#     page_title="AC~DC",
#     page_icon="🦀",
# )
# st.sidebar.markdown("# 📑Title")


st.write("# AC-DC")
st.write(f":blue-background[Last update: {last_date}]")
st.divider()
st.write('Collected statistics on alliance players and some general statistics on other alliances💹.')
st.write("On the left side there are tabs where you can choose what data you want to view.🥢")
st.write("""
This project was developed for educational👨‍🎓  purposes and is in the testing stage, so there may be errors and bugs.🐛 
""")
st.write("Please write to Crabik about any errors and shortcomings you find (better with screenshots).🦀")

st.write("It is important to note that since I am collecting data via screen scanning, there may be errors in the names. So I apologize if anyone's name is misspelled😀")
st.write("To update the data🦀, I need to perform some manipulations, so the last update date may be a few days ago. "
         f"The first day i start calculate units killed, dead and heal is {first_date} ")

st.divider()
st.markdown(":blue[All graphs can be expanded to full screen.]📜️")
st.divider()



