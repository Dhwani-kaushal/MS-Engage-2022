from flask import Flask, request , jsonify
from deepface import DeepFace
from flask_cors import CORS,cross_origin
import base64

app = Flask(__name__)

CORS(app)

def convert_and_save(b64_string):
    with open("../facedetect.jpg", "wb") as fh:
        fh.write(base64.decodebytes(b64_string.encode()))

@app.route("/")
def home_view():
		return "<h1>Welcome to Geeks for Geeks</h1>"


@app.route('/predict',methods=['POST'])
def predict():
	file=request.form['photo']
	convert_and_save(file)
    result=DeepFace.analyze('../facedetect.jpg',actions=['emotion'])
	emotion=result['dominant_emotion']
	data={
			"emotion":emotion
		}
	return jsonify(data)


