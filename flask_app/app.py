from flask import Flask, request, render_template_string

app = Flask(__name__)

# Home route - Hello World
@app.route('/')
def home():
    return '<h1>Hello, World!</h1>'

# Route for form
@app.route('/greet', methods=['GET', 'POST'])
def greet():
    form_html = '''
    <form method="post">
        Name: <input type="text" name="name"><br><br>
        Age: <input type="text" name="age"><br><br>
        <input type="submit" value="Submit">
    </form>
    '''
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        age = request.form.get('age', '').strip()

        # Basic error handling
        if not name:
            return form_html + '<p style="color:red;">Error: Name cannot be empty.</p>'
        if not age.isdigit():
            return form_html + '<p style="color:red;">Error: Age must be a number.</p>'

        return f'<h2>Hello {name}, you are {age} years old!</h2>'

    return form_html

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050, debug=True)


