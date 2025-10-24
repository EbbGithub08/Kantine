# Kantine-Flask-Prosjekt

Velkommen til kildekoden for den splitter nye kantina i syvende etasje hos Snobademiet. Dette er et mesterverk av en nettside, bygget med Flask, for å vise frem alt det forferdelige vi har å tilby.

## Om Prosjektet

Etter kort tids ønske fra ingen, har vi desverre fått på plass en kantine vi ikke er stolte av. Målet med denne nettsiden er å gi en "god" oversikt over det vi serverer. Vi garanterer 100% at du tilbringer tredje time på dass etter et måltid herfra.

Nettsiden er bygget for å være så brukervennlig at selv en apekatt kunne funnet frem, men innholdet er en annen sak.

## Features

*   **Dynamisk Meny**: Viser en full ukesmeny. Siden henter automatisk ut dagens rett basert på hvilken dag det er, og fremhever den med en glinsende gull-animasjon. I helgene får du en hyggelig beskjed om å komme tilbake på mandag.
*   **Vareside**: En oversikt over standardvarer som sandwich, frukt og kaffe. Inkluderer et helt sinnsykt **GIGA ULTRA SALE** på God Morgen Yogurt, med regnbue-animasjon for maks oppmerksomhet.
*   **Kontaktside**: En liste over nøkkelpersoner i kantinedriften. Noen av oss er viktigere enn andre, så ett av kortene har fått litt ekstra CSS-kjærlighet.
*   **Responsivt (ish) Design**: Ser helt greit ut på de fleste skjermer, takket være litt flexbox og grid.
*   **Fete Animasjoner**: Fordi hvorfor ikke? Vi har regnbuer og skinnende gull.

## Teknologier

Dette vidunderet er bygget med:

*   **Backend**: Python med Flask
*   **Frontend**: HTML5, CSS3
*   **Templating**: Jinja2

## Hvordan kjøre prosjektet

Hvis du av en eller annen grunn vil kjøre dette lokalt.

1.  **Klone repoet** (hvis du har det på Git)
    ```bash
    git clone <din-repo-url>
    cd Kantine
    ```

2.  **Installer Flask**
    Det er lurt å bruke et virtuelt miljø, men hvem bryr seg.
    ```bash
    pip install Flask
    ```

3.  **Kjør appen**
    ```bash
    python app.py
    ```

4.  **Åpne i nettleseren**
    Gå til `http://127.0.0.1:5000` og nyt elendigheten. `debug=True` er på, så du kan bare lagre endringer og laste inn siden på nytt. Fakk deg!

## Hvordan det funker (sånn ca.)

*   `app.py`: Hovedfilen som styrer alt. Den har noen ruter (`@app.route`) for hver side.
*   **Dagens Rett**: `app.py` bruker `datetime` for å finne ut hvilken dag det er. Så slår den opp i en ordbok for å finne dagens rett og sender den til `index.html` og `meny.html`. Ganske smart, egentlig.
*   `templates/`: Her ligger alle HTML-filene. `base.html` er skjelettet, og de andre sidene fyller inn innhold med Jinja-blokker.
*   `static/`: Inneholder `style.css` som får alt til å se... ut. Og bildene, selvfølgelig.

---

© 2025 Kantine Laget Av Ebbe
