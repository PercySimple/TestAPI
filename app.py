import numpy as np

from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

#importing function for calculations
from matrix_calc_function import matrix_calc


@app.route("/")
def home():
  return render_template('index.html')

#@app.route("/math_func", methods = ['POST'])
#def math_func():
#  x = request.form['x']
#  n = request.form['n']
#  operation = str(request.form['operation'])
#  result = matrix_calc(x, n, operation)
#  return render_template('index.html', result_text = str(result))

@app.route("/post_json", methods = ['POST'])
def process_json():
  content_type = request.headers.get('Content-Type')
  if (content_type == 'application/json'):
    json = request.json
    return json
  else:
    return 'Content-Type not supported!'
  
  

# def math_function():
# x = request.json['x']
# n = request.json['n']
# operation = request.json['operation']
# result = matrix_calc(x, n, operation)
# return jsonify(result)

if __name__ == '__main__':
  app.run(host='0.0.0.0',debug=True)