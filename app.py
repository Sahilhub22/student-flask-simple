from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory student list (replace with DB later)
students = []

@app.route('/')
def index():
    return render_template('index.html', students=students)

@app.route('/add', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        name = request.form['name']
        roll = request.form['roll']
        students.append({'name': name, 'roll': roll})
        return redirect(url_for('index'))
    return render_template('add_student.html')

@app.route('/edit/<int:student_id>', methods=['GET', 'POST'])
def edit_student(student_id):
    student = students[student_id]
    if request.method == 'POST':
        student['name'] = request.form['name']
        student['roll'] = request.form['roll']
        return redirect(url_for('index'))
    return render_template('edit_student.html', student=student, student_id=student_id)

@app.route('/delete/<int:student_id>')
def delete_student(student_id):
    students.pop(student_id)
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

