import sqlite3

#Connect to a (new) database
conn = sqlite3.connect("D:\\Prospect_Sim\\DB Data\\test.db")

#Close Connection
conn.close()