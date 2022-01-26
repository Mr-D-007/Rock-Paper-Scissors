from django.shortcuts import render
import sqlite3
from passlib.context import CryptContext

pwd_context = CryptContext(
        schemes=["pbkdf2_sha256"],
        default="pbkdf2_sha256",
        pbkdf2_sha256__default_rounds=30000
)
def encrypt_password(password):
    return pwd_context.encrypt(password)


def check_encrypted_password(password, hashed):
    return pwd_context.verify(password, hashed)

def register(request):
    return render(request, 'register.html')

def check(request):
    name = request.GET.get("Name")
    mail = request.GET.get("MailID")
    passw = request.GET.get("password")
    conn = sqlite3.connect('db.sqlite3')
    cc = conn.cursor()
    cc.execute("SELECT * from rps_app_user where User_Name=? and Mail_id=?", (name, mail))
    records = cc.fetchall()
    encrypted = encrypt_password(passw)
    if len(records) > 0:
        msg = 0
    else:
        cc.execute("INSERT INTO rps_app_user (User_Name, Mail_id,password) VALUES(?, ?,?)",
                   (name, mail, encrypted))
        conn.commit()
        msg = 1
        cc.close()
        conn.close()
    return render(request, 'register.html', {'data': msg})

def login(request):
    return render(request, 'login.html')

def checklogin(request):
    name = request.GET.get("Name")
    passw = request.GET.get("password")
    conn = sqlite3.connect('db.sqlite3')
    cc = conn.cursor()
    query_str = "SELECT password from rps_app_user where User_Name='"+name+"'"
    print(query_str)
    cc.execute(query_str)
    passwd_from_db = cc.fetchall()
    decrypted = check_encrypted_password(passw, passwd_from_db[0][0])
    if decrypted:
        msg = 0
    else:
        msg = 1
    cc.close()
    conn.close()
    return render(request, 'login.html', {'data': msg})

def home(request):
    return render(request, 'home.html')
