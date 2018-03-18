from flask import Flask, jsonify, render_template, request, jsonify
import sqlite3 as sql
app = Flask(__name__)
con = sql.connect('Task2.db')                              #Connection to DB
cur = con.cursor()

@app.route('/')
def index():
    return render_template('task2.html')

@app.route('/_background_process')
def background_process():
    lang = request.args.get('proglang', 0, type=str)        #Fetching from HTML PAGE
    motor_list=[]
    if lang!="":
         motor_list = list(map(int,lang.split(',')))
    if len(motor_list)<1:
       try:
           cur.execute("DROP TABLE store ")                    #Dropping previous data
           cur.execute("Create Table store(csm1)")              #creating fresh table
           con.commit()
       except:
           print("Table Already Empty")
    elif len(motor_list)>0:
       cur.execute('PRAGMA TABLE_INFO(%s)'%('store'))         #Extracting Table Info
       names = [tup[1] for tup in cur.fetchall()]             #Fetching Column Details
       nI = len(names)
       if (nI<len(motor_list)):                               #Inserting new column.. Handled for creation of more than one motor at a time
           diff=len(motor_list)-nI
           for i in range(1,diff+1):
               cur.execute("ALTER TABLE store ADD COLUMN %s TEXT;"%('csm'+str(nI+i)))
               con.commit()
       cur.execute('PRAGMA TABLE_INFO(%s)'%('store'))         #Again fetching the total number of columns and their names for Dynamic insertion of data
       names = [tup[1] for tup in cur.fetchall()]
       cur.execute("INSERT INTO store(%s) VALUES(%s)"%(str(names)[1:-1],str(motor_list)[1:-1]))
       con.commit()
    return jsonify(True)

            
if __name__ == '__main__':
     app.run()
