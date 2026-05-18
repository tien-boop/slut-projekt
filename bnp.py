import csv

import matplotlib.pyplot as plt

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("search.html")

#Ta emot formulär-informationen
@app.route("/", methods=["POST"])
def show():

    if request.method == "POST":

        #Tar emot imput
        country = request.form["bnp"].strip().lower()

        with open("bnp.csv", encoding='utf-8-sig') as file:
            reader = csv.DictReader(file)

            #Läser innehållet i csv
            for row in reader:

                #Landet som söks stämmer med de som finns i csv
                if country == row['Country Name'].strip().lower():
                    
                    years = []
                    bnp = []

                    #Går igenom alla värde från 1960-2025 från det landet som söktes
                    for year in range(1960, 2026):

                        #Visar alla värde från 1960-2025
                        result = row[str(year)]
                        
                        #Lägger bara till riktiga siffror
                        if result != "":

                            #Lägger till året/värdet på det året i years- resp bnp-listan
                            years.append(year)
                            bnp.append(float(result))

                    #Skapar grafen 
                    plt.plot(years, bnp)
                    plt.xlabel("Year")
                    plt.ylabel("GDP per capita")
                    plt.title("GDP-growth")
                    plt.savefig('static/graph.png')
                    plt.close()

                    #Visar den färdiga bilden när man klicker på Send
                    return render_template("search.html", image="graph.png")

            #Ifall det inte finns det landet i CSV 
            return 'Not founded'
        

if __name__ == "__main__":
    app.run(debug=True)