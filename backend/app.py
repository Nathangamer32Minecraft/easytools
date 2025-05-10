from flask import Flask, request, send_file
import os
import subprocess

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
OUTPUT_FOLDER = "output"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

@app.route("/upload", methods=["POST"])
def upload_file():
    file = request.files["file"]
    if not file.filename.endswith(".class"):
        return "Only .class files are supported", 400

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    output_path = os.path.join(OUTPUT_FOLDER, file.filename + ".java")
    file.save(file_path)

    # Décompilation avec CFR
    subprocess.run([
        "java", "-jar", "decompiler/cfr.jar", file_path,
        "--outputdir", OUTPUT_FOLDER
    ])

    return send_file(output_path, as_attachment=False)

if __name__ == "__main__":
    app.run(debug=True)
