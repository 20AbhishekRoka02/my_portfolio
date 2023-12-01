import os
import json
json_creds_path = os.getenv('JSON_CREDS_PATH', '../credentials/secret.json')
with open(json_creds_path) as f:
    json_creds=json.load(f)


os.environ['FIREBASE_TYPE']=json_creds.get('FIREBASE_TYPE','')
os.environ['FIREBASE_PROJECT_ID']=json_creds.get('FIREBASE_PROJECT_ID','')
os.environ['FIREBASE_PRIVATE_KEY_ID']=json_creds.get('FIREBASE_PRIVATE_KEY_ID','')
os.environ['FIREBASE_PRIVATE_KEY']=json_creds.get('FIREBASE_PRIVATE_KEY','')
os.environ['FIREBASE_CLIENT_EMAIL']=json_creds.get('FIREBASE_CLIENT_EMAIL','')

os.environ['FIREBASE_AUTH_URI']=json_creds.get('FIREBASE_AUTH_URI','')
os.environ['FIREBASE_TOKEN_URI']=json_creds.get('FIREBASE_TOKEN_URI','')
os.environ['FIREBASE_AUTH_PROVIDER_X509_CERT_URL']=json_creds.get('FIREBASE_AUTH_PROVIDER_X509_CERT_URL','')
os.environ['FIREBASE_CLIENT_X509_CERT_URL'] = json_creds.get('FIREBASE_CLIENT_X509_CERT_URL','')
os.environ['FIREBASE_URNIVERSE_DOAMIN']=json_creds.get('FIREBASE_URNIVERSE_DOAMIN','')

