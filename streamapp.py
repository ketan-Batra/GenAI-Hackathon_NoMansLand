import streamlit as st
from knowledgebase import search_knowledge_base
# from integration import generate_response
from azure_api import generate_response
# Function to process complaints
def process_complaint(user_complaint):
    # Step 1: Parse the complaint for relevant keywords (a simple approach here)
    issue_keywords = user_complaint.lower().split()  # Basic keyword extraction
    
    # Step 2: Search the knowledge base (you can refine this logic)
    knowledge_response = search_knowledge_base(issue_keywords)
    # st.write("Generated Response - :"+ knowledge_response)
    
    # Step 3: Generate a response using OpenAI (Azure GPT)
     # User complaint: {user_complaint}. Here are some relevant knowledge articles: {knowledge_response}. Based on this, generate a helpful and friendly response. Please stick to knowledge base and don't use your own knowledge. Identify the abuses and make sure to provide a proper response not to use foul language and always be respectful"
    # Identify the abuses and make sure to provide a proper response not to use foul language and always be respectful. dentify PII(Personal Idenitifiable Information) in the query and make sure to not respond to such queries with the data and just provide a context to connect with us via proper authenticated channel. Make sure response does not lead to harmful consequences either directly or indirectly. Response should not exhibit problematic social biases or share protected or sensitive information. Make sure the responses are on-topic, of proper extensiveness, written in suitable tone"
    prompt = f"""  
    User complaint: {user_complaint}. Here are some relevant knowledge articles: {knowledge_response}. Based on this, generate a helpful and friendly response. 

    Guardrails:
    1. Please stick to the knowledge base and if you want you can use your own knowledge but dont talk about our knowledge base if we dont have information.
    2. Identify any abusive language and provide a proper response not to use foul language and always be respectful.
    3. Identify PII (Personal Identifiable Information) in the query and make sure not to respond with such data. Instead, provide a context to connect with us via a proper authenticated channel.
    4. Ensure the response does not lead to harmful consequences either directly or indirectly.
    5. The response should not exhibit problematic social biases or share protected or sensitive information.
    6. Ensure the responses are on-topic, of proper extensiveness, written in a suitable tone.
    7. Ensure step by step instructions are given and bold the topics along with summarization
    8. If the response is not relevant but in context with bank, please inform the customer to reach out via authenticated channels like the app or web, or call on 1800 100 100, or email
    9. Always ask for feedback and provide a proper closure to the conversation
    10. If the response is not relevant and not in context with bank, please inform the we do not have the information and provide a proper closure to the conversation and dont talk about knowledge base
    If no relevant knowledge base article is found, please inform the customer to reach out via authenticated channels like the app or web, or call on 1800 100 100, or email bank@bank.com.
    """

    generated_response = generate_response(prompt)
    
    return generated_response

# Streamlit UI
def main():
    st.set_page_config(page_title="BBuddy Portal", layout="wide")
    
    # st.title("BBuddy Social Media Handling System")

    st.markdown("""
    <style>
    .main {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 10px;
    }
    .header {
        text-align: center;
        color: #4CAF50;
    }
    .subheader {
        text-align: center;
        color: #555;
    }
    .title {
        text-align: center;
        font-size: 2em;
        color: #4CAF50;
    }           
    </style>
    """, unsafe_allow_html=True)

    st.markdown("<h1 class='title'>BBuddy Social Media Handling System</h1>", unsafe_allow_html=True)

    st.markdown("<h3 class='subheader'>We are here to help you with your complaints</h3>", unsafe_allow_html=True)

# Layout with two columns: Left for complaint input, Right for response display
    col1, col2 = st.columns([1, 1])

    with col1:
        st.header("Share Your Queries/Complaints")
        # User input for the complaint
        user_complaint = st.text_area("Enter your query:")

        # Submit button
        submit_button = st.button("Submit Query")

        if submit_button and user_complaint:
            progress_bar = st.progress(0)
            status_text = st.empty()
            status_text.text("Processing your query... Please wait.")
            
            # Update progress bar
            for percent_complete in range(100):
                progress_bar.progress(percent_complete + 1)
            
            # Process complaint and generate response
            response = process_complaint(user_complaint)
            st.session_state.response = response
            
            # Hide progress bar
            progress_bar.empty()
            status_text.text("Request processed. Please see the generated response.")
        elif submit_button and not user_complaint:
            st.warning("Please write a query before submitting.")
            st.session_state.response = ''
    
    # Column 2: Response output
    with col2:
        st.markdown("<h2 style='text-align: center;'>Generated Response</h2>", unsafe_allow_html=True)
        # st.header("Generated Response")

        if 'response' in st.session_state:
            st.write(st.session_state.response)
        else:
            st.write("No complaint posted yet. Please submit a query to see the response.")
    
            
# Run the Streamlit app
if __name__ == "__main__":
    main()
