import sqlite3
import pandas as pd

def load_csv_to_sqlite(csv_file, db_name, table_name):
    # Load CSV file into a DataFrame without the 'errors' parameter
    data = pd.read_csv(csv_file, encoding="utf-8")
    
    # Remove index column if it exists
    if 'Unnamed: 0' in data.columns:
        data = data.drop(columns=['Unnamed: 0'])
    
    # Fill missing answers with placeholder text
    data = data.assign(Answers=data['Answers'].fillna("Answer not available."))

    
    # Connect to SQLite database
    conn = sqlite3.connect(db_name)
    
    # Load data into SQLite as a table
    data.to_sql(table_name, conn, if_exists='replace', index=False)
    print(f"Data loaded into '{table_name}' table in '{db_name}' database.")
    
    # Close connection
    conn.close()

# Load data from CSV into SQLite database
load_csv_to_sqlite('/Users/diyakalyanpur/Downloads/LLM  project/full_Chat_data.csv', 'chatbot_data.db', 'qa_pairs')


