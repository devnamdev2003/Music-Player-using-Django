import os
import openai
import pandas as pd
from io import StringIO
import sqlite3
import re
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
csv_data = """
Roll_Number,Name,SGPA,CGPA
0967CS201001,ABHYUDAYSHARMA,7.79,8.52
0967CS201002,ADARSHSHARMA,6.67,7.49
0967CS201003,ADITYAPANDEY,6.33,7.54
0967CS201004,ADITYATRIPATHI,7.33,8.42
0967CS201005,AESHKUMARSEN,7.08,7.65
0967CS201006,AJAYDHAKAD,3.63,5.73
0967CS201007,AKASHKUSHWAH,6.50,7.49
0967CS201008,AMANDHAKAD,6.96,8.06
0967CS201009,AMANGOYAL,6.88,8.21
0967CS201010,AMANSHARMA,6.83,8.08
0967CS201011,ANAMIKAMUDOTIYA,7.63,8.35
0967CS201012,ANCHALMAHRA,6.58,6.89
0967CS201013,ANIRUDHSINGHBHADAURIA,8.54,8.73
0967CS201014,ANKITLILHORE,7.17,7.89
0967CS201015,ANUBHAVPANDEY,6.92,8.14
0967CS201016,AYUSHKHAN,7.25,8.35
0967CS201017,AYUSHKUSHWAH,7.79,7.99
0967CS201018,DEVKUMARSETH,5.79,7.81
0967CS201019,DEVNAMDEV,8.21,8.80
0967CS201020,DEVESHTIWARI,7.33,8.31
"""


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


userQuery = input("Enter Query: ")
user_input = csv_data + "\n\n\n" + userQuery
AiQuery = get_ai_response(user_input)
AiQuerytry = AiQuery
sql_query_match = re.search(r'SELECT .*?;', AiQuery, re.DOTALL)
if sql_query_match:
    AiQuery = sql_query_match.group().strip()
    print("\n-----------------------\n")
    print(AiQuery)
    print("\n-----------------------\n")
else:
    print(AiQuerytry)
    print("SQL query not found in the provided text.")

try:
    df = pd.read_csv(StringIO(csv_data))
    conn = sqlite3.connect(':memory:')
    df.to_sql('data', conn, index=False, if_exists='replace')
    result = pd.read_sql_query(AiQuery, conn)
    print(result)
    conn.close()
except Exception:
    print('Error')
