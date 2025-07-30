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
    conn.commit()
    conn.close()
    return 'Basketball table succesfully created'


@app.route('/db_insert')
def db_insert():
    conn = psycopg.connect("postgresql://flask_hello_world_db_3tcd_user:plLtvyBCNtZlopRpBONqG2naXcFO0nQv@dpg-d24q21ali9vc73eigphg-a/flask_hello_world_db_3tcd")
    cur = conn.cursor()

    cur.execute('''
        INSERT INTO Basketball (First, Last, City, Name, Number)
        Values
        ('Jayson', 'Tatum', 'Boston', 'Celtics', 0),
        ('Stephen', 'Curry', 'San Francisco', 'Warriors', 30),
        ('Nikola', 'Jokic', 'Denver', 'Nuggets', 15),
        ('Kawhi', 'Leonard', 'Los Angeles', 'Clippers', 2);
    ''')
    conn.commit()
    conn.close()
    return 'Basketball table succesfully populated'


@app.route('/db_select')
def db_select():
    conn = psycopg.connect("postgresql://flask_hello_world_db_3tcd_user:plLtvyBCNtZlopRpBONqG2naXcFO0nQv@dpg-d24q21ali9vc73eigphg-a/flask_hello_world_db_3tcd")
    cur = conn.cursor()
    cur.execute('''
        SELECT * FROM Basketball;
    ''')

    records = cur.fetchall()
    conn.close()

    response_string = '<table>'
    for player in records:
        response_string += '<tr>'
        for info in player:
            response_string += f'<td>{info}</td>'
        response_string += '</tr>'
    response_string += '</table>'
    return response_string



@app.route('/db_drop')
def db_drop():
    conn = psycopg.connect("postgresql://flask_hello_world_db_3tcd_user:plLtvyBCNtZlopRpBONqG2naXcFO0nQv@dpg-d24q21ali9vc73eigphg-a/flask_hello_world_db_3tcd")
    cur = conn.cursor()

    cur.execute('''
        DROP TABLE Basketball;
    ''')
    conn.commit()
    conn.close()
    return 'Basketball table succesfully dropped'
