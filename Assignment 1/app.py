from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "secret_event_key"

# Sample Data for Task 2
events_list = [
    {"id": 1, "name": "Tech Summit 2026", "date": "May 15, 2026", "venue": "Convention Center", "desc": "Exploring the future of AI and Robotics."},
    {"id": 2, "name": "Music Fest", "date": "June 10, 2026", "venue": "City Park", "desc": "A night of jazz, blues, and rock and roll."},
    {"id": 3, "name": "Art Expo", "date": "July 05, 2026", "venue": "National Gallery", "desc": "Showcasing modern digital masterpieces."},
    {"id": 4, "name": "Code Sprint", "date": "August 20, 2026", "venue": "IT Hub", "desc": "24-hour hackathon for student developers."}
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/events')
def event_list():
    return render_template('events.html', events=events_list)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Task 4: Handling Form Submission
        flash(f"Successfully registered for {request.form.get('event_choice')}!")
        return redirect(url_for('index'))
    return render_template('register.html', events=events_list)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False) # use_reloader=False stops the looping error you had