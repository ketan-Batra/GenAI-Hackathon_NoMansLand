import openai
import os
import streamlit as st

# Set your OpenAI API key from Azure
openai.api_key = ""
openai.api_base = "https://genai-openai-nomansland.openai.azure.com/"


def generate_response(prompt, model="gpt-4o"):
    """
    Function to send a prompt to Azure OpenAI and get a response
    :param prompt: The query or complaint.
    :param model: The model to use (e.g., gpt-4)
    :return: Generated response from the model.
    """
    st.write("Prompt is : - "+ prompt)
    try:
        response = openai.Completion.create(
            model=model,
            prompt=prompt,
            max_tokens=150,
            temperature=0.7,
            n=1
        )
        print("response",response, response.items)
        return response.choices[0].text.strip()
    except Exception as e:
        print("Error:",e)
        return f"Error: {str(e)}"
