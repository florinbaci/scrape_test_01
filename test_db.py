import sqlite3

conn = sqlite3.connect('test13.db')
c = conn.cursor()


def create_table():
    with conn:
        c.execute("""CREATE TABLE IF NOT EXISTS test_db(
                  Date TEXT, 
                  Hour TEXT, 
                  Money INT,
                  Jockey TEXT,
                  Link TEXT PRIMARY KEY
                  )""")
# use PRIMARY KEY for the unique link that is inserted

date01 = '5 Ian'
hour01 = '10:25:00'
race01 = 'Bordertown'
country01 = 'AUS'
money01 = '205311'
odds01 = '2.09'
jockey01 = 'Texan Windstorm'
link01 = 'https://www.betfair.ro/exchange/plus/horse-racing/market/1.192983291?nodeId=31156627.0250'
won_lost01 = 0
no_of_jockeys01 = 14
winner_jockey = 'Texan Windstorm'


# def insert_race():
#     with conn:
#         c.execute("""INSERT OR REPLACE INTO test_db VALUES (?, ?, ?, ?, ?)""",
#                   (date01, hour01, money01, jockey01, 'Null'))

def insert_race():
    with conn:
        c.execute("""INSERT INTO test_db VALUES (:Date, :Hour, :Money, :Jockey, :Link)""",
                  {'Date': date01,
                   'Hour': hour01,
                   'Money': money01,
                   'Jockey': 'Null',
                   'Link': link01})


# def update_race():
#     with conn:
#         c.execute("""UPDATE test_db SET Jockey = :Jockey
#                      WHERE Link = :Link""",
#                   {'Link': link01,
#                    'Jockey': jockey01})

# create_table()
insert_race()
# update_race()

# def read_from_db():
#     # c.execute('SELECT * FROM races_db WHERE Country = "AUS" AND Against_odds <= 2.04 AND Against_odds >= 2.01 ')
#     # c.execute('SELECT Against_odds, No_of_jockeys FROM races_db WHERE Against_odds >= 2.01')
#     c.execute('SELECT Money')
#     # data = c.fetchall()
#     # print(data)
#     for row in c.fetchall():
#         print(row)


# def create_table():
#     c.execute("CREATE TABLE IF NOT EXISTS races_db(Data TEXT, Hour TEXT, Race TEXT, "
#               "Country TEXT, Money REAL, Against_odds REAL, Jockey TEXT, Link TEXT, "
#               "Win_Lost REAL, No_of_jockeys REAL, Winner_jockey TEXT)")
#
#
# def data_entry():
#     c.execute("INSERT INTO races_db VALUES ('5 Ian', '06:25', 'Bore', 'AUS', '5555', '2.05', 'Joko', 'google.com', '1', '8', 'Koko')")
#     conn.commit()
#     c.close()
#     conn.close()
#
#
# date01 = '5 Ian'
# hour01 = '06:25:00'
# race01 = 'Bordertown'
# country01 = 'AUS'
# money01 = '205311'
# odds01 = '2.02'
# jockey01 = 'Texan Windstorm'
# link01 = 'https://www.betfair.ro/exchange/plus/horse-racing/market/1.192983291?nodeId=31156627.0420'
# won_lost01 = 0
# no_of_jockeys01 = 14
# winner_jockey = 'Texan Windstorm'
#
#
# def dynamic_data_entry():
#     c.execute("INSERT INTO races_db(Data, Hour, Race, "
#               "Country, Money, Against_odds, Jockey, Link, "
#               "Win_Lost, No_of_jockeys, Winner_jockey) "
#               "VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
#               (date01, hour01, race01, country01, money01, odds01, jockey01, link01, won_lost01, no_of_jockeys01, winner_jockey))
#     conn.commit()
#     c.close()
#     conn.close()
#
#
# # create_table()
# # data_entry()
# # dynamic_data_entry()
#
# def read_from_db():
#     # c.execute('SELECT * FROM races_db WHERE Country = "AUS" AND Against_odds <= 2.04 AND Against_odds >= 2.01 ')
#     c.execute('SELECT Against_odds, No_of_jockeys FROM races_db WHERE Against_odds >= 2.01')
#     # data = c.fetchall()
#     # print(data)
#     for row in c.fetchall():
#         print(row)


# read_from_db()
