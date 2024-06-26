
# Import necessary modules
from flask import Flask, render_template, request, redirect, url_for

# Create a Flask application
app = Flask(__name__)

# Define the home route
@app.route('/')
def home():
    """Render the home page."""
    return render_template('index.html')

# Define the lessons route
@app.route('/lessons')
def lessons():
    """Render the lessons page."""
    return render_template('lessons.html')

# Define the lesson route
@app.route('/lesson/<lesson_id>')
def lesson(lesson_id):
    """Render an individual lesson page."""
    return render_template('lesson.html', lesson_id=lesson_id)

# Define the grammar route
@app.route('/grammar')
def grammar():
    """Render the grammar page."""
    return render_template('grammar.html')

# Define the exercises route
@app.route('/exercises')
def exercises():
    """Render the exercises page."""
    return render_template('exercises.html')

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
