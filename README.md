## Install
### pip install playwright
### playwright install
### pip install pytest
### pip install pytest-playwright

## User story [U1] 
### Som en användare vill jag kunna se att knappen 'Add timer' är synlig och kan klickas

## Acceptanskriterier 
[A1] Knappen "Add timer" ska vara synlig på sidan.
[A2] När jag klickar på knappen, ska en ny timer visas på skärmen.

## Testscenario [T1] –  Kontrollera att knappen 'Add timer' är synlig och kan klickas
1. Navigera till webbsidan.
2. Kontrollera att knappen "Add timer" finns och är synlig.
3. Klicka på knappen "Add timer".

## User story [U2] 
### Som en användare vill jag kunna se att knappen 'Add note' är synlig och kan klickas, och dessutom kunna lägga till och ändra ordningen på noterna.

## Acceptanskriterier 
[A1] Knappen "Add note" ska vara synlig på sidan.
[A2] När jag klickar på knappen, ska en text "Click to change text" visas på skärmen.
[A3] Det ska vara möjligt att klicka på texten och ändra innehållet.
[A4] När man trycker "Enter", sparas texten.
[A5] När man trycker på korgen, suddas texten bort.
[A6] Det ska vara möjligt att ändra ordningen på noterna med hjälp av pilarna (upp eller ner).

## Testscenario [T2] – Kontrollera att knappen 'Add note' är synlig och kan klickas, add och delete note
1. Navigera till webbsidan.
2. Kontrollera att knappen "Add note" finns och är synlig.
3. Klicka på knappen "Add note".
4. Kontrollera att en text "Click to change text" visas på skärmen.
5. Klicka på texten "Click to change text" 
6. Hitta input-fältet 
7. Fyll i ny text till något som "Note 1"
8. Tryck på "Enter" för att spara
9. Kontrollera att texten har ändrats till "Note 1"
10. Klicka på "Add note" igen och addera en ny text, ändra texten î "Note 2".
11. Ändra ordningen på "Note 1" och "Note 2" när man klickar på pilen
12. Kontrollera om ändringen sker dvs. om texterna har ändrad ordningen
13. Testar delete button (korgen)

## User story [U3] 
### Som en användare vill jag kunna se att timern startar från 15:00 och att den kan reset eller startas.

## Acceptanskriterier
[A1] Timern ska starta från 15:00.
[A2] Timern ska ha knappar för "Start" och "Reset".
[A3] När man klickar på "Start" börjar timern räkna ner.
[A4] När man klickar på "Reset" ska timern återställas till 15:00.

## Testscenario [T3] – Timmerinteraktioner
1. Kontrollera att timern visas korrekt på sidan efter att du har klickat på knappen "Add timer".
2. Kontrollera att timern startar från 15:00.
3. Klicka på "Start" och kontrollera att timern börjar räkna ner.
4. Klicka på "Reset" och kontrollera att timern återställs till 15:00.
