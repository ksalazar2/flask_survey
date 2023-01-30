from flask import Flask, request, render_template, redirect, flash
import surveys

app = Flask(__name__)
app.config['SECRET_KEY'] = 'plswork'

# list containing user answers
responses = []

@app.route('/')
def survey_start():
    """Generate survey instructions and start page."""

    title = surveys.satisfaction_survey.title
    instructions = surveys.satisfaction_survey.instructions

    return render_template('home_page.html', survey_title = title, survey_instructions = instructions)

@app.route('/questions/<int:qnum>')
def show_question(qnum):
    """Show current question."""
    
    title = surveys.satisfaction_survey.title
    if qnum != len(responses):
        next_question = '/questions/' + str(len(responses))
        flash("Please do not attempt to access invalid questions")
        return redirect (next_question)
    
    if len(responses) == len(surveys.satisfaction_survey.questions):
        flash("You have already completed the survey!")
        return redirect('/thankyou')
    
    question = surveys.satisfaction_survey.questions[qnum].question
    choices = surveys.satisfaction_survey.questions[qnum].choices
    if choices is None:
        choices = ['Yes', 'No']
    
    return render_template('question_page.html', survey_title = title, survey_question = question, survey_choices = choices)

@app.route('/answer', methods=['POST'])
def handle_answer():
    """Append answer to responses list and redirect user to next page."""
    answer = request.form['user_answer']
    responses.append(answer)
    num_ans = len(responses)
    if num_ans < len(surveys.satisfaction_survey.questions):
        next_question = '/questions/' + str(num_ans)
        return redirect(next_question)
    return redirect('/thankyou')

@app.route('/thankyou')
def show_thanks():
    """Show Thank You Page."""
    title = 'Thank you!'

    return render_template('thank_you.html', title = title)