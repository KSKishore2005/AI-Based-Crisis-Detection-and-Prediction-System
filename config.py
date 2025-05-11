from flask import Flask

# Create the Flask app instance
app = Flask(__name__)

TWITTER_API_KEY="rmWPRjP5TFcOdy72PjALeaT5Y"
TWITTER_API_SECRET_KEY="5Hu0olanqmJhiCFhvXuWwc3rqRMAlTKqKjlh8gZ6uDtKqSvYQP"
TWITTER_ACCESS_TOKEN="1895391824577282048-Ol45b5TR0Pvn82m3SxE7h5ZQdavHDv"
TWITTER_ACCESS_TOKEN_SECRET="D2KvSawJrMaP9Yh21zaq1QjUX5B4oPkRjHicMDfCMYGVY"

@app.route('/configure_monitoring', methods=['GET', 'POST'])
def configure_monitoring():
    if request.method == 'POST':
        region = request.form['region']
        data_sources = request.form.getlist('data_sources')
        thresholds = request.form['thresholds']
        # Save configuration to the database
        # ...
        return redirect(url_for('dashboard'))
    return render_template('configure_monitoring.html')