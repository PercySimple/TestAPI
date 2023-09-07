from flask import Flask, request, jsonify
import numpy as np
import time
import logging.config

# Configure the logging package from the logging ini file
logging.config.fileConfig('logging.ini', disable_existing_loggers=False)

# Get a logger for our module
log = logging.getLogger(__name__)

app = Flask(__name__)

@app.route("/math_func", methods = ['POST'])
def process_json():
  log.debug(f"POST /math_func")
  st = time.time()

  try:
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
      json_data = request.get_json()
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
      return jsonify(output_dict), 201
    log.warning(f"POST /math_func: Content-Type not supported.")
    return f"Content-Type not supported!", 400
  except LookupError:
    log.exception(f"An exception occurred while posting the request. Please enter the correct key and/or index.")
    return f"An exception occurred while posting the request. Please enter the correct key and/or index.", 400

  

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True, threaded=True)