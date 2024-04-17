from openai import OpenAI
import streamlit
import json

streamlit.title("An AI Code Reviewer")



#User input
code = streamlit.text_area("Enter python code here")

if streamlit.button("Click to generate"):
    OpenAPI_key = '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'
    client = OpenAI(api_key=OpenAPI_key)

    response = client.chat.completions.create(
                      model="gpt-3.5-turbo",
                      messages=[
                        {"role": "system", "content": """You are a teaching assistant working with an edtech for a Data Science course. 
                                        Your job here is to help students resolve there doubts regarding specific data science topics.
                                        You are know to be polite and helpful AI bot. 
                                        If the doubt is not relevant to data science you can politely ask the user another doubt.
                                        """},
                        {"role": "user", "content": f"Fix and explain the bug in the following python code: {code}"}
                      ],
                      temperature=0.5
                )
    
    #review = json.load(response.choices[0].message.content)

    streamlit.write(response.choices[0].message.content)
    #streamlit.header("Code Review")
    #streamlit.subheader("Bugs Report")
    #streamlit.write(review['Bugs'])
    #streamlit.subheader("Fixed Code")
    #streamlit.code(review['Code'])
