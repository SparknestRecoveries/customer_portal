import streamlit as st
from datetime import datetime
import os
from google.cloud import firestore

# Initialize Firestore
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/Users/olaoye/Desktop/Projects/sales_bot/adaditech-7de9347adf7b.json'
db = firestore.Client()

# External CSS to enhance visuals and improve dark mode compatibility
def set_css():
    st.markdown("""
    <style>
    .main {
        background-color: var(--background);
        padding: 20px;
    }
    .header {
        text-align: center;
        color: var(--header-color);
        font-size: 48px;
        font-weight: bold;
        margin-bottom: 20px;
        font-family: 'Arial', sans-serif;
    }
    .sub-header {
        text-align: center;
        color: var(--sub-header-color);
        font-size: 18px;
        margin-bottom: 20px;
        font-family: 'Arial', sans-serif;
    }
    .card {
        background-color: var(--card-bg);
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 15px;
        box-shadow: 0px 6px 12px rgba(0, 0, 0, 0.1);
        color: var(--card-text);
    }
    .highlight {
        background-color: #ffcc00;
        color: black;
        padding: 10px;
        text-align: center;
        border-radius: 5px;
        margin-bottom: 20px;
        font-weight: bold;
    }
    .button-link {
        text-align: center;
        margin: 20px 0;
    }
    .button-link a {
        background-color: #009688;
        color: white;
        padding: 10px 20px;
        text-decoration: none;
        font-weight: bold;
        border-radius: 5px;
    }
    .button-link a:hover {
        background-color: #00796b;
    }
    @media (prefers-color-scheme: dark) {
        :root {
            --background: #1e1e1e;
            --header-color: #ffffff;
            --sub-header-color: #cccccc;
            --card-bg: #333333;
            --card-text: #f0f0f0;
        }
    }
    @media (prefers-color-scheme: light) {
        :root {
            --background: #ffffff;
            --header-color: #004c3f;
            --sub-header-color: #333;
            --card-bg: #e0f7fa;
            --card-text: #000000;
        }
    }
    </style>
    """, unsafe_allow_html=True)

# Retrieve customer data from Firestore based on client ID in URL parameter
def get_customer_data(client_id):
    doc_ref = db.collection('leads').document(client_id)
    doc = doc_ref.get()
    if doc.exists:
        return doc.to_dict()
    else:
        st.error("Customer not found.")
        return None

# Main function to render the app
def main():
    # Load CSS
    set_css()

    # Header
    st.markdown('<div class="header">Sparknest Portal</div>', unsafe_allow_html=True)
    st.markdown('[Let us help you](https://docs.google.com/forms/d/e/1FAIpQLSdegpUtj6G4Sy7FavmEaWed1SnJL55r9UmHdrF6LcqFtxQK9g/viewform?usp=sf_link)', unsafe_allow_html=True)
    #st.markdown('<div class="sub-header">Find out how we can help</div>', unsafe_allow_html=True)

    # Get the customer ID from the URL
    query_params = st.query_params
    client_id = query_params.get('id', None)

    if client_id:
        customer_data = get_customer_data(client_id)
        if customer_data:
            # Display customer details in a card layout
            #st.markdown('<div class="card">', unsafe_allow_html=True)
            st.write(f"**Name**: {customer_data['Name']}")
            st.write(f"**Phone**: {customer_data['Contact_1']}")
            st.write(f"**Email**: {customer_data['Email']}")
            st.write(f"**Address**: {customer_data['address']}")
            st.write(f"**Amount Owed**: N{customer_data['updated_amount_deliquent']}")
            st.write(f"\n")
            st.write(f"Pay N{int(customer_data['updated_amount_deliquent']*.9)} now and Sparknest cover the rest for you 💰")
            st.write(f"You can make payment by depositing the amount into your Carbon account:")
            st.write(f"**{customer_data['Wallet_ID']}-Carbon**")
            st.markdown('</div>', unsafe_allow_html=True)

            # Discount offer in a highlighted banner
            #st.markdown('<div>💰 Get 10% reduction if you pay now!</div>', unsafe_allow_html=True)

            # Google form link for requesting assistance
            st.markdown('<div class="button-link">', unsafe_allow_html=True)
            st.markdown('[Request Assistance](https://docs.google.com/forms/d/e/1FAIpQLSdegpUtj6G4Sy7FavmEaWed1SnJL55r9UmHdrF6LcqFtxQK9g/viewform?usp=sf_link)', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

    else:
        st.error("No client ID found in the URL")

if __name__ == "__main__":
    main()
