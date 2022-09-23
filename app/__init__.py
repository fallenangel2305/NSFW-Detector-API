import os
from nudenet import NudeDetector,NudeClassifier
from flask import Flask, request, jsonify

app = Flask(__name__)
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
    print("Testing")
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
                is_nude.append( classifier.classify(path))
                
                    

            # Removing the temporary file
            os.unlink(path)

        # If the file doesn't pass mimetype checks
        else:
            pass

    return jsonify(is_nude)

if __name__ == "__main__":
    app.run()
