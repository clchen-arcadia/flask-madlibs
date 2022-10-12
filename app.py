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

    return render_template("questions.html", prompts = prompts)


@app.get('/story')
def answer_page():
    ''' Read form inputs, generate new story on page'''
    answers = {}

    for word in silly_story.prompts:

        answers[word] = request.args.get(word)

    results = silly_story.generate(answers)

    return render_template('results.html', results = results)













