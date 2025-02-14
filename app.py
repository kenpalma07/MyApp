from flask import Flask, flash, jsonify, redirect, url_for, render_template, Blueprint, request
from datetime import datetime, timezone
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from sqlalchemy.sql import func
import os
import secrets

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost:3308/patient_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

patient_bp = Blueprint('patient', __name__)
register_bp = Blueprint('register', __name__)
home_bp = Blueprint('home', __name__)
edit_bp = Blueprint('edit', __name__)

app.secret_key = secrets.token_hex(16) # 16 characters long
current_number = 1

class register_pat(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    hpatcode = db.Column(db.String(100), nullable=False)
    pfname = db.Column(db.String(100), nullable=False)
    pmname = db.Column(db.String(100), nullable=True)
    plname = db.Column(db.String(100), nullable=False)
    psuffix = db.Column(db.String(20), nullable=True)
    pbirthdate = db.Column(db.Date, nullable=False)
    psex = db.Column(db.String(10), nullable=False)
    pcstatus = db.Column(db.String(20), nullable=False)
    psaddress = db.Column(db.String(255), nullable=False)
    pscity = db.Column(db.String(100), nullable=False)
    psbrgy = db.Column(db.String(100), nullable=False)
    psregion = db.Column(db.String(100), nullable=False)
    psdistrict = db.Column(db.String(100), nullable=False)
    psprovince = db.Column(db.String(100), nullable=False)
    pszipcode = db.Column(db.String(10), nullable=False)
    pscountry = db.Column(db.String(100), nullable=False)
    praddress = db.Column(db.String(255), nullable=False)
    prcity = db.Column(db.String(100), nullable=False)
    prbrgy = db.Column(db.String(100), nullable=False)
    prregion = db.Column(db.String(100), nullable=False)
    prdistrict = db.Column(db.String(100), nullable=False)
    prprovince = db.Column(db.String(100), nullable=False)
    przipcode = db.Column(db.String(10), nullable=False)
    prcountry = db.Column(db.String(100), nullable=False)
    cpname = db.Column(db.String(100), nullable=False)
    cpaddress = db.Column(db.String(255), nullable=False)
    cptel = db.Column(db.String(15), nullable=False)
    cprelationship = db.Column(db.String(50), nullable=True)
    created_at = db.Column(db.DateTime, default=func.now())
    updated_at = db.Column(db.DateTime, default=func.now(), onupdate=func.now(), nullable=True)
    pstats = db.Column(db.String(15), nullable=False)


@app.route('/submit', methods=['GET', 'POST'])
def receive_data():
    if request.method == 'POST':
        new_patient = register_pat(
            hpatcode=request.form.get('hpatcode'),
            pfname=request.form.get('pfname'),
            pmname=request.form.get('pmname', ''),
            plname=request.form.get('plname'),
            psuffix=request.form.get('psuffix', ''),
            pbirthdate=request.form.get('pbirthdate'),
            psex=request.form.get('psex'),
            pcstatus=request.form.get('pcstatus'),
            psaddress=request.form.get('psaddress'),
            pscity=request.form.get('pscity'),
            psbrgy=request.form.get('psbrgy'),
            psregion=request.form.get('psregion'),
            psdistrict=request.form.get('psdistrict'),
            psprovince=request.form.get('psprovince'),
            pszipcode=request.form.get('pszipcode'),
            pscountry=request.form.get('pscountry'),
            praddress=request.form.get('praddress'),
            prcity=request.form.get('prcity'),
            prbrgy=request.form.get('prbrgy'),
            prregion=request.form.get('prregion'),
            prdistrict=request.form.get('prdistrict'),
            prprovince=request.form.get('prprovince'),
            przipcode=request.form.get('przipcode'),
            prcountry=request.form.get('prcountry'),
            cpname=request.form.get('cpname'),
            cpaddress=request.form.get('cpaddress'),
            cptel=request.form.get('cptel'),
            cprelationship=request.form.get('cprelationship'),
            pstats='Active'
        )

        db.session.add(new_patient)
        db.session.commit()

        return redirect(url_for('success'))  # Redirect instead of rendering

    return render_template('index.html', content='Testing')

@app.route('/success')
def success():
    return redirect(url_for('patient.patient'))
    # return "Registration Successful!"

@app.route('/update/<int:patient_id>', methods=['POST'])
def update(patient_id):
    patient = register_pat.query.get_or_404(patient_id)
    
    patient.pfname = request.form.get('pfname')
    patient.pmname = request.form.get('pmname')
    patient.plname = request.form.get('plname')
    patient.psuffix = request.form.get('psuffix')
    patient.pbirthdate = request.form.get('pbirthdate')
    patient.psex = request.form.get('psex')
    patient.pcstatus = request.form.get('pcstatus')
    patient.psaddress = request.form.get('psaddress')
    patient.pscity = request.form.get('pscity')
    patient.psbrgy = request.form.get('psbrgy')
    patient.psregion = request.form.get('psregion')
    patient.psdistrict = request.form.get('psdistrict')
    patient.psprovince = request.form.get('psprovince')
    patient.pszipcode = request.form.get('pszipcode')
    patient.pscountry = request.form.get('pscountry')
    patient.praddress = request.form.get('praddress')
    patient.prcity = request.form.get('prcity')
    patient.prbrgy = request.form.get('prbrgy')
    patient.prregion = request.form.get('prregion')
    patient.prdistrict = request.form.get('prdistrict')
    patient.prprovince = request.form.get('prprovince')
    patient.przipcode = request.form.get('przipcode')
    patient.prcountry = request.form.get('prcountry')
    patient.cpname = request.form.get('cpname')
    patient.cpaddress = request.form.get('cpaddress')
    patient.cptel = request.form.get('cptel')
    patient.cprelationship = request.form.get('cprelationship')
    
    db.session.commit()
    
    flash("Patient updated successfully!", "success")
    
    return redirect(url_for('patient.patient'))
    
@patient_bp.route('/patient')
def patient():
    patients = register_pat.query.filter_by(pstats="Active").all()  # Fetch all records from MySQL
    
    for patient in patients:
        patient.full_name = f"{patient.plname}, {patient.pfname} {patient.pmname or ''}".strip()
    
    return render_template('patients.html', patients=patients)

@app.route('/get_patient/<int:patient_id>')
def get_patient(patient_id):
    patient = register_pat.query.get(patient_id)
    
    formatted_birthdate = patient.pbirthdate.strftime("%m/%d/%Y") if patient.pbirthdate else None
    full_name = f"{patient.plname}, {patient.pfname}, {patient.pmname}".strip()
    full_address = f"{patient.psaddress}, {patient.psbrgy}, {patient.psprovince}, {patient.psregion}, {patient.pszipcode}, {patient.pscountry}".strip()
    
    if not patient:
        return jsonify({"error": "Patient not found"}), 404
    return jsonify({
        "id": patient.id,
        "hcode": patient.hpatcode,
        "name": full_name,
        "birthdate": formatted_birthdate,
        "sex": patient.psex,
        "status" : patient.pcstatus,
        "address": full_address,
        "cperson" : patient.cpname,
        "cpaddress" : patient.cpaddress,
        "cptel" : patient.cptel,
        "cprelationship" : patient.cprelationship
    })

@register_bp.route('/register')
def register():
    last_patient = register_pat.query.order_by(register_pat.id.desc()).first()
    
    if last_patient and last_patient.hpatcode:
        last_number = int(last_patient.hpatcode)  # Convert stored string to integer
    else:
        last_number = 0
        
    new_number = last_number + 1
    formatted_number = f"{new_number:015d}"  # Format the number to 15 digits
    return render_template('register.html', formatted_number=formatted_number)

@edit_bp.route('/edit/<int:patient_id>', methods=['GET'])
def edit(patient_id):
    patient = register_pat.query.get_or_404(patient_id)
    return render_template('edit.html', patient=patient)

@app.route('/delete_patient/<int:patient_id>', methods=['POST'])
def soft_delete_patient(patient_id):
    patient = register_pat.query.get(patient_id)
    
    if not patient:
        return jsonify({"error": "Patient not found"}), 404

    # Soft delete: Change status to Inactive and store timestamp
    patient.pstats = "Inactive"
    patient.deleted_at = datetime.now(timezone.utc)

    db.session.commit()
    flash("Patient record soft deleted successfully", "success")
    return redirect(url_for('patient.patient'))

@app.route('/consent/<int:patient_id>')
def consent(patient_id):
    patient = register_pat.query.get(patient_id)
    
    if not patient:
        return "Patient not found", 404  # Handle missing patient
    
    return render_template('consent.html', patient=patient)

@home_bp.route('/')
def home():
    return render_template('index.html', content='Testing')

# Register the blueprints
app.register_blueprint(home_bp)
app.register_blueprint(patient_bp)
app.register_blueprint(register_bp)
app.register_blueprint(edit_bp)

if __name__ == '__main__':
    app.run(debug=True)
