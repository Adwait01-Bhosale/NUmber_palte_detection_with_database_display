import os
from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from PIL import Image

UPLOAD_FOLDER = "static/uploads/"
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =\
    'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime(timezone=True),
                           server_default=func.now())
    bio = db.Column(db.Text)

    def __repr__(self):
        return f'<Student {self.created_at}>'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/services/')
def services():
    students = Student.query.all()
    return render_template('services.html', students=students)


@app.route('/about/')
def about():
    return render_template('aboutUs.html')


@app.route('/<int:student_id>/')
def student(student_id):
    student = Student.query.get_or_404(student_id)
    return render_template('student.html', student=student)


@app.route('/get_ocr/', methods=('GET', 'POST'))
def image_ocr():
    if request.method == 'POST':
        image = request.files['file']
        # print(image)
        if image.filename != '':
            image.save(UPLOAD_FOLDER+image.filename)
            from function import extract_text
            ocr = extract_text(UPLOAD_FOLDER+image.filename)
            print("*************************")
            print(ocr)
        cars = Student(bio=str(ocr))
        db.session.add(cars)
        db.session.commit()
    return render_template('getOCR.html')

# @app.route('/image_ocr')
# def image_ocr():
#     return render_template('image_input.html')


if __name__ == '__main__':
    app.run(debug=True, port=5000)
