from flask import Flask, render_template, session, redirect  #Importando Flask para permitirnos crear una aplicacion donde  flask es extesion y Flask es la clase Flask

app = Flask (__name__) # Creando una  instancia de Flask y la llamo app "(_name)"reemplaza el nombre del archivo en este caso server.py

app.secret_key="Esta es mi llave secreta."

@app.route('/')
def index():
    if "count" not in session:
        session["count"] = 0
    else:
        session['count'] += 1
    return render_template("index.html")

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')


if __name__ == "__main__": #Asegurando de que el archivo se esté ejecutando directamente y NO desde otro módulo
    app.run(debug=True)   #Ejecute mi aplicación

