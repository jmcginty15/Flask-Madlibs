from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import Story

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yeet'
debug = DebugToolbarExtension(app)

prompts = ['place', 'noun', 'verb', 'adjective', 'plural_noun']
template = """Once upon a time in a long-ago {place}, there lived a large
{adjective} {noun}. It loved to {verb} {plural_noun}."""
story = Story(prompts, template)

@app.route('/')
def form():
    return render_template('form.html', prompts=story.prompts)

@app.route('/story')
def homepage():
    inputs = request.args
    story_output = story.generate(inputs)
    return render_template('story.html', story=story_output)