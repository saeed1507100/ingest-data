from flask import Flask, render_template, Response, request

from ui.src.execution import run_script_generator
from ui.src.insert_data_endpoint import insert_data_endpoint

app = Flask(__name__)



@app.route('/')
def index():
    return render_template('index.html')


@app.route('/run_script')
def run_script():
    return Response(run_script_generator(), mimetype='text/plain')


# Insert Data page
@app.route('/insert')
def insert_data():
    return render_template('insert_data_endpoints.html')


# Handle the data insertion request
@app.route('/insert', methods=['POST'])
def insert_data_to_mongodb():

    insert_data_endpoint()

    return render_template('insert_data_endpoints.html', message='Data inserted successfully!')


if __name__ == '__main__':
    app.run(port=3000)
