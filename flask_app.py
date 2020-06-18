from flask import Flask, request, redirect, render_template
import webbrowser


app = Flask(__name__)

@app.route('/') 
def sql_database():
    from functions.sqlquery import sql_edit_insert, sql_query, sql_input_query
    from time import strftime
    import sqlite3
    results = sql_query('''SELECT * FROM task_data''')
    query = 'SELECT * FROM task_data'
    timestamp = strftime("%a, %d %b %Y %H:%M:%S")
    sql_edit_insert('''INSERT INTO logs(query, timestamp)
        VALUES (?, ?)''', (query, timestamp))
    return render_template('sqldatabase.html', results=results, msg=query) 
 
@app.route('/insert',methods = ['POST', 'GET']) #this is when user submits an insert
#def sql_datainsert():
#    from functions.sqlquery import sql_edit_insert, sql_query
#    if request.method == 'POST':
#        id = request.form['id']
#        timestamp = request.form['timestamp']
#        temperature = request.form['temperature']
#        duration = request.form['duration']
#        sql_edit_insert('''INSERT INTO task_data(id ,timestamp ,temperature , duration)
#        VALUES (?, ?, ?, ?)''', (id ,timestamp ,temperature , duration))
#    results = sql_query(''' SELECT * FROM task_data''')
#    msg = 'INSERT INTO task_data(id ,timestamp ,temperature , duration) VALUES ('+id+','+timestamp+','+temperature+','+duration+')'
#    return render_template('sqldatabase.html', results=results, msg=msg) 


@app.route('/filter',methods = ['POST', 'GET']) #this is when user submits an insert
def sql_datainsert():
    from functions.sqlquery import sql_edit_insert, sql_query, sql_input_query
    from time import strftime
    import sqlite3
    if request.method == 'POST':
        id = request.form['id']
#        timestamp = request.form['timestamp']
#        temperature = request.form['temperature']
#        duration = request.form['duration']
#        sql_edit_insert('''INSERT INTO task_data(id ,timestamp ,temperature , duration)
#        VALUES (?, ?, ?, ?)''', (id ,timestamp ,temperature , duration))
    results = sql_input_query('''SELECT * FROM task_data WHERE id = (?)''', (id,))
#    msg = 'INSERT INTO task_data(id ,timestamp ,temperature , duration) VALUES ('+id+','+timestamp+','+temperature+','+duration+')'
    query = 'SELECT * FROM task_data WHERE id = ' + str(id)
    timestamp = strftime("%a, %d %b %Y %H:%M:%S")
    sql_edit_insert('''INSERT INTO logs(query, timestamp)
        VALUES (?, ?)''', (query, timestamp))

 #   conn = sqlite3.connect('example.db', check_same_thread=False)
 #   cur = conn.cursor()
 #   cur.execute('''INSERT INTO logs(query, timestamp)
 #       VALUES (?, ?)''', (query, timestamp))
    return render_template('sqldatabase.html', results=results, msg=query) 


if __name__ == "__main__":
    webbrowser.open('http://localhost:5000')
    app.run(debug=True)
