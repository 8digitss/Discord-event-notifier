import sqlite3
from datetime import datetime, timedelta

conn = sqlite3.connect('events.db', detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
c = conn.cursor()
c.execute("""
CREATE TABLE IF NOT EXISTS events (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    time TEXT NOT NULL,
    description TEXT
)
""")
conn.commit()

def add_event(title, time, description):
    with conn:
        c.execute("INSERT INTO events (title, time, description) VALUES (?, ?, ?)", (title, time, description))

def list_events():
    c.execute("SELECT * FROM events ORDER BY time")
    return c.fetchall()

def get_upcoming_events():
    now = datetime.now().isoformat()
    upcoming = (datetime.now() + timedelta(minutes=10)).isoformat()
    c.execute("SELECT * FROM events WHERE time BETWEEN ? AND ?", (now, upcoming))
    return c.fetchall()
