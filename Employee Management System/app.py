from database import conn,cursor
from flask import Flask,render_template,request,redirect

app = Flask(__name__)

#get
@app.route("/")
def home():
    
    # return render_template("index.html",res=[{"id":101,"name":"celvin","email":"celvin@gmail.com"},{"id":102,"name":"ameen","email":"ameen@gmail.com"}])
    # breakpoint()
    # import pdb;pdb.set_trace()
    res = cursor.execute('''SELECT * FROM employee''')
    all_res = res.fetchall()
    return render_template("index.html",res=all_res)

    
@app.route("/add")
def add():
    return render_template("add.html")


@app.route("/adddb", methods=['POST','GET'])
def adddb():
    if request.method == 'POST':
        id = request.form['empid']
        name = request.form['empname']
        email = request.form['empemail']
        # print([id,name,email])
        cursor.execute('''INSERT INTO employee(id,name,email) VALUES(?,?,?)''',(id,name,email))
        conn.commit()
        return redirect('/')
    
    
#To edit empoyee info
@app.route("/<id>/edit")
def edit(id):
    res = cursor.execute('''SELECT * FROM employee WHERE id=?''',(id,))
    my_res = res.fetchone()
    return render_template('update.html', res=my_res)

@app.route("/editdb", methods=['POST','GET'])
def editdb():
    if request.method == 'POST':
        id = request.form['empid']
        name = request.form['empname']
        email = request.form['empemail']
        # print([id,name,email]) 
        cursor.execute('''UPDATE employee SET name=?,email=? WHERE id=?''',(name,email,id))
        conn.commit()
        print("Updated successfully!")
        return redirect('/')
    
@app.route("/<id>/delete")
def delete(id):
    cursor.execute('''DELETE FROM employee WHERE id=?''',(id,))
    conn.commit()
    print("Employee deleted successfully!!")
    return redirect('/')
if __name__=='__main__':
    app.run(debug=True)

#import pdb;pdb.set_trace()