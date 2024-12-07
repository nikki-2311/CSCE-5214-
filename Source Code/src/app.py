from flask import Flask, render_template, request, jsonify
import os
import time
from detect import main
# import detect
# from flask_ngrok import run_with_ngrok

app = Flask(__name__)
# run_with_ngrok(app)

# Directory where images will be saved
SAVE_DIR = r"C:\Users\sahit\Desktop\SDAI\SimpleHTR-master\SimpleHTR-master\data"

@app.route('/', methods=['GET'])
def index():
    
    return render_template('index.html', predicted_text=None)

@app.route('/', methods=['POST'])
def detect():
    imageFile = request.files['image']
    original_filename = imageFile.filename
    safe_filename = os.path.basename(original_filename)
    file_extension = os.path.splitext(safe_filename)[1]
    new_filename = f"{os.path.splitext(safe_filename)[0]}_{int(time.time())}{file_extension}"
    image_path = os.path.join(SAVE_DIR, new_filename)
    imageFile.save(image_path)
    print(image_path)
    
    classification = main(image_path)
    print(classification)

    # Return the prediction directly for AJAX
    return jsonify(predicted_text=classification)

if __name__ == '__main__':
    app.run(port=3000, debug=False)
