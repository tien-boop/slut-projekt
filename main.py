import requests
from bs4 import BeautifulSoup

from flask import Flask, render_template, request

url = "https://en.wikipedia.org/wiki/The_World%27s_Billionaires"

response = requests.get(url)

html_content = response.text
soup = BeautifulSoup(html_content, "html.parser")
main_table = soup.select("table.wikitable tr td")

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("search.html")

@app.route("/", methods=["POST"])
def show():
    search = request.form["billionaire"]
    return "Du gillar: " + search




if __name__ == "__main__":
    app.run(debug=True)