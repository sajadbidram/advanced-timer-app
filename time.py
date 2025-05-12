from flask import Flask, render_template, request
import time

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('upload_form.html', timer=None)

@app.route('/set_timer', methods=['POST'])
def set_timer():
    time_value = int(request.form['time_value'])
    time_unit = request.form['time_unit']

    # تبدیل زمان به ثانیه
    if time_unit == 'minutes':
        total_seconds = time_value * 60
    elif time_unit == 'hours':
        total_seconds = time_value * 3600
    else:  # ثانیه
        total_seconds = time_value

    # نمایش تایمر در صفحه
    return render_template('upload_form.html', timer=total_seconds)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
