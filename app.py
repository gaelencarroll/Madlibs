from flask import Flask, request, render_template
from stories import story
from flask_debugtoolbar import DebugToolbarExtension


app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"
debug = DebugToolbarExtension(app)

@app.route('/')
def homepage():
    prompts = story.prompts
    return render_template('base.html',prompts=prompts)

@app.route('/story')
def story_page():
    text = story.generate(request.args)
    return render_template('story.html',text=text)


