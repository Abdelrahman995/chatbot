from flask import Flask, render_template, request
from flask import jsonify
import io
import numpy as np
import json
import ast
import sys

app = Flask(__name__)
@app.route('/', methods=[ 'POST'])
def upload():
    if request.method == 'POST' :
        try :
            print (request.headers)
            data = str(request.data.decode('utf-8'))
            data = json.loads(data)
            header = str(request.headers['Token'])
            if (header!="kdjsdskacvbbc217vpewe"):
                return jsonify({"error":"Invalid Token"})
            if data is None:
                return "Please enter valid data"

            else:
                print (cv2.imread("b.jpg", 0).shape , np.array(data["image1"]).shape)
                emotion, confidence=Emotion_detector.main(np.array(data["image1"],dtype='uint8'))
                return jsonify({"emotion":str(emotion) , "confidence":str(confidence)})

        except Exception as e:
            error = traceback.format_exc()
            return jsonify({"error":str(error)})

if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0')
