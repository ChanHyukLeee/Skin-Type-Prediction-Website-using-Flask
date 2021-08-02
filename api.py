import os
from flask import Flask
from flask import request
from flask import render_template
from flask import jsonify
from torch_utils import transform_image, prediction

UPLOAD_FOLDER = 'D:\learn_flask\Practice_Flask\static'
ALLOWED_FILE = ['jpg', 'png', 'jpeg' ]

app = Flask(__name__)

@app.route("/", methods = ["GET", "POST"])
def upload_predict():
    if request.method == "POST":
        image_file = request.files["image"]
        if image_file is None or image_file.filename =="":
            return jsonify({'error': 'no file'})
        if not ALLOWED_FILE(image_file.filename):
            return jsonify({'error': 'format not supported'})
        if image_file:
            image_location = os.path.join(
                UPLOAD_FOLDER, image_file.filename
            )
            image_file.save(image_location)
            img_bytes = image_file.read()
            img_tensor = transform_image(img_bytes)
            pred = prediction(img_tensor)
            
            return render_template("index.html", prediction=pred, image_loc = image_file.filename)
    pred = ""
    return render_template("index.html", prediction=pred, image_file = None)

if __name__ == "__main__":
    app.run(port=1200, debug=True)