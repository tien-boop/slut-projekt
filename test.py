import requests
from bs4 import BeautifulSoup

from flask import Flask, render_template, request

app = Flask(__name__)

url = "https://en.wikipedia.org/wiki/The_World%27s_Billionaires"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

# Hitta tabellen
table = soup.find("table", class_="wikitable")

# Hämta alla rader
rows = table.find_all("tr")

billionaires = []

# Skippa första raden (rubriker)
for row in rows[1:]:

    cols = row.find_all("td")

    if len(cols) >= 5:

        try:
            rank = cols[0].text.strip()
            name = cols[1].text.strip()

            # Ta bort $ och kommatecken
            net_worth = cols[2].text.strip()
            net_worth = net_worth.replace("$", "")
            net_worth = net_worth.replace(",", "")

            country = cols[3].text.strip()

            billionaires.append({
                "rank": rank,
                "name": name,
                "worth": net_worth,
                "country": country
            })

        except:
            pass

@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":

        search = request.form["year"]

        result = ""

        for person in billionaires:

            result += f"""
            <p>
            #{person['rank']} -
            {person['name']} -
            ${person['worth']} billion
            </p>
            """

        return result

    return render_template("search.html")

if __name__ == "__main__":
    app.run(debug=True)