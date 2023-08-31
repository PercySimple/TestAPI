import numpy as np
import json
import time

from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

@app.route("/")
def home():
  return render_template('index.html')

'''@app.route("/math_func", methods = ['POST'])
def math_func():
  x = request.form['x']
  n = request.form['n']
  operation = str(request.form['operation'])
  result = matrix_calc(x, n, operation)
  return render_template('index.html', result_text = str(result))'''

@app.route("/api/math_func", methods = ['POST'])
def process_json():
  st = time.time()
  with open('input_data.json', 'r') as json_file :
    json_data = json.load(json_file)
    id = int(json_data["id"])
    x = int(json_data["file"]["matrixSize"])
    n = int(json_data["file"]["seed"])
    np.random.seed(n)
    array1 = np.random.randint(n, size = (x, x))
    arrayT = array1.transpose()
    trace_val = int(np.trace(array1.dot(arrayT)))
    et = time.time()
    elapsed_time = et-st

    output_dict = {
      "id" : str(id),
      "result" : str(trace_val),
      "processing_time" : str(elapsed_time)
    }
    
    return jsonify(output_dict)
  
  
if __name__ == '__main__':
  app.run(host='0.0.0.0',debug=True, threaded=True)