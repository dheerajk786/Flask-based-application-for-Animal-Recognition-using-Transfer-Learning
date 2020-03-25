
from flask import Flask,render_template,request,redirect,send_file,send_from_directory
import os
from werkzeug.utils import secure_filename
from scripts.label_image import predict

UPLOAD_FOLDER = 'static/data'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

fname=""

@app.route('/',methods=['GET','POST'])  #it is decorator
def uploadpredict():
   if request.method == 'POST':
         print("yeah")
         print("Button press=",request.form['action'])

# check if the post request has the file part
         if 'file' not in request.files:
            # flash('No file part')
            print("No file part")
            return redirect(request.url)
         file = request.files['file']
        # if user does not select file, browser alsode
        # submit a empty part without filename
         if file.filename == '':
            # flash('No selected file')
            print("No selected file")
            return redirect(request.url)
         if file :
            filenames = secure_filename(file.filename)
            print(os.path.exists(os.path.join(app.config['UPLOAD_FOLDER'], filenames)))
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filenames))
            des=os.path.join(app.config['UPLOAD_FOLDER'], filenames)
            result=predict(des)
            tresult,lresult={},{}
            count=0
            for i in result.keys():
               if count==0:
                  tresult[i]=result[i]
               else:
                  lresult[i]=result[i]
               count=+1
            print(tresult)
            print(lresult)
            return render_template("animal_prediction.html",image=des,result1=tresult,result2=lresult)
   return render_template("animal_prediction.html")


if __name__=="__main__":    #cmds to run flask
   app.run(port=8000,debug=True)