from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/meny')
def meny():
    ukemeny = [
        {'dag': 'Mandag', 'rett': 'Stekt Peeper', 'bilde': 'mandag.jpg', 'beskrivelse': 'Lokalplukket peeper, stekt til perfeksjon med et hint av Kharaa bacterium.'},
        {'dag': 'Tirsdag', 'rett': 'Dubious Måltid', 'bilde': 'tirsdag.jpg', 'beskrivelse': 'Resultatet av at Straffe-sjeffen Audun prøvde å lage en matrett.'},
        {'dag': 'Onsdag', 'rett': 'Stekt Biff', 'bilde': 'onsdag.jpg', 'beskrivelse': 'Denne oppskriften kommer fra en gammel kolega som het Steve, Er bare en stekt biff.'},
        {'dag': 'Torsdag', 'rett': 'Slurpfish', 'bilde': 'torsdag.jpg', 'beskrivelse': 'En forfriskene og sloppy fiskerett som kan gjøre deg blå av glede.'},
        {'dag': 'Fredag', 'rett': 'Gold Pickled Fowl Foot', 'bilde': 'fredag.jpg', 'beskrivelse': 'En gull delikatesse fra The Lands Between som bringer lykke og penger.'}
    ]
    return render_template('meny.html', meny=ukemeny)

@app.route('/varer')
def varer():
    varer_liste = [
        {'navn': 'Ost & Skinke Sandwich', 'pris': '60 kr', 'bilde': 'sandwich.jpg'},
        {'navn': 'God Morgen Yogurt', 'pris': '24.99 kr', 'bilde': 'yogurt.jpg'},
        {'navn': 'Diverse Frukt', 'pris': '15 kr', 'bilde': 'frukt.jpg'},
        {'navn': 'Kaffe', 'pris': '25 kr', 'bilde': 'kaffe.jpg'},
        {'navn': 'Litago 0.5L', 'pris': '25 kr', 'bilde': 'litago.jpg'},
        {'navn': 'Wasa Sandwich', 'pris': '30 kr', 'bilde': 'wasa.jpg'}
    ]
    return render_template('varer.html', varer=varer_liste)

@app.route('/kontakt')
def kontakt():
    return render_template('kontakt.html')

if __name__ == '__main__':
    app.run(debug=True)