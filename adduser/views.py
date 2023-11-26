from django.shortcuts import HttpResponse

from django.http import JsonResponse
import firebase_admin
from firebase_admin import firestore
import json

def addInterestUser(request):
    if request.method == 'POST':
        try:
            # print(request.body)
            # Get data from the form
            data = json.loads(request.body)

            # Access data using keys
            fullname = data.get('fullname')
            email = data.get('email')
            subject = data.get('subject')
            message = data.get('message')

            # Store data in Firebase Firestore
            db = firestore.client()
            db.collection('interestUser').add({
                    'fullname': fullname,
                    'email': email,
                    'subject': subject,
                    'message': message,
                    # Add other fields as needed
                })

            return JsonResponse({'status': 'success'})
        except json.JSONDecodeError as e:
            return JsonResponse({'status': 'error', 'message': 'Invalid JSON format'})
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'})

def check_site(request):
    return HttpResponse("Hello, World")