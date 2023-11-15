from flask import Flask
"""
Setting up Flask Server:
Instantiate Object that will serve as the access point to config the server
"""
# Assign to file that will run the server when file executes
app = Flask(__name__)
# Define the home route that populates. 
# The app decorator in combo w/ the view function sends results to front-end
@app.route("/", methods=["GET"])
# Define the view function (usually home, index, or root)
def home():
    return "Hello, world!"
# Associate the file with the port
if __name__ == "__main__":
    app.run(debug=True, port=5000)