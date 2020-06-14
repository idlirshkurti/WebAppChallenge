from flask import Flask, request, redirect, render_template
import webbrowser


app = Flask(__name__)

@app.route('/') 
def sql_database():
    from functions.sqlquery import sql_query
    results = sql_query('''SELECT * FROM task_data''')
    msg = 'SELECT * FROM task_data'
    return render_template('sqldatabase.html', results=results, msg=msg) 
 
@app.route('/insert',methods = ['POST', 'GET']) #this is when user submits an insert
def sql_datainsert():
    from functions.sqlquery import sql_edit_insert, sql_query
    if request.method == 'POST':
        id = request.form['id']
        timestamp = request.form['timestamp']
        temperature = request.form['temperature']
        duration = request.form['duration']
        sql_edit_insert('''INSERT INTO task_data(id ,timestamp ,temperature , duration)
        VALUES (?, ?, ?, ?)''', (id ,timestamp ,temperature , duration))
    results = sql_query(''' SELECT * FROM task_data''')
    msg = 'INSERT INTO task_data(id ,timestamp ,temperature , duration) VALUES ('+id+','+timestamp+','+temperature+','+duration+')'
    return render_template('sqldatabase.html', results=results, msg=msg) 

if __name__ == "__main__":
    webbrowser.open('http://localhost:5000')
    app.run(debug=True)
