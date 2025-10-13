from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/meny')
def meny():
    return render_template('meny.html')

@app.route('/varer')
def varer():
    varer_liste = [
        {'navn': 'Ost og Skinke Sandwich', 'pris': '60 kr'},
        {'navn': 'God Morgen Yogurt', 'pris': '30 kr'},
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