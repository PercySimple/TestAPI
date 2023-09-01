import numpy as np
import time

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/api/math_func", methods = ['POST'])
def process_json():
  st = time.time()
  content_type = request.headers.get('Content-Type')
  if (content_type == 'application/json'):
    json_data = request.json
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
  else:
    return 'Content-Type not supported!'
  
  
if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True, threaded=True)