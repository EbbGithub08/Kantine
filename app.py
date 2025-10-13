from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/meny')
def meny():
    ukemeny = [
        {'dag': 'Mandag', 'rett': 'Stekt Peeper', 'bilde': 'mandag.jpg'},
        {'dag': 'Tirsdag', 'rett': 'Dubious Måltid', 'bilde': 'tirsdag.jpg'},
        {'dag': 'Onsdag', 'rett': 'Stekt Biff', 'bilde': 'onsdag.jpg'},
        {'dag': 'Torsdag', 'rett': 'Slurpfish', 'bilde': 'torsdag.jpg'},
        {'dag': 'Fredag', 'rett': 'Gold Pickled Fowl Foot', 'bilde': 'fredag.jpg'}
    ]
    return render_template('meny.html', meny=ukemeny)

@app.route('/varer')
def varer():
    varer_liste = [
        {'navn': 'Ost og Skinke Sandwich', 'pris': '60 kr'},
        {'navn': 'God Morgen Yogurt', 'pris': '24.99 kr'},
        {'navn': 'Eple / Banan / Pære (Diverse Frukt)', 'pris': '15 kr'},
        {'navn': 'Kaffe', 'pris': '25 kr'},
        {'navn': 'Litago 0.5L', 'pris': '25 kr'},
        {'navn': 'TINE IsKaffe', 'pris': '30 kr'},
        {'navn': 'Wasa Sandwich', 'pris': '30 kr'}
    ]
    return render_template('varer.html', varer=varer_liste)

@app.route('/kontakt')
def kontakt():
    return render_template('kontakt.html')

if __name__ == '__main__':
    app.run(debug=True)