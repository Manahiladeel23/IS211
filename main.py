from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)

app.secret_key="this is my secret key"
# List to store To Do items
todo_list = []

# Route to render main page and display To Do items
@app.route('/')
def show_todo_list():
    return render_template('todo_list.html', todo_list=todo_list)


# Route to handle form submission for adding new To Do items
@app.route('/submit', methods=['POST'])
def submit_todo_item():
    task = request.form['task']
    email = request.form['email']
    priority = request.form['priority']

    # Data validation
    if not email or '@' not in email:
        flash(message="email is not valid")
        return redirect(url_for('show_todo_list'))

    if priority not in ['Low', 'Medium', 'High']:
        flash(message="email is not valid")

        return redirect(url_for('show_todo_list'))

    # Add new To Do item to the list
    todo_list.append({'task': task, 'email': email, 'priority': priority})

    return redirect(url_for('show_todo_list'))

# Route to clear the list of To Do items
@app.route('/clear', methods=['POST'])
def clear_todo_list():
    todo_list.clear()
    return redirect(url_for('show_todo_list'))

if __name__ == '__main__':
    app.run(debug=True)



