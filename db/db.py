import duckdb
from models import Process

# Create a new DuckDB connection
dbconn = duckdb.connect(config={'database':':memory', 'duckdb_read_only': 'false', threaded: 'true', 'threads': 2})
print("DuckDB connection created successfully")
print("DuckDB version:", conn.execute("SELECT duckdb_version()").fetchone()[0])
print("DuckDB connection info:", conn.info())

# Function to create the processes table
def _create_process_table():
    conn.execute("CREATE TABLE IF NOT EXISTS processes (process_id VARCHAR PRIMARY KEY, process_status VARCHAR, process_results VARCHAR)")
    conn.commit()

# Function to create the process_items table
def _create_process_items_table():
    dbconn.execute("CREATE TABLE IF NOT EXISTS process_items (process_id VARCHAR, source_id VARCHAR PRIMARY KEY, source_type VARCHAR, \
        source_uri VARCHAR, source_name VARCHAR, convert_to VARCHAR, destination_uri VARCHAR, conversion_result VARCHAR, \
            FOREIGN KEY (process_id) REFERENCES processes(process_id) ON DELETE CASCADE)")
    dbconn.commit()

# Function to create all necessary tables
def create_tables(dbconn: duckdb.DuckDBPyConnection):
    _create_process_table()
    _create_process_items_table()

# Function to get the DuckDB connection
def get_connection():
    # Create a new DuckDB connection
    if dbconn is None:
        dbconn = duckdb.connect(config={'database':':memory', 'duckdb_read_only': 'false', threaded: 'true', 'threads': 2})
    return dbconn

# Initialize the database and create tables
dbconn = get_connection()
create_tables(dbconn)




