import json
import sqlite3 as sq


class DatabaseManger:
    def __init__(self):
        self.con = sq.connect('main.db')
        self.cur = self.con.cursor()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            self.con.commit()
        self.con.close()

    def create_database(self):
        self.cur.executescript(
            """
            DROP TABLE IF EXISTS days_info;
            CREATE TABLE days_info (
                date_key TEXT PRIMARY KEY,
                windows_json TEXT,
                windows_for_room_json TEXT,
                api_check TEXT
            )
            """
        )

    def insert_date(self, date_key, windows_json, windows_for_room_json, api_check):
        self.cur.execute(
            """
            INSERT INTO days_info
            VALUES (?, ?, ?, ?)
            """, [date_key, windows_json, windows_for_room_json, api_check]
        )

    def select_date(self, date_key):
        self.cur.execute(
            """
            SELECT windows_json, windows_for_room_json, api_check
            FROM days_info
            WHERE date_key = ?
            """, [date_key]
        )
        windows_json, windows_for_room_json, api_check = self.cur.fetchone()

        return json.loads(windows_json), json.loads(windows_for_room_json), api_check
