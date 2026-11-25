# suprise_2026

Een Django-site voor je Surprise: inloggen, een gedicht lezen, drie opdrachten maken en – bij drie goede antwoorden – een 3-cijferige combinatie voor het slot krijgen.

## Snel starten

1) Maak en activeer een virtualenv (optioneel als je IDE dit al doet)
- macOS/Linux:
  - `python -m venv .venv && source .venv/bin/activate`
- Windows (PowerShell):
  - `python -m venv .venv; .\.venv\Scripts\Activate.ps1`

2) Installeer dependencies
- `pip install -r requirements.txt`

3) Initialiseer database
- `python manage.py migrate`

4) Maak een admin-gebruiker (om gedicht en opdrachten te beheren)
- `python manage.py createsuperuser`

5) Start de server
- `python manage.py runserver`
- Ga naar http://127.0.0.1:8000
- Login met een (door jou aangemaakt) account. De eerste keer worden voorbeeld-gegevens (1 gedicht, 3 opdrachten) automatisch aangemaakt.

## Beheer

- Admin-omgeving: http://127.0.0.1:8000/admin
- Daar kun je:
  - Poem (Gedicht): titel/tekst wijzigen en “active” aanvinken voor het gedicht dat getoond moet worden.
  - Task (Opdracht): drie opdrachten beheren met volgorde (1–3), vraag, juist antwoord en het cijfer (0–9) dat bij een goed antwoord hoort.

## Werking

- De homepage (achter login) toont:
  - Het actieve gedicht
  - Drie opdrachten (1, 2, 3)
  - Een formulier met drie antwoorden
- Na versturen:
  - Je ziet hoeveel antwoorden goed zijn en een cijfer (0–10)
  - Als alle drie goed zijn, verschijnt de combinatie (bijv. “147”)
  - Als niet alles goed is, zie je een hint met bekende cijfers en “?” voor foute antwoorden (bijv. “1?7”)

## Aanpassen

- Tekst van het gedicht en de opdrachten pas je aan via de admin.
- Styling kun je wijzigen in `static/css/style.css`.
- Templates staan in `templates/`.

Veel plezier en succes met je Surprise!
