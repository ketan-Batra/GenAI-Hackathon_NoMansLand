
import os  
from openai import AzureOpenAI  

endpoint = os.getenv("ENDPOINT_URL", "https://genai-openai-nomansland.openai.azure.com/")  
deployment = os.getenv("DEPLOYMENT_NAME", "gpt-4o")  
search_endpoint = os.getenv("SEARCH_ENDPOINT", "https://genai-datasearch-rekyc-search-service.search.windows.net")  
search_key = os.getenv("SEARCH_KEY", "put your Azure AI Search admin key here")  
search_index = os.getenv("SEARCH_INDEX_NAME", "primarytransaction")  
subscription_key = os.getenv("AZURE_OPENAI_API_KEY", "")  

# Initialize Azure OpenAI client with key-based authentication
client = AzureOpenAI(  
    azure_endpoint=endpoint,  
    api_key=subscription_key,  
    api_version="2024-05-01-preview",  
)  



def generate_response(prompt, model="gpt-4o"):
    chat_prompt = [
    {
        "role": "system",
        "content": prompt
    }
    ]  
    try:
        # Include speech result if speech is enabled  
        speech_result = chat_prompt  

        # Generate the completion  
        completion = client.chat.completions.create(  
            model=deployment,  
            messages=speech_result,  
            # past_messages=10,  
            max_tokens=800,  
            temperature=0.7,  
            top_p=0.95,  
            frequency_penalty=0,  
            presence_penalty=0,  
            stop=None,  
            stream=False  
        )
        print("response",completion.to_json())
        return completion.choices[0].message.content
    except Exception as e:
        print("Error",e)