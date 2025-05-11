from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form['email']
        organization = request.form['organization']
        plan = request.form['plan']
        # Save user details to the database
        # ...
        return redirect(url_for('dashboard'))
    return render_template('signup.html')

@app.route('/dashboard')
def dashboard():
    # Render dashboard with a tour for first-time users
    return render_template('dashboard.html', first_time=True) 