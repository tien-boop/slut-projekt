import requests
from bs4 import BeautifulSoup

from flask import Flask, render_template, request

app = Flask(__name__)

url = "https://en.wikipedia.org/wiki/The_World%27s_Billionaires"

response = requests.get(url)

html_content = response.text
soup = BeautifulSoup(html_content, "html.parser")

# Hämta tabellen
main_table = soup.select("table.wikitable")
# Hämta individuella rutor i tabellen
main_boxes = soup.select("table.wikitable tr td")
# Hämta länkar i tabellen
main_links = soup.select("table.wikitable tr td a")

billionaires = []

found = False



@app.route("/")
def home():
    return render_template("search.html")

@app.route("/", methods=["POST"])
def show():

    if request.method == "POST":

        year = request.form["billionaire"].strip()

        # Hitta år
        year_headers = soup.find("h3")

        #!!!.vrf ska man ha for i detta fall vrf ska man ha innehållet av den!!for h3 in year_headers:

            if h3.text == year:
                
                table = h3.find_next("table")

            return str(table)

        #if year_text:
        #    hittar ordning på personer och namn

        #else:
        #    return "Året hittades inte"

        return "Året hittades inte"

if __name__ == "__main__":
    app.run(debug=True)