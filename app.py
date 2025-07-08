import os
from flask import Flask, render_template, request, send_from_directory
from rembg import remove
from PIL import Image
from io import BytesIO

app = Flask(__name__)
UPLOAD_FOLDER = 'static/output'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        image = request.files["image"]
        if image:
            input_image = Image.open(image)
            output_image = remove(input_image)

            output_path = os.path.join(UPLOAD_FOLDER, "output.png")
            output_image.save(output_path)
            print(f"Image saved at: {output_path}")
            return render_template("index.html", result_image="output.png")

    return render_template("index.html", result_image=None)

@app.route("/static/output/<filename>")
def send_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)

if __name__ == "__main__":
    app.run(debug=True)