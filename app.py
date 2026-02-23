from flask import Flask,render_template,request,redirect,url_for,flash,session
from database import get_connection
from werkzeug.security import generate_password_hash,check_password_hash


app=Flask(__name__)
app.secret_key='super-secret'

@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    return render_template('index.html')

@app.route('/students')
def students():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    conn=get_connection()
    cursor=conn.cursor(dictionary=True)
    cursor.execute('select * from student')
    data=cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('students.html',student=data)

@app.route('/apply',methods=['GET','POST'])
def apply():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    if request.method=='POST':
        try:
            student_id=request.form.get('student_id')
            internship_id=request.form.get('internship_id')
            conn=get_connection()
            cursor=conn.cursor()
            cursor.execute('select application_id from application order by application_id desc limit 1')
            last_id=cursor.fetchone()
            if last_id:
                last_num=int(last_id[0][1:])
                current_id="A"+str(last_num+1).zfill(3)
            else:
                current_id='A001'
            cursor.execute("insert into application(application_id,student_id,internship_id) values(%s,%s,%s)",(current_id,student_id,internship_id))
            conn.commit()
            flash("Application submitted successfully!","success")
        except Exception as e:
            print(e)  
            if "Duplicate entry" in str(e):
                flash("You have already applied for this internship.", "error")
            else:
                flash("Something went wrong.","error")
        finally:
            cursor.close()
            conn.close()

        return redirect(url_for('apply'))
    return render_template('apply.html')

@app.route('/internships')
def internships():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    conn=get_connection()
    cursor=conn.cursor(dictionary=True)
    cursor.execute('select * from internship')
    data=cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('internships.html', internship=data)

@app.route('/analytics')
def analytics():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute('select count(*) from student')
    total_students=cursor.fetchone()[0]
    cursor.execute('select count(*) from internship')
    total_internships=cursor.fetchone()[0]
    cursor.execute('select count(*) from application')
    total_applications=cursor.fetchone()[0]
    cursor.execute("select count(*) from application where status='Selected'")
    total_placed=cursor.fetchone()[0]
    if total_students>0:
        placement_rate=round(((total_placed*100)/total_students),2)
    else:
        placement_rate=0
    cursor.execute("select a.internship_id,i.company_id,count(*) as applicants,sum(case when a.status='Selected' then 1 else 0 end) as selected,sum(case when a.status='Rejected' then 1 else 0 end) as rejected,sum(case when a.status='Shortlisted' then 1 else 0 end) as shortlisted from application a join internship i on i.internship_id=a.internship_id  group by a.internship_id,i.company_id order by applicants desc")
    data1=cursor.fetchall()
    cursor.execute("select s.branch,count(*) as applications,sum(case when a.status='Selected' then 1 else 0 end) as selected, sum(case when a.status='Rejected' then 1 else 0 end) as rejected,sum(case when a.status='Shortlisted' then 1 else 0 end) as shortlisted from student s join application a on s.student_id=a.student_id group by s.branch order by applications desc")
    data2=cursor.fetchall()
    cursor.execute("select s.skill_name from internship_skill ins join skill s on ins.skill_id=s.skill_id group by s.skill_name order by count(*) desc limit 3")
    top_skills=cursor.fetchall()
    cursor.execute("select s.skill_name from application a join student_skill ss on a.student_id=ss.student_id join skill s on s.skill_id=ss.skill_id where a.status='Selected' group by s.skill_name order by count(*) desc limit 3")
    selected_skill=cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('analytics.html',total_students=total_students, total_applications=total_applications,total_internships=total_internships,placement_rate=placement_rate, table1=data1, table2=data2, top_skills=top_skills, selected_skill=selected_skill)

@app.route('/register', methods=['GET','POST'])
def register():
    if request.method=='POST':
        conn=None
        cursor=None
        try:
            name=request.form.get('name')
            email_id=request.form.get('email_id')
            password=request.form.get('password')
            hashed_password = generate_password_hash(password)
            conn=get_connection()
            cursor=conn.cursor()
            cursor.execute('insert into user (name,email_id,password) values (%s,%s,%s)',(name,email_id,hashed_password))
            conn.commit()
            return redirect(url_for('login'))
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()

    return render_template('register.html')
        
@app.route('/login',methods=['GET','POST'])
def login():
    if request.method=='POST':
        conn=None
        cursor=None
        try:
            email_id=request.form.get('email_id')   
            password=request.form.get('password')   
            conn=get_connection()  
            cursor=conn.cursor()
            cursor.execute('select user_id,password from user where email_id=%s',(email_id,))
            user=cursor.fetchone()
            if user and check_password_hash(user[1], password):
                session['user_id'] = user[0]
                return redirect(url_for('dashboard'))
            else:
                return "Invalid email or password"
        except Exception as e:
            print(e)
            return ('Somethimg went wrong')
        finally:
            cursor.close()
            conn.close()
    return render_template('login.html')


if __name__=='__main__':
    app.run(debug=True)