import os
from nudenet import NudeDetector,NudeClassifier
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"*": {"origins": "*"}})
detector = NudeDetector()
classifier = NudeClassifier()
app.config["UPLOAD_FOLDER"] = "./upload"
@app.route("/", methods=["GET"])
def HelloWorld():
    return "<p>Hello world<p/>"
# The main route for analyzing the images/videos
@app.route("/analyze", methods=["POST"])
def AnalyzeImage():
    # For tracking media validity
    valid = True

    # Looping through each field in the request
    for field in request.files:
        file = request.files.get(field)
        type = file.mimetype.split("/")
        mime = type[0]

        if mime == "video" or mime == "image":
            # Temporarily storing the file in a local folder
            path = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
            file.save(path)

            if mime == "video":
                is_nude = detector.detect_video(path, mode="fast")
                if is_nude.get("preds") != {}:
                    valid = False

            elif mime == "image":
                is_nude = detector.detect(path, mode="fast")
                if len(is_nude) > 0:
                    valid = False

            # Removing the temporary file
            os.unlink(path)

        # If the file doesn't pass mimetype checks
        else:
            pass

    return jsonify(["is_safe",valid])
@app.route("/detect", methods=["POST"])
def ClassifyImage():
    print("Checking image ...")
    # For tracking media validity
    is_nude = []

    # Looping through each field in the request
    
    for field in request.files:
        file = request.files.get(field)
       
        type = file.mimetype.split("/")
        mime = type[0]

        if mime == "image":
            # Temporarily storing the file in a local folder
            path = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
            file.save(path)

            if mime == "image":
                is_nude = classifier.classify(path)
                print(is_nude.get(path))
                    

            # Removing the temporary file
            os.unlink(path)

        # If the file doesn't pass mimetype checks
        else:
            pass
   
    return is_nude.get(path)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000,debug=True,use_reloader=True)
