import streamlit as st
from llm_client import get_completion
from sql_runtime import query_database, get_sql_query

# Database details
db_name = 'chatbot_data.db'

# Streamlit interface
st.title("Alzheimer's Disease Chatbot")

# User input for Alzheimer's-related questions
user_input = st.text_input("Ask a question about Alzheimer's disease:")

if st.button("Submit"):
    # Use get_sql_query to generate a SQL query based on user input
    sql_query = get_sql_query(user_input)
    
    if sql_query:
        # Fetch and display results if SQL query generated
        columns, results = query_database(db_name, sql_query)
        if results:
            # Display each answer as a separate line
            for result in results:
                st.write(result[0])  # Display only the answer text
        else:
            st.write("No results found in the database for your query.")
    else:
        # Fallback to LLM if SQL query cannot be generated
        response = get_completion(user_input)
        st.write(response)

