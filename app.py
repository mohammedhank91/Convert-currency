from flask import Flask, render_template, request

app = Flask(__name__,template_folder='template')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    result = 0
    currency_from = request.form['currency_from']
    currency_to = request.form['currency_to']
    amount = request.form['amount']

    # Perform currency conversion calculation here

    # Return the result as a string
    return str(result)

if __name__ == '__main__':
    app.run(debug=True)
