import sqlite3

DB_NAME = "api_console.db"

def init_db():
    """Create the database and table if they don't exist."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS request_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            url TEXT NOT NULL,
            method TEXT NOT NULL,
            request_body TEXT,
            status_code INTEGER,
            response_body TEXT,
            response_time REAL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

def log_request(url, method, request_body, status_code, response_body, response_time):
    """Save a request and its response to the database."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO request_logs (url, method, request_body, status_code, response_body, response_time)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (url, method, request_body, status_code, response_body, response_time))
    conn.commit()
    conn.close()

def get_all_logs():
    """Fetch all saved logs from the database, newest first."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM request_logs ORDER BY timestamp DESC')
    rows = cursor.fetchall()
    conn.close()
    return rows

def delete_all_logs():
    """Delete all logs from the database."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('DELETE FROM request_logs')
    conn.commit()
    conn.close()