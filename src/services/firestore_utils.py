import os
from google.cloud import firestore
import datetime

# Specify the path to your credentials JSON file
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/Users/olaoye/Desktop/Projects/sales_bot/adaditech-7de9347adf7b.json'

# Initialize Firestore client
db = firestore.Client()

def read_collection(collection_name):
    """Read all documents from a Firestore collection."""
    collection_ref = db.collection(collection_name)
    docs = collection_ref.stream()
    docs_list = []
    for doc in docs:
        doc_dict = doc.to_dict()
        doc_dict['id'] = doc.id
        docs_list.append(doc_dict)
    return docs_list

def write_document(collection_name, document_id, data):
    """Write data to a Firestore document."""
    doc_ref = db.collection(collection_name).document(document_id)
    doc_ref.set(data)

def update_document(collection_name, document_id, data):
    """Update an existing Firestore document."""
    doc_ref = db.collection(collection_name).document(document_id)
    doc_ref.update(data)

def delete_document(collection_name, document_id):
    """Delete a document from Firestore."""
    doc_ref = db.collection(collection_name).document(document_id)
    doc_ref.delete()

def query_collection(collection_name, field_name, operator, value):
    """Query a Firestore collection."""
    collection_ref = db.collection(collection_name)
    query = collection_ref.where(field_name, operator, value)
    docs = query.stream()
    docs_list = []
    for doc in docs:
        doc_dict = doc.to_dict()
        doc_dict['id'] = doc.id
        docs_list.append(doc_dict)
    return docs_list

