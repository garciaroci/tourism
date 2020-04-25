from flask import Flask, escape, request, render_template
import mysql.connector as mysql

# Conectamos a la base de datos
db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = "password",
    database = "turism"
)

def get_states():
    cursor = db.cursor()

    ## Consultamos todas las provincias cargadas
    query = "SELECT * FROM state"

    ## Ejecutamos la consulta
    cursor.execute(query)

    ## Obtenemos el resultado de la consulta. 
    states = cursor.fetchall()

    result = []
    for state in states:
        result.append({
            "id": state[0],
            "name": state[1],
            "description": state[2],
            "image_url": state[3],
            "video_url": state[4],
        })
        
    return result

def get_state(id):
    cursor = db.cursor()

    ## Consultamos por una provincia en particular buscando por id
    query = "SELECT * FROM state WHERE id = %s" % str(id)

    ## Ejecutamos la consulta
    cursor.execute(query)

    ## Obtenemos el resultado de la consulta. 
    states = cursor.fetchall()

    return {
            "id": states[0][0],
            "name": states[0][1],
            "description": states[0][2],
            "image_url": states[0][3],
            "video_url": states[0][4],
        }

app = Flask(__name__)

@app.route('/')
def index():
    states_list = get_states()

    return render_template('index.html', states_list=states_list)

@app.route('/provincia/<state_id>')
def state(state_id):
    state = get_state(state_id)
    return render_template('state.html', state=state)
