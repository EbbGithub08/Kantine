from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)


ukemeny_list = [
    {'dag': 'Mandag', 'rett': 'Stekt Peeper', 'bilde': 'mandag.jpg', 'beskrivelse': 'Lokalplukket pepper, stekt til perfeksjon med et hint av Kharaa bacterium.'},
    {'dag': 'Tirsdag', 'rett': 'Dubious Måltid', 'bilde': 'tirsdag.jpg', 'beskrivelse': 'Resultatet av at Straffe-sjefen Audun prøvde å lage en matrett.'},
    {'dag': 'Onsdag', 'rett': 'Stekt Biff', 'bilde': 'onsdag.jpg', 'beskrivelse': 'Denne oppskriften kommer fra en gammel kollega som het Steve. Er bare en stekt biff.'},
    {'dag': 'Torsdag', 'rett': 'Slurpfish', 'bilde': 'torsdag.jpg', 'beskrivelse': 'En forfriskende og sloppy fiskerett som kan gjøre deg blå av glede.'},
    {'dag': 'Fredag', 'rett': 'Gold Pickled Fowl Foot', 'bilde': 'fredag.jpg', 'beskrivelse': 'En gulldelikatesse fra The Lands Between som bringer lykke og penger.'}
]# Ordbok med all informasjonen om de forksjellige dagene av ukeplannen i seg.



ukemeny_dict = {item['dag']: item for item in ukemeny_list} # Går gjennom ukemeny_list og bygger en ny ordbok hvor nøkkelen blir dagen og verdien er alt innenfor den dagen i ukemeny_list
# Dette gjør jeg sånn at jeg kan slå opp en av dagene, og så få all informasjonen ut fra ordboken, isteden for å måtte gå gjennom hele lista
# For eksempel = ukemeny_dict["Tirsdag"] hadde gitt meg all infoen til tirsdag, altså retten bildet og beskrivelsen.

dag_translation = {
    'Monday': 'Mandag', 'Tuesday': 'Tirsdag', 'Wednesday': 'Onsdag',
    'Thursday': 'Torsdag', 'Friday': 'Fredag', 'Saturday': 'Lørdag', 'Sunday': 'Søndag'
}# datetime biblioteket har engelske navn for ukedagene, siden jeg kodet nettsiden min på norsk er det lettest å lage en ordbok hvor nøkkelen er det engelske ordet til dagen og verdien er den norske.

@app.route('/')
def home():
    today_english = datetime.now().strftime('%A') # setter "today_english" til datoen idag sin engelske navn på ukedagen, ".strftime('%A')" gjør at vi henter string versonen av ukedagen blir hentet
    dagens_navn = dag_translation.get(today_english) # Henter translationen fra dag_translation til dagen idag.
    dagens_rett = ukemeny_dict.get(dagens_navn) # Henter navnet til dagen fra ukement_dict som jeg forklarte før.
    return render_template('index.html', dagens_rett=dagens_rett) # Gir "index.html" tilgang til dagens_rett som en variabel

@app.route('/meny') # Gjør det samme som home med datetime, bare at den også henter hele menyen.
def meny():
    today_english = datetime.now().strftime('%A')
    dagens_navn = dag_translation.get(today_english)
    return render_template('meny.html', meny=ukemeny_list, dagens_navn=dagens_navn)

@app.route('/varer') # Her har jeg puttet vare listen inni funksjonen fordi jeg trenger den bare inne på Varer siden, jeg har derfor meny listen uttenfor funksjonene fordi jeg trenger den til flere sider.
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
    app.run(debug=True) # Debug=True gjør at jeg slipper å starte og stoppe flask serveren for å se endringer på nettsiden. kan bare reloade isstedenfor.