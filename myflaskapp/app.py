from flask import Flask, render_template
import test

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

@app.route("/forward/", methods=['POST'])
def move_forward():
    #Moving forward code
    test.turnOn()
    forward_message = "Moving Forward..."
    return render_template('articles.html', message=forward_message);


if __name__ == '__main__':
   app.run(debug=True, host='0.0.0.0')
