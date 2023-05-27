from flask import Flask, render_template, request, redirect
import pyshorteners

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        long_url = request.form['url']
        short_url = shorten_url(long_url)
        return render_template('index.html', short_url=short_url)
    return render_template('index.html')

def shorten_url(url):
    shortener = pyshorteners.Shortener()
    short_url = shortener.tinyurl.short(url)
    return short_url

if __name__ == '__main__':
    app.run(debug=True)