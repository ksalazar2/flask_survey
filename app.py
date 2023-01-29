from flask import Flask, request, render_template, redirect, flash
import surveys

app = Flask(__name__)

# list containing user answers
responses = []

@app.route('/')
def survey_start():
    """Generate survey instructions and start page."""

    title = surveys.satisfaction_survey.title
    instructions = surveys.satisfaction_survey.instructions

    return render_template('home_page.html', survey_title = title, survey_instructions = instructions)