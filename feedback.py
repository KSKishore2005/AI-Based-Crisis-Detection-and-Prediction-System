@app.route('/feedback', methods=['POST'])
def feedback():
    user_feedback = request.form['feedback']
    # Save feedback to the database
    # ...
    return redirect(url_for('dashboard')) 