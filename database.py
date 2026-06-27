import sqlite3

DATABASE_NAME = "data/business.db"


def connect():
    """Connect to the SQLite database."""
    return sqlite3.connect(DATABASE_NAME)


def create_tables():
    """Create all tables needed for the system."""

    conn = connect()
    cursor = conn.cursor()

    # Trips Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS trips (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        customer_name TEXT NOT NULL,
        phone TEXT,
        pickup TEXT NOT NULL,
        destination TEXT NOT NULL,
        vehicle TEXT NOT NULL,
        driver TEXT,
        fare REAL NOT NULL,
        fuel_cost REAL DEFAULT 0,
        payment_method TEXT,
        status TEXT DEFAULT 'Completed',
        trip_date TEXT
    )
    """)

    conn.commit()
    conn.close()

    print("✅ Database is ready.")
