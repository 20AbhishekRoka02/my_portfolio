from django.http import HttpResponse
from django.shortcuts import render, redirect


def index(request):
    return render(request,'index.html')

# def check(request):
#     return render(request,'checkform.html')





# Code added here
import hashlib
def hash_password(password):
    # Encode the password as bytes
    password_bytes = password.encode('utf-8')

    # Create a SHA-256 hash object
    sha256_hash = hashlib.sha256()

    # Update the hash object with the password bytes
    sha256_hash.update(password_bytes)

    # Get the hexadecimal representation of the hashed password
    hashed_password = sha256_hash.hexdigest()

    return hashed_password

from firebase_admin import auth, firestore
db = firestore.client()

def check_user_exists(email):
    try:
        # Retrieve user by email
        user = auth.get_user_by_email(email)
        # print(f"User with email {email} exists.")
        # print(f"User UID: {user.uid}")
        return True
    except Exception as e:        
        return False

def addUserWithPassword(uid, password):
    try:
        
        db.collection("UserPasses").document(uid).set({'password':password})
        return True
    except Exception as e:
        print(e)
    return False

    
def signup(request):
    if request.method == 'POST':
        form_data = request.POST

        email = form_data.get('email')
        if not check_user_exists(email):
            password=hash_password(form_data.get('pass'))
            new_user = auth.create_user(email=email)
            uid = auth.get_user_by_email(email).uid
            if (addUserWithPassword(uid, password)):
                return HttpResponse("""
<h1> Your Account has been created! </h1>
<a href="login/"> Login </a>
""")
            else:
                auth.delete_user(uid)
                return HttpResponse("Unable to create account now, Please try again later.")
        else:
            return HttpResponse("""
<h1>This User already exists!</h1>
<p> Please <a href="login/"> Log in </a>! </p>
                                    

""")
    if request.method == "GET":
        if 'uid' in request.COOKIES:
            return redirect("index")
    return render(request,"signup.html")

def verifyPassword(uid,password):
    if (password == db.collection("UserPasses").document(uid).get().to_dict()["password"]):
        return True
    return False
    

    


def login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = hash_password(request.POST.get('pass'))
        # print("Working!")
        try:
                # print("working!")              
            if check_user_exists(email):
                user = auth.get_user_by_email(email)
                # .set_cookie('uid',user.uid, httponly=True)
                if (verifyPassword(user.uid, password)):  
                    response = HttpResponse("""
                                            <h1>Your Sucessfully logged in!</h1>
                                            <a href="/">Go back to home page! </a>
                                            """)
                    response.set_cookie('uid',user.uid,httponly=True)
                    return response
                else:
                    return HttpResponse("""
<h1>This User not exists!</h1>
<p> Please <a href="signup/"> Sign up </a> first! </p>
                                    

""")
        
        except Exception as e:
            return HttpResponse(f"{e}")
    if request.method == "GET":
        if 'uid' in request.COOKIES:
            return redirect("index")
    return render(request,"login.html")

# def logout(request):
#     pass

# def index(request):
#     return render(request,'index.html')
#     pass

# def summary(request):
#     return render(request,"summary.html")