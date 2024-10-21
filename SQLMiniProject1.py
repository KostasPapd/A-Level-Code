import sqlite3
from tkinter import *

conn = sqlite3.connect('test.db')

conn.commit()
conn.close()
