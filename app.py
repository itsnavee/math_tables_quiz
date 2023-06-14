from flask import Flask, render_template, request
import random

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        param1_min = int(request.form.get('param1_min', 2))
        param1_max = int(request.form.get('param1_max', 4))
        param2_min = int(request.form.get('param2_min', 2))
        param2_max = int(request.form.get('param2_max', 10))
        num_questions = int(request.form.get('num_questions', 128))

        questions = generate_quiz_questions(
            param1_min, param1_max, param2_min, param2_max, num_questions)

        return render_template('index.html', questions=questions,
                               param1_min=param1_min, param1_max=param1_max,
                               param2_min=param2_min, param2_max=param2_max,
                               num_questions=num_questions)

    return render_template('index.html', param1_min=2, param1_max=4, param2_min=2, param2_max=10, num_questions=128)


def generate_quiz_questions(param1_min, param1_max, param2_min, param2_max, num_questions):
    questions = []

    for _ in range(num_questions):
        param1 = random.randint(param1_min, param1_max)
        param2 = random.randint(param2_min, param2_max)
        result = param1 * param2
        questions.append(f"{param1} x {param2} = ")

    return questions


if __name__ == '__main__':
    app.run()
