import sqlite3

DB_NAME = "database.db"

def init_db():
    with sqlite3.connect(DB_NAME) as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS urls (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                original_url TEXT NOT NULL,
                short_url TEXT NOT NULL UNIQUE,
                visit_count INTEGER DEFAULT 0
            )
        ''')

def insert_url(original_url, short_url):
    with sqlite3.connect(DB_NAME) as conn:
        conn.execute('''
            INSERT INTO urls (original_url, short_url)
            VALUES (?, ?)
        ''', (original_url, short_url))

def get_one_url_by_short_url(short_url):
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.execute('''
            SELECT * FROM urls WHERE short_url = ?
        ''', (short_url,))
        return cursor.fetchone()

def update_visit_count(short_url):
    with sqlite3.connect(DB_NAME) as conn:
        conn.execute('''
            UPDATE urls 
            SET visit_count = visit_count + 1 WHERE short_url = ?
        ''', (short_url,))

def get_all_urls():
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.execute('''
            SELECT * FROM urls ORDER BY id DESC
        ''')
        return cursor.fetchall()
    
def delete_url(short_url):
    with sqlite3.connect(DB_NAME) as conn:
        conn.execute('''
            DELETE FROM urls WHERE short_url = ?
        ''', (short_url,))