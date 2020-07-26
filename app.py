from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import Story

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yeet'
debug = DebugToolbarExtension(app)

prompts = {0: ['place', 'noun', 'verb', 'adjective', 'plural_noun'],
1: ['person', 'noun_1', 'noun_2', 'noun_3', 'noun_4', 'verb', 'superlative_adjective', 'female_person', 'body_part_1', 'body_part_2', 'body_part_3'],
2: ['person', 'body_part', 'liquid', 'substance']}

display_prompts = {0: {'place': 'Place', 'noun': 'Noun', 'verb': 'Verb', 'adjective': 'Adjective', 'plural_noun': 'Plural noun'},
1: {'person': 'Person', 'noun_1': 'Noun 1', 'noun_2': 'Noun 2', 'noun_3': 'Noun 3', 'noun_4': 'Noun 4', 'verb': 'Verb', 'superlative_adjective': 'Superlative adjective', 'female_person': 'Female person', 'body_part_1': 'Body part 1', 'body_part_2': 'Body part 2', 'body_part_3': 'Body part 3'},
2: {'person': 'Person', 'body_part': 'Body part', 'liquid': 'Liquid', 'substance': 'Substance'}}

templates = {0: """Once upon a time in a long-ago {place}, there lived a large
{adjective} {noun}. It loved to {verb} {plural_noun}.""",
1: """{person} once told me the {noun_1} is gonna {verb} me
I ain't the {superlative_adjective} {noun_2} in the {noun_3}
{female_person} was looking kind of dumb with her {body_part_1} and her {body_part_2}
In the shape of a(n) {noun_4} on her {body_part_3}""",
2: """{person} is sick with the {body_part} flu.
Drink more {liquid} and take {substance} as needed."""
}

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/form')
def form():
    story_index = int(request.args['story'])
    global story
    story = Story(prompts[story_index], templates[story_index])
    return render_template('form.html', prompts=story.prompts, display_prompts=display_prompts[story_index])

@app.route('/story')
def homepage():
    inputs = request.args
    story_output = story.generate(inputs)
    return render_template('story.html', story=story_output)