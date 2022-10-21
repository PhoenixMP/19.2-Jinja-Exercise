
from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension

from stories import *


app = Flask(__name__)
app.config['SECRET_KEY'] = "oh-so-secret"
debug = DebugToolbarExtension(app)


answers = {}
words = None
story = None


@app.route('/')
def choose_story():
    return render_template("choose.html", story1=story1.template, story2=story2.template, story3=story3.template)


@app.route('/form')  # this is a decorator
def madlib_form():
    global story, words
    story = globals()[request.args.get('story')]
    words = story.prompts
    return render_template("form.html", words=words, story=story)


@app.route('/story')
def madlib_story():
    for word in words:
        answers[F'{word}'] = request.args[f"{word}"]
    text = story.generate(answers)
    return render_template("story.html", text=text)
