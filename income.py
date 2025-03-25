from flask import Flask, render_template

app = Flask(__name__, template_folder='/home/student/griffitb/public_html/csci375/templates')

@app.route('/~griffitb/csci375/income')
def income():
    # Example data for columns and rows
    columns = ['ID', 'Name', 'Amount']
    rows = [
        [1, 'John Doe', 5000],
        [2, 'Jane Smith', 6000],
        [3, 'Jim Brown', 5500]
    ]
    
    return render_template('welcome_flask.html', columns=columns, rows=rows)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
