knowledge_base = {
    # "laptop screen damage": "To fix a damaged laptop screen, first check if the laptop is still under warranty. If so, contact your manufacturer for a replacement. Otherwise, you can consider using online tutorials or visiting a local repair shop. In the event of water damage, turn off the laptop immediately and dry it out.",
    # "laptop overheating": "If your laptop is overheating, try cleaning the fans or ensuring that the air vents are unobstructed. Additionally, consider using a cooling pad. You may also need to check if any software or background processes are consuming too much CPU power.",
    # "Battery functioning": "Ensure that your charger and power outlet are functioning. If the laptop still doesn't charge, the issue may be with the battery or charging port, and you may need a replacement part.",
    "Barclays credit card": "you can try to check credit card status by calling us on 1800 180 100",
    "barclays customer care": "You can try to calling us on 1800 180 101 for the customer card agents",
    "barcalys chatbot": "If you need any help with barclays bank, our chatbot is here to help you with most of the queries like direct debit, how to check transaction on app",
    "direct debit": '''A direct debit or direct withdrawal is a financial transaction in which one organisation withdraws funds from a payer's bank account.[1] Formally, the organisation that calls for the funds ("the payee") instructs their bank to collect (i.e., debit) an amount directly from another's ("the payer's") bank account designated by the payer and pay those funds into a bank account designated by the payee. Before the payer's banker will allow the transaction to take place, the payer must have advised the bank that they have authorized the payee to directly draw the funds. It is also called pre-authorized debit (PAD) or pre-authorized payment (PAP). After the authorities are set up, the direct debit transactions are usually processed electronically.''',
    "Job Opportunities": "We are hiring for various roles. Please visit our careers page ban.careers@bank.com to view the available positions and apply online.",
    "Set up direct debit": """You will need to contact the company or organisation you want to pay - this can be done over the phone, online or by post - they will be able to set up the direct debit for you. To arrange a new direct debit, you will need to sign a direct debit mandate which is provided to you by the organisation you wish to pay and return it back to them. The organisation will then set up the direct debit mandate with us.
            The information you'll need to provide to set up a direct debit will include:
                Your name and address
                The name and address of your bank
                Your bank account number
                Your sort code
                The name(s) on the bank account
                Newly set up direct debits will only show on Online Banking once the first payment has been taken from your account.

            After the first payment has been taken it will display on your statement, and you will be able to view it along side any other existing direct debits.""",
    "Cancel direct debit via app": """Log in to your mobile banking app
                                Tap ‘Payments’ on the bottom of the home screen
                                Make sure the account displayed is set to the account where the direct debit is paid from. You can swipe to change accounts or tap 'Change account'
                                Tap 'Regular payments' then 'Direct debits'
                                Select the direct debit you want cancelled. You will see the detail of the direct debit, and the option to cancel the direct debit will appear at the bottom of this screen""",
    "Not helpful worst service no response": "We are sorry to hear that you are not satisfied with our service. Please provide more details about your issue on our email bank@bank.com so that we can assist you better.",
    "Link is not working": """Thank you for bringing this to our attention. I apologize for any inconvenience you are experiencing with the link.

To assist you further, I recommend trying the following troubleshooting steps:

Clear your browser's cache and cookies, and then try opening the link again.
Use a different browser (e.g., Chrome, Firefox, Edge) to see if the issue persists.
Ensure that your internet connection is stable and try refreshing the page.
If the problem continues, please let me know, and I will escalate the matter to our technical support team to investigate further. In the meantime, if you need immediate assistance with any banking services, please feel free to reach out directly.

Thank you for your understanding, and I look forward to resolving this issue for you as quickly as possible.""",
    "Transaction amount transfer pending" : """if you need assistance with any urgent banking matters, please do not hesitate to contact me directly. I will personally follow up on your case and keep you updated with any progress.

Again, I apologize for any inconvenience this may have caused, and I truly appreciate your patience as we work to resolve this issue."""
}

def search_knowledge_base(issue_keywords):
    """
    Function to search the knowledge base for relevant articles based on issue keywords.
    :param issue_keywords: The list of keywords extracted from the user complaint.
    :return: String containing relevant knowledge articles.
    """
    relevant_articles = []
    for keyword, article in knowledge_base.items():
        if any(kw in keyword for kw in issue_keywords):
            relevant_articles.append(article)
    return "\n".join(relevant_articles) if relevant_articles else "No relevant articles found."
