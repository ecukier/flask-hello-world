from flask import Flask
import psycopg2

app = Flask(__name__)



@app.route('/')
def hello_world():
    return 'Hello World from Ephram Cukier in 3308'


@app.route('/db-test')
def db_test():
    conn = psycopg2.connect("postgresql://flask_hello_world_db_3tcd_user:plLtvyBCNtZlopRpBONqG2naXcFO0nQv@dpg-d24q21ali9vc73eigphg-a/flask_hello_world_db_3tcd")
    conn.close()
    return 'Database connection succesfull'