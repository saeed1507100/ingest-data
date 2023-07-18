import subprocess
from ui.src.constants import SCRIPT_PATH


def run_script_generator():
    # Code to run your Python script
    process = subprocess.Popen(['python', SCRIPT_PATH], stdout=subprocess.PIPE,
                               universal_newlines=True)

    # Read and yield each line of the script output
    for line in process.stdout:
        yield line