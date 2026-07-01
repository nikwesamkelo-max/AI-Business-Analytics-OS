import sqlite3

DATABASE_NAME = "data/business.db"


def connect():

    conn = sqlite3.connect(DATABASE_NAME)

    conn.row_factory = sqlite3.Row

    return conn


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
    
def add_trip(customer_name, phone, pickup, destination,
             vehicle, driver, fare, fuel_cost,
             payment_method, trip_date):

    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO trips (
        customer_name,
        phone,
        pickup,
        destination,
        vehicle,
        driver,
        fare,
        fuel_cost,
        payment_method,
        trip_date
    )
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        customer_name,
        phone,
        pickup,
        destination,
        vehicle,
        driver,
        fare,
        fuel_cost,
        payment_method,
        trip_date
    ))

    conn.commit()
    conn.close()

    print("✅ Trip added successfully!")


def view_trips():

    conn = connect()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM trips")

    trips = cursor.fetchall()

    conn.close()

    return trips
    
def search_customer(customer_name):

    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM trips
        WHERE customer_name LIKE ?
    """, (f"%{customer_name}%",))

    results = cursor.fetchall()

    conn.close()

    return results

def update_trip_status(trip_id, new_status):

    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE trips
        SET status = ?
        WHERE id = ?
    """, (new_status, trip_id))

    conn.commit()
    conn.close()

    print("✅ Trip status updated successfully.")

def delete_customer(customer_id):

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM customers WHERE customer_id = ?",
        (customer_id,)
    )

    conn.commit()
    conn.close()

    print("Customer deleted successfully.")

def get_total_trips():

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM trips")
    total = cursor.fetchone()[0]

    conn.close()
    return total

def get_completed_trips():

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT COUNT(*) 
        FROM trips 
        WHERE status = 'Completed'
    """)

    total = cursor.fetchone()[0]
    conn.close()
    return total

def get_active_trips():

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT COUNT(*) 
        FROM trips 
        WHERE status = 'In Progress'
    """)

    total = cursor.fetchone()[0]
    conn.close()
    return total

def get_cancelled_trips():

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT COUNT(*) 
        FROM trips 
        WHERE status = 'Cancelled'
    """)

    total = cursor.fetchone()[0]
    conn.close()
    return total

def get_cancellation_rate():

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM trips")
    total_trips = cursor.fetchone()[0]

    cursor.execute("""
        SELECT COUNT(*) 
        FROM trips 
        WHERE status = 'Cancelled'
    """)
    cancelled = cursor.fetchone()[0]

    conn.close()

    if total_trips == 0:
        return 0

    return (cancelled / total_trips) * 100

def get_total_revenue():

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT SUM(fare)
        FROM trips
        WHERE status = 'Completed'
    """)

    total = cursor.fetchone()[0]
    conn.close()

    if total is None:
        return 0

    return total
