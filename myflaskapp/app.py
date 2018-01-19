from flask import Flask, render_template
import test
import drive
app = Flask(__name__)

@app.route('/')

def index():
   return render_template('home.html')

@app.route('/about')

def about():
    return render_template('about.html')

@app.route('/articles')
def articles():
    return render_template('articles.html')

@app.route("/backward/", methods=['POST'])
def move_forward():
    #Moving forward code
    #test.turnOn()
    #forward_message = "Moving Forward..."
    drive.moveForward()
    #return render_template('articles.html', message=forward_message)
    return ('', 204)

@app.route("/forward/", methods=['POST'])
def move_backwards():
    drive.moveBackward()
    return('', 204)

@app.route("/left/", methods=['POST'])
def move_left():
    drive.moveLeft()
    return('', 204)

@app.route("/right/", methods=['POST'])
def move_right():
    drive.moveRight()
    return('', 204)



if __name__ == '__main__':
   app.run(debug=True, host='0.0.0.0')
