from flask import Flask, render_template,request
from validate_email import validate_email
import smtplib
import uuid
import datetime
import schedule

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("Home.html")

all_data = []
data = {}

def validate_phone(num):
    num = str(num)
    if num[0] in ['6','7','8','9'] and len(num)==10:
        return True
    return False

@app.route("/submit",methods=["POST"])
def submit():
    issue_data_time = str(datetime.datetime.now())
    booking_id = uuid.uuid4()
    username = request.form.get("username")
    phone_number = request.form.get("contact_number")
    email = request.form.get("email_id")
    
    if validate_email(email) and validate_phone(phone_number):
        data["booking_id"] = booking_id
        data["name"] = username
        data["phone"] = phone_number
        data["email"] = email
        
        return(render_template("Trip_Form.html",name = username))
    
    else:
        return(render_template("Home.html",error="Please Provide Valid number and email ID"))

@app.route("/trip_details",methods=["POST"])
def trip_details():
    start_date = request.form.get("start_date")
    start_time = request.form.get("start_time")
    start_location = request.form.get("start_location")
    end_location = request.form.get("end_location")
    trip_type = request.form.get("trip_type")
    
    data["start_date"] = start_date
    data["start_time"] = start_time
    data["start_location"] = start_location
    data["end_location"] = end_location
    data["trip_type"] = trip_type
    
    all_data.append(data)
    
    return render_template("trip-summary.html",Data = data)

@app.route("/invoice",methods=["POST"])
def invoice():
    
    email = "erdeshmukhyash@gmail.com"
    receiver = data["email"]
        
    border = "-"*50
    subject = "Your trip has been generated"
    message = f'''
            Subject : {subject}
            
            
            Hello {data["name"]},
            
            You are starting your Journey from {data["start_location"]} to {data["end_location"]}
            starting in {data["start_date"]} 
            {border}
            
            Thank you for choosing us : 
            | Contact us : 7350604040 | email : erdeshmukhyash@gmail.com |
    '''
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()

    server.login(email,"sunchzdeftgzlxmm")
    server.sendmail(email,receiver,message)

    all_data.append(data)
    return render_template("Trip_Invoice.html" ,Data = data)

