@app.route('/download_report')
def download_report():
    # Logic to generate and download reports
    return send_file('report.pdf', as_attachment=True) 