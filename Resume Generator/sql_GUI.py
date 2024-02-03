import os
import openai
import pandas as pd
from io import StringIO
import sqlite3
import re
import tkinter as tk
from tkinter import filedialog, Label, Text, Button

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

# Function to get AI response
def get_ai_response(user_input):
    openai.api_key = os.getenv('OPENAI_KEY')
    completion = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant for writing a SQL Query of given dataset and default table name is data"},
            {"role": "user", "content": user_input}
        ]
    )
    response_text = completion.choices[0].message.content
    return response_text

# Function to handle query and display result
def handle_query():
    user_input = text.get("1.0",'end-1c')
    user_query = user_input.strip()
    
    if user_query:
        AiQuery = get_ai_response(csv_data + "\n\n\n" + user_query)
        AiQuerytry = AiQuery
        sql_query_match = re.search(r'SELECT .*?;', AiQuery, re.DOTALL)
        if sql_query_match:
            AiQuery = sql_query_match.group().strip()
            result_text.config(state='normal')
            result_text.delete(1.0, "end")
            result_text.insert(tk.END, f"\n-----------------------\n{AiQuery}\n-----------------------\n\n")
            result_text.config(state='disabled')

            try:
                df = pd.read_csv(StringIO(csv_data))
                conn = sqlite3.connect(':memory:')
                df.to_sql('data', conn, index=False, if_exists='replace')
                result = pd.read_sql_query(AiQuery, conn)
                result_text.config(state='normal')
                result_text.insert(tk.END, f"{result}\n")
                result_text.config(state='disabled')
                conn.close()
            except Exception as e:
                result_text.config(state='normal')
                result_text.insert(tk.END, f"Error: {e}\n")
                result_text.config(state='disabled')

        else:
            result_text.config(state='normal')
            result_text.insert(tk.END, f"{AiQuerytry}\nSQL query not found in the provided text.\n")
            result_text.config(state='disabled')


# Function to open file dialog and set CSV data
def open_file_dialog():
    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if file_path:
        global csv_data
        with open(file_path, 'r') as file:
            csv_data = file.read()
        file_label.config(text=f"File: {os.path.basename(file_path)}")


# GUI Setup
root = tk.Tk()
root.title("SQL Query Assistant")

# Open File Button
open_file_button = Button(root, text="Open CSV File", command=open_file_dialog)
open_file_button.pack(pady=10)

# File Label
file_label = Label(root, text="")
file_label.pack()

# Query Input Textbox
text = Text(root, height=10, width=50)
text.pack(pady=10)

# Query Button
query_button = Button(root, text="Run Query", command=handle_query)
query_button.pack()

# Result Textbox
result_text = Text(root, height=20, width=80)
result_text.pack(pady=10)
result_text.config(state='disabled')

# Run GUI
root.mainloop()
