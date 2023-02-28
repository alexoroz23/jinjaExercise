from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
from stories import story

app = Flask(__name__)
app.config['SECRET_KEY'] = "madlib"

debug = DebugToolbarExtension(app)


@app.route("/")
def ask_questions():
    """Generate and show form to ask words."""

    # Get the prompts from the `story` object
    prompts = story.prompts

    # Render the `mlquestions.html` template and pass in the prompts
    return render_template("mlquestions.html", prompts=prompts)


@app.route("/story")
def show_story():
    """Show story result."""

    # Generate the story text by calling the `generate` method of the `story` object and passing in the form data
    text = story.generate(request.args)

    # Render the `story.html` template and pass in the generated text
    return render_template("story.html", text=text)