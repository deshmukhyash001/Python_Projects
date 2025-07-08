from flask import Flask, render_template,request
from validate_email import validate_email

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
    username = request.form.get("username")
    phone_number = request.form.get("contact_number")
    email = request.form.get("email_id")
    
    if validate_email(email) and validate_phone(phone_number):
        data["name"] = username
        data["phone"] = phone_number
        data["email"] = email
        
        return(render_template("Trip_Form.html",name = username))
    
    else:
        return(render_template("Home.html",error="Please Provide Valid number and email ID"))
    
@app.route("/trip_details",methods=["POST"])
def trip_details():
    start_date = request.form.get("start_data")
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
    
    return render_template("trip-summary.html")
