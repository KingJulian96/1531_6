from server import app, valid_time
from flask import request, render_template
from Calculator import Calculator

def right_time(time):
    if time == None:
        return 0
    return 1

@app.route('/', methods=['POST', 'GET'])
def interest_total():
    if request.method == 'POST':
        time = float(request.form.get('time'))
        initial = float(request.form.get('invested'))
        rate = float(request.form.get('rate'))
        calc = Calculator(initial, rate)
        total = calc.total_interest(time)
        
        return render_template('interest_form.html', calc_total=True, total = total)
    return render_template('interest_form.html', calc_total=True)

@app.route('/time', methods=['POST', 'GET'])
def time_interest():
    if request.method == 'POST':
        initial = float(request.form.get('invested'))
        rate = float(request.form.get('rate'))
        calc = Calculator(initial, rate)
        total = float(request.form.get('total'))
        time = calc.time_required(total)
        
        return render_template('interest_form.html', calc_time=True, calc_total=False, time=time)
    return render_template('interest_form.html', calc_time = True,calc_total=False,)

@app.route('/credits', methods=['GET'])
def credits():
    return render_template('credits.html', name='Julian')
