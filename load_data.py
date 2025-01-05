import datetime
import streamlit as st
import pandas as pd
import sqlalchemy
import psycopg2
import psycopg
from streamlit.connections import SQLConnection
col = ["id", "name", "alliance", "power", "merits", "killed", "dead", "healed", "date"]

# def load_data(_table):
    # st.cache_data.clear()
    # conn = st.connection(name="my_database", ttl=5)
    # query = f"SELECT * FROM {_table}"
    # st.write("Виконується запит:", query)
    # data = conn.query(query)
    # return data

def load_data(table):
    st.cache_data.clear()
    conn = st.connection(name ="my_database", ttl=3)
    data = conn.query(f"SELECT * FROM {table}")
    return data
#     # conn = psycopg.connect(
    #     user='genya',
    #     password='H1TdkjbyQR2g',
    #     host='ep-round-feather-a2r7rxys.eu-central-1.pg.koyeb.app',
    #     port='5432',
    #     dbname='codplayers1'
    # )
    # cur = conn.cursor()
    # data = cur.execute(f"SELECT * FROM {table}")
    # return data


@st.cache_data(ttl=5)
def load_player_statistic():
    player_statistic = load_data("players")
    data_players_statistic_f = pd.DataFrame(player_statistic, columns=col)
    return data_players_statistic_f
data_players_statistic = load_player_statistic()


@st.cache_data(ttl=5)
def load_info_player():
    info_player = load_data("name_id")
    data_name_id_f = pd.DataFrame(info_player, columns=['id', 'name'])
    return data_name_id_f
data_name_id = load_info_player()


@st.cache_data(ttl=5)
def load_alliance_power():
    alliance_power = load_data('all_power')
    data_alliance_power_f = pd.DataFrame(alliance_power, columns=['name', 'power', 'date'])
    print("load_data")
    return data_alliance_power_f
data_alliance_power = load_alliance_power()

@st.cache_data(ttl=5)
def load_alliance_merits():
    alliance_merits = load_data('all_merits')
    data_alliance_merits_f = pd.DataFrame(alliance_merits, columns=['name', 'merits', 'date'])
    return data_alliance_merits_f
data_alliance_merits = load_alliance_merits()


last_date = data_players_statistic['date'].max()
first_date = data_players_statistic['date'].min()

server_220 = ['[D~C]Demons of Chaos', '[A~C]Angels Of Chaos']
server_113 = ['[CMAR]Chill Martians', '[CMA1] Chill Martians 1', '[CMA2] Chill Martians 2' ]
server_110 = ['[RoA]Ronin Aegis', '[RoS]Ronin Storm', '[RoV]Ronin Vanguard', '[RoK]Ronin Kingsguard', '[RoG]Ronin Guard']
server_171 = ['[ASC~]Ascendants', '[ASF~]Ascendants Farm', '[She~]Ascendants Shell']

server_11 = ['-EXILE-', '[EvM]Valiant Maidens', '[XNXX]xExileFramerx', '[Ex-F]Exile Farmers']
server_186 = ['[ERA]Eternal Rage Army', '[xERA]Chimera']
server_244 = ['[TG:B] Together B Team', '[TG:A] Together ATeam', '[TG:&]Together We Strong', '[TG:C] Together C Team',
            ]
server_211 = ['[K211]NEXUS', '[DvF]Divine Future', '[211F]K211 Farm']

server_list = [
    server_220,
    server_113,
    server_110,
    server_171,
    server_11,
    server_186,
    server_244,
    server_211
]

server_names = [
    '220 AC-DC',
    '113 CMAR',
    '110 ROA',
    '171 ASK',
    '11 EXILE',
    '186 ERA',
    '244 TG',
    '211 K+DvF'
]
