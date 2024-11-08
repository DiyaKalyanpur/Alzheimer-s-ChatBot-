import sqlite3

def query_database(db_name, query):
    """Execute a SQL query on the database and return results."""
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    field_names = [description[0] for description in cursor.description]
    conn.close()
    return field_names, results

def get_sql_query(prompt):
    """
    Generate SQL queries for the Alzheimer’s dataset based on keywords in the prompt.
    The queries fetch answers related to common Alzheimer’s questions.
    """
    if "symptoms" in prompt.lower():
        return "SELECT Answers FROM qa_pairs WHERE Questions LIKE '%symptoms%'"
    elif "causes" in prompt.lower():
        return "SELECT Answers FROM qa_pairs WHERE Questions LIKE '%causes%'"
    elif "treatment" in prompt.lower():
        return "SELECT Answers FROM qa_pairs WHERE Questions LIKE '%treatment%'"
    elif "risk factors" in prompt.lower():
        return "SELECT Answers FROM qa_pairs WHERE Questions LIKE '%risk factors%'"
    elif "prevention" in prompt.lower():
        return "SELECT Answers FROM qa_pairs WHERE Questions LIKE '%prevention%'"
    elif "stages" in prompt.lower():
        return "SELECT Answers FROM qa_pairs WHERE Questions LIKE '%stages%'"
    elif "statistics" in prompt.lower():
        return "SELECT Answers FROM qa_pairs WHERE Questions LIKE '%statistics%'"
    elif "progression" in prompt.lower():
        return "SELECT Answers FROM qa_pairs WHERE Questions LIKE '%progression%'"
    else:
        return None

