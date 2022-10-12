from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import silly_story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

@app.get('/')
def landing_page():
    """Shows form to begin playing madlibs"""

    prompts = silly_story.prompts

    prompts = [word.replace("_", " ") for word in prompts]

    return render_template("questions.html", prompts = prompts)


@app.get('/story')
def answer_page():
    for item in silly_story.generate(answer):
        request.args.get()
