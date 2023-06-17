#A Summarizers App  06/06/2023

# Importing the dependencies
import openai
import streamlit as st

#Set the GPT-3 API Key
#openai.api_key = st.secrets['pass']
openai.api_key = "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"

st.header("Summarizer App Using OpenAI + Streamlit")

article_text = st.text_area("Enter your scientific texts to summarize")
output_size = st.radio(label = "What kind of output do you want?", 
                    options= ["To-The-Point", "Concise", "Detailed"])

if output_size == "To-The-Point":
    out_token = 50
elif output_size == "Concise":
    out_token = 128
else:
    out_token = 516
    
temp = st.slider("temperature", 0.0, 1.0, 0.5)

if len(article_text) > 100 :
    if st.button("Generate Summary"):
        # Use GPT-3 to generate summary of the article
        response = openai.Completion.create(
            engine = "text-davinci-003",
            prompt = "Please  summarize this scientific article for me in a few sentences : " + article_text,
            #max_token = out_token,
            temperature = temp
        )
        
        # Print the summary generated
        res = response["choices"][0]["text"]
        st.success(res)
        st.download_button("Download Results", res)    
else :
    st.warning("Not enough words to summarize!")
    
    
#Start the program with "streamlit run Test_how_to_use_openai.py"