from openai import OpenAI
import streamlit

#Reading API Key
OpenAPI_key = 'sk-proj-XLF4Mit1oVdCV6l1BXHXT3BlbkFJiiWfKgnCyWzocnNHH7VJ'
client = OpenAI(api_key=OpenAPI_key)


streamlit.title("AI based MCQ Generator")
streamlit.subheader("It will generate five MCQs")


#User Input
prompt = streamlit.text_input("Enter any Topic")

#If button is clicked , generate response
if streamlit.button("Click to generate") == True:
    streamlit.balloons()
    response = client.chat.completions.create(
                model = 'gpt-3.5-turbo' , 
                messages = [
                {'role':'system' , 'content':'''You are a helpful AI assistance, Given a data science topics you always
                    Generate 5 data science questions and answers for MCQ test''' },
                {'role':'user' , 'content': prompt}] 
                )
    
    #Print Responces on app
    streamlit.write(response.choices[0].message.content)