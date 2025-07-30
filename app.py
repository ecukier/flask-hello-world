from flask import Flask
import psycopg

app = Flask(__name__)



@app.route('/')
def hello_world():
    return 'Hello World from Ephram Cukier in 3308'


@app.route('/db_test')
def db_test():
    conn = psycopg.connect("postgresql://flask_hello_world_db_3tcd_user:plLtvyBCNtZlopRpBONqG2naXcFO0nQv@dpg-d24q21ali9vc73eigphg-a/flask_hello_world_db_3tcd")
    conn.close()
    return 'Database connection succesfull'


@app.route('/db_create')
def db_create():
    conn = psycopg.connect("postgresql://flask_hello_world_db_3tcd_user:plLtvyBCNtZlopRpBONqG2naXcFO0nQv@dpg-d24q21ali9vc73eigphg-a/flask_hello_world_db_3tcd")
    cur = conn.cursor()

    cur.execute('''
        CREATE TABLE IF NOT EXISTS Basketball(
            First varchar(255),
            Last varchar(255),
            City varchar(255),
            Name varchar(255),
            Number int
            );
    ''')
    conn.close()
    return 'Basketball table succesfully created'