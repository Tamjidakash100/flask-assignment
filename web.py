from flask import Flask, request

app = Flask(__name__)

@app.route('/cal/<int:num1>/<string:op>/<int:num2>')
def calculator(num1, op, num2):
    if op == '+':
        result = num1 + num2
    elif op == '-':
        result = num1 - num2
    elif op == '*':
        result = num1 * num2
    #slash is not supported in route
    elif op == 'div':
        result = num1 / num2
    elif op == '%':
        result = num1 % num2
    else:
        return 'Invalid operator'

    return f'The result is {result}'

if __name__ == '__main__':
    app.run(debug=True)
