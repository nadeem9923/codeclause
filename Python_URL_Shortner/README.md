# Project Title: URL Shortener using Python

In this code, I used the flask library to create a basic web application. The shorten_url function generates a random short URL consisting of 6 characters from the set of uppercase letters, lowercase letters, and digits.

The / route handles the POST request to shorten a URL. It expects the long URL to be sent in the request body as url. It generates a short URL using shorten_url and stores the mapping of the short URL to the long URL in the url_mapping dictionary.

The /<short_url> route handles the GET request for a short URL. If the short URL exists in the url_mapping dictionary, it retrieves the corresponding long URL and redirects the user to that URL. Otherwise, it returns an error message.

To run this code, make sure you have the flask library installed (pip install flask) and save the code in a file (e.g., app.py). Then, you can run the application by executing python app.py in your terminal. The application will start running, and you can access it at http://localhost:5000/.

# IDE used: Pycharm
