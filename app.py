# # Varibles can be passed from your Python code. Python needs to render templates, so import the module for that.
# from flask import render_template, Flask

# app = Flask(__name__)

# @app.route('/')
# @app.route('/index')
# def index():
#     name = 'Rosalia'
#     return render_template('index.html', title='Welcome', username=name)

from flask import Flask, request, Response, render_template
import time
import random

app = Flask(__name__)

def run_my_script(input):
    # Generate some random data based on the input
    data = []
    for i in range(int(input)):
        data.append(random.randint(1, 60))

    # Return the data as a string
    return str(data)

@app.route('/',  methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        input = request.form['input']
        if input:
            output = run_my_script(input)
            return render_template('index.html', title='Win the Lotto', output=output)
        else:
            return render_template('index.html', title='Win the Lotto')
    else:
        return render_template('index.html')

@app.route('/streaming')
def streaming_function():
    def generate_data():
        while True:
            # Run your script here
            output = run_my_script(5)

            yield f"data:{output}\n\n"
            time.sleep(1)

    return Response(generate_data(), mimetype='text/event-stream')