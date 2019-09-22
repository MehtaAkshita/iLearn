from flask import Flask, render_template,request
from string import Template
app = Flask(__name__)

# APP_ROOT=os.path.dirname(os.path.abspath(__file__))

yurl={
	'youtube_link':'https://www.youtube.com/embed/UQKNdwiSNOc'
}

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html',yurl=yurl)
    # return """ 
    # <iframe src="https://www.youtube.com/embed/UQKNdwiSNOc" width="800" height="480" frameborder="0"></iframe>
    # """

# @app.route('/', methods=["POST","GET"])
# def y_id():
# 	y_id = request.form.get('upload')
# 	print(y_id)

@app.route('/', methods=["POST"])
def some_function():
    text = request.form.get('upload')
    print(text)
    return render_template('index.html')


# def contact():
#     if request.method == 'POST':
        # if (request.form['upload_btn']):
        #     pass # do something
        # if (request.form['search_btn']):
        #     speechtotext.myfunction()
        # elif (request.form['play_btn']):
        #     pass # do something else
    #     else:
    #         pass # unknown
    # elif request.method == 'GET':
    #     return render_template('index.html', form=form)



# @app.route('/upload/', methods=['GET', 'POST'])
# def upload_file():
#     if request.method == 'POST':
#         f = request.files['the_file']
#         f.save('/var/www/uploads/uploaded_file.txt')

# @app.route('/videos/<vid>')
# def videos(vid):    


# @app.route("/upload/",methods=['POST'])
# def upload(id):
# 	upload=

# def videos(vid):
# 	vidtemplate = Template("""
# 		<h2>
#         YouTube video link: 
#         <a href="https://www.youtube.com/watch?v=${youtube_id}">
#           ${youtube_id}
#         </a>
#       </h2>


#       <iframe src="https://www.youtube.com/embed/${youtube_id}" width="853" height="480" frameborder="0">
# 		""")    

# 	return vidtemplate.substitute(youtube_id=vid)


if __name__ == '__main__':
    app.run(debug=True,use_reloader=True,threaded=True)