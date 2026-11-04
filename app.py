from flask import Flask, render_template, request, redirect, make_response

app = Flask(__name__)

FLAG = "CURSOR{c00k13_m0nst3r_4dm1n_4cc3ss}"

@app.route('/')
def index():
    return redirect('/login')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        login_type = request.form.get('type')

        if login_type == 'admin':
            username = request.form.get('username', '')
            password = request.form.get('password', '')
            if username and password:
                return render_template('login.html', error=True)
            return render_template('login.html', error=False, field_error=True)

        if login_type == 'guest':
            resp = make_response(redirect('/dashboard'))
            resp.set_cookie('role', 'guest')
            return resp

    return render_template('login.html', error=False)

@app.route('/dashboard')
def dashboard():
    role = request.cookies.get('role')
    if role == 'admin':
        return render_template('dashboard.html', flag=FLAG, is_admin=True, page='dashboard')
    elif role == 'guest':
        return render_template('dashboard.html', flag=None, is_admin=False, page='dashboard')
    return redirect('/login')

@app.route('/users')
def users():
    role = request.cookies.get('role')
    if role == 'admin':
        return render_template('dashboard.html', flag=FLAG, is_admin=True, page='users')
    elif role == 'guest':
        return render_template('dashboard.html', flag=None, is_admin=False, page='users')
    return redirect('/login')

@app.route('/settings')
def settings():
    role = request.cookies.get('role')
    if role == 'admin':
        return render_template('dashboard.html', flag=FLAG, is_admin=True, page='settings')
    elif role == 'guest':
        return render_template('dashboard.html', flag=None, is_admin=False, page='settings')
    return redirect('/login')

@app.route('/logout')
def logout():
    resp = make_response(redirect('/login'))
    resp.delete_cookie('role')
    return resp

if __name__ == '__main__':
    app.run(debug=False)