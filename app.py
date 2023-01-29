from flask import Flask,render_template,request,redirect
from werkzeug.utils import secure_filename
from face_detection import detectFaces
import os
from water_art import waterArtMaker
from remove_noise import remove_Noise
from edgesDetection import getEdges
from autoColorCorrection import correctColor
# Initializing App
app=Flask(__name__)
app.config['UPLOAD_FOLDER']='static/uploads'
app.secret_key=os.urandom(24)
photo_id=0
# Defualt Route
@app.route("/",methods=["GET","POST"])
def home_page():
    return render_template("index.html")

@app.route("/editor",methods=["GET","POST"])
def editorView():
    return render_template("normal.html")

@app.route("/editorai",methods=["GET","POST"])
def editorAIView():
    return render_template("AI.html",imgPath="../static/imgs/image-placeholder.png")

@app.route("/faceDetection",methods=["GET","POST"])
def faceDetection():
    if request.method=="POST":
        f=request.files['upload_file']
        photo_id=len(os.listdir(app.config['UPLOAD_FOLDER']))+1
        img_path=os.path.join(app.config['UPLOAD_FOLDER'],f"{photo_id}_"+secure_filename(f.filename))
        f.save(img_path)
        modified=detectFaces(img_path)
        return render_template("test.html",img_path=img_path)
    return render_template("index.html")

@app.route("/applyFilter",methods=["GET","POST"])
def applyImgFilter():
    if request.method=="POST":
        filter=""
        f=request.files['upload_file']
        filter=request.form.get('Selected Filter')
        photo_id=len(os.listdir(app.config['UPLOAD_FOLDER']))+1
        img_path=os.path.join(app.config['UPLOAD_FOLDER'],f"{photo_id}_"+secure_filename(f.filename))
        f.save(img_path)
        modified=waterArtMaker(img_path)
        if filter=="Auto Adjust":
            correctColor(img_path)
            filter=""
            return render_template("AI.html",imgPath=img_path)
        elif filter=="Detect Faces":
            detectFaces(img_path)
            filter=""
            return render_template("AI.html",imgPath=img_path)
        elif filter=="Noise Remover":
            remove_Noise(img_path)
            filter=""
            return render_template("AI.html",imgPath=img_path)
        elif filter=="AI water-filter":
            waterArtMaker(img_path)
            filter=""
            return render_template("AI.html",imgPath=img_path)
        elif filter=="Detect Edges":
            getEdges(imgPath=img_path)
            filter=""
            return render_template("AI.html",imgPath=img_path)

    return render_template("index.html")
if __name__=="__main__":
    app.run(debug=True)