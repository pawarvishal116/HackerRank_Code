from flask import Flask     #This imports the Flask class from the Flask package.

app = Flask(__name__)       #This creates your Flask application and stores it in the variable app.

@app.route('/')             #When someone visits /, execute the function below it.
def home():                 #Flask sees / and calls home().
    return 'Hello, Data Scientist!'

if __name__ == '__main__':  #Flask uses __name__ to understand where your application is located so it can find related resources.
    app.run(debug=True)     #This starts the Flask development server.

#debug=True is useful while developing because Flask provides debugging information when your code has an error, and typically reloads the application when your Python code changes.
