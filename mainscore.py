from utils import get_score

from flask import Flask, render_template_string

app = Flask(__name__)


html_template = """
<!DOCTYPE html>
<html>
<head>
    <title>Score Page</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f5f5f5;
            text-align: center;
        }

        h1 {
            color: #333;
        }

        p {
            font-size: 24px;
            color: #007bff;
        }

        form {
            margin-top: 20px;
        }

        input[type="submit"] {
            background-color: #007bff;
            color: #fff;
            padding: 10px 20px;
            font-size: 18px;
            border: none;
            cursor: pointer;
        }

        input[type="submit"]:hover {
            background-color: #0056b3;
        }
    </style>
</head>
<body>
    <h1>Score Page</h1>

    <!-- Display the current score -->
    <p>Score: {{ score }}</p>

    <!-- Form with a refresh button -->
    <form method="POST" action="/refresh">
        <input type="submit" value="Refresh Score">
    </form>
</body>
</html>
"""


@app.route('/')
def show_score():
    if type(get_score()) == str:
        return render_template_string(html_template, score=get_score())
    elif type(get_score()) == int:
        return render_template_string(html_template, score='Error - Could not find "score.txt" file')


@app.route('/refresh', methods=['POST'])
def refresh_score():
    return show_score()


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5050)
