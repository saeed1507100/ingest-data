from flask import Flask, render_template, Response
import subprocess

app = Flask(__name__)
SCRIPT_PATH = '/Users/saeed.anwar/Projects/ingest-data/app/test_data_integration.py'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/run_script')
def run_script():
    def run_script_generator():
        # Code to run your Python script
        process = subprocess.Popen(['python', SCRIPT_PATH], stdout=subprocess.PIPE,
                                   universal_newlines=True)

        # Read and yield each line of the script output
        for line in process.stdout:
            yield line

    return Response(run_script_generator(), mimetype='text/plain')


if __name__ == '__main__':
    app.run(port=3000)
