from flask import Flask, render_template, request, redirect
import re

app = Flask(__name__)

# Global variable to store user data
users = {}

# Config file path
config_file_path = '/etc/freeradius/3.0/users'

# Read the config file
def read_config_file():
    global users
    users = {}
    with open(config_file_path, 'r') as file:
        file_contents = file.read()

    # Extract usernames and passwords using regex
    pattern = r'^(\w+)\s+Cleartext-Password\s:=\s"(\w+)"$'
    matches = re.findall(pattern, file_contents, re.MULTILINE)

    # Populate the users dictionary
    for match in matches:
        username, password = match
        users[username] = password

# Save the generated file contents to the config file
def save_to_config_file(file_contents):
    with open(config_file_path, 'w') as file:
        file.write(file_contents)

# Home page with the user table
@app.route('/')
def home():
    return render_template('index.html', users=users)

# Add a new user
@app.route('/add', methods=['POST'])
def add_user():
    username = request.form['username']
    password = request.form['password']
    users[username] = password
    return redirect('/')

# Delete a user
@app.route('/delete/<username>', methods=['GET'])
def delete_user(username):
    if username in users:
        del users[username]
    return redirect('/')

# Generate the file with user credentials and save it
@app.route('/generate-file', methods=['GET'])
def generate_file():
    file_contents = ''
    for username, password in users.items():
        file_contents += f'{username} Cleartext-Password := "{password}"\n'
        
    file_contents += '\nDEFAULT Framed-Protocol == PPP\n'
    file_contents += '        Framed-Protocol = PPP,\n'
    file_contents += '        Framed-Compression = Van-Jacobson-TCP-IP\n\n'
    file_contents += '\nDEFAULT Hint == "CSLIP"\n'
    file_contents += '        Framed-Protocol = SLIP,\n'
    file_contents += '        Framed-Compression = Van-Jacobson-TCP-IP\n\n'
    file_contents += 'DEFAULT Hint == "SLIP"\n'
    file_contents += '        Framed-Protocol = SLIP\n'

    # Save the file contents to the config file
    save_to_config_file(file_contents)

    return redirect('/')

if __name__ == '__main__':
    read_config_file()
    app.run(host="0.0.0.0", port=8888, debug=True)
