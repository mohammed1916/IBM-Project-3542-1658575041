from flask import Flask, render_template, request

import make_prediction

app = Flask(__name__)


@app.route('/', methods=['GET'])
def main():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def predict():
    imageFile = request.files['imagefile']
    imgPath = "./images/sample.png"
    imageFile.save(imgPath)
    pred = make_prediction.predict()
    pred = "The digitalised output is"+pred
    return render_template('index.html', pred=pred)


if __name__ == "__main__":
    app.run()
