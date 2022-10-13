from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import stories_collection

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

@app.get('/')
def show_landing_page():
    """Shows drop down menu to select madlib story"""

    stories = stories_collection.keys()

    return render_template("landing_page.html", stories = stories)


@app.get('/questionnaire')
def show_question_page():
    """Shows form to begin playing madlibs"""
    story_name = request.args.get('menu_select')
    story_instance = stories_collection.get(story_name)
    prompts = story_instance.prompts

    return render_template(
        "questions.html",
        prompts = prompts,
        story_name = story_name
        )


@app.get('/results')
def show_answer_page():
    ''' Read form inputs, generate new story on page'''
    story_name = request.args.get("story_name")
    story_instance = stories_collection.get(story_name)
    results = story_instance.generate(request.args)

    return render_template('results.html', results = results)
