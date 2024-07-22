from flask import Flask, request, render_template, redirect
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
 
app =Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
 
class EmployeeModel(db.Model):
    __tablename__ = "table"
 
    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.Integer(),unique = True)
    name = db.Column(db.String())
    age = db.Column(db.Integer())
    position = db.Column(db.String(80))
 
    def __init__(self, employee_id,name,age,position):
        self.employee_id = employee_id
        self.name = name
        self.age = age
        self.position = position
 
    def __repr__(self):
        return f"{self.name}:{self.employee_id}"

@app.route('/data')
def RetrieveDataList():
    employees = EmployeeModel.query.all()
    return render_template('datalist.html',employees = employees)

@app.route('/data/create' , methods = ['GET','POST'])
def create():
    if request.method == 'GET':
        return render_template('createpage.html')
 
    if request.method == 'POST':
        employee_id = request.form['employee_id']
        name = request.form['name']
        age = request.form['age']
        position = request.form['position']
        employee = EmployeeModel(employee_id=employee_id, name=name, age=age, position = position)
        db.create_all()
        db.session.add(employee)
        db.session.commit()
        return redirect('/data')
    
app.run(host='localhost', port=5000)
