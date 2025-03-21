import psycopg2

DB_NAME = "recipebook"
DB_USER = "your_username"
DB_PASSWORD = "your_password"
DB_HOST = "localhost"
DB_PORT = "5432"

def connect_db():
    try:
        conn = psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT
        )
        return conn
    except Exception as e:
        print("Error connecting to the database: ", e)
        return None
    
def create_tables():
    conn = connect_db()
    if conn is not None:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS recipes (
                id SERIAL PRIMARY KEY,
                name TEXT NOT NULL,
                ingredients TEXT NOT NULL,
                instructions TEXT NOT NULL
            );
        """)
        conn.commit()
        cursor.close()
        conn.close()
    else:
        print("Unable to connect to the database. Tables were not created.")

if __name__ == "__main__":
    create_tables()
