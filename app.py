# Importing Necessary packages
from flask import Flask,render_template, request, jsonify
import numpy as np
from fastai.vision.all import *
from fastbook import load_learner
import pickle 
import os
import io
import PIL
from PIL import Image
from fastai.vision.core import PILImage
import pathlib
from torchvision import transforms
temp = pathlib.PosixPath
pathlib.PosixPath = pathlib.WindowsPath

# setting working dir
cwd = os.getcwd()
path= cwd + '/model/model-resnet18.pkl'
assert os.path.isfile(path)

# Initialiazing flask app
app = Flask(__name__)

# Loading the saved model
model = load_learner(path, 'model-resnet18.pkl')

@app.route('/')
def index():
    return render_template('index.html',)

@app.route('/upload', methods=["POST"])
def upload():
    # try:
        # Getting img from POST
        file = request.files['user-img']
        # Resizing img to 224 X 224 , This is the size on which model was trained
        # Prediction using model
        prediction = model.predict(PILImage.create(file))[0]
        # Getting Prediction ready to sent it to frontend
        response = {"result": str(prediction)}
        return jsonify(response)

    # except:
    #     return jsonify({'result': "Sorry, Something Went Wrong !"})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
