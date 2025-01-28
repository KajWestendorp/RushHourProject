**Rush Hour** is een ogenschijnlijk eenvoudig puzzeltje met een verrassend uitdagend karakter. In een veld van 6 hoog en 6 breed staat een rode auto (de jouwe), en die moet naar de uitgang die recht voor je ligt. Andere voertuigen versperren echter de weg: auto's van twee eenheden lang en trucks van drie eenheden lang, die alleen in hun rijrichting bewogen mogen worden. Ze mogen niet draaien.  
De opdracht is simpel: **beweeg je auto naar buiten** of, beter nog, **schrijf een computerprogramma om dat voor je te doen**.

---

## Experimenteren

Om de resultaten te reproduceren, roep je simpelweg de `main.py` functie aan in je terminal terwijl je in de `RushHourProject` directory bent. Hierna verschijnt een keuzemenu waarmee je verschillende borden kunt kiezen en de verschillende algoritmes kunt uitvoeren.

- De data voor **Breadth First Search (BFS)** wordt automatisch opgeslagen in een `.csv`-bestand, met de naam gebaseerd op de grootte en moeilijkheidsgraad van het bord.
- In de terminal worden vervolgens de **sequence van moves** geprint, samen met de tijd die het gekost heeft om de functie uit te voeren.
- De oplossing wordt ook opgeslagen.

---

## Het programma uitvoeren

Om het programma uit te voeren, voer je het volgende commando uit in de terminal terwijl je in de `RushHourProject` directory bent:

```bash
$ python main.py
```

### Stap 1: Kies een algoritme

Na het uitvoeren van het programma verschijnt een keuzemenu om het algoritme te selecteren:

```plaintext
Available algorithms:
  1. Random Algorithm
  2. Random + Heuristic
  3. Hill Climber
  4. Simulated Annealing
  5. Breadth First Search
  6. Depth First Search
  7. Hill Climber Optimized
Select an algorithm (1-7):
```

### Stap 2: Aantal trials invoeren

Daarna volgt een keuzemenu voor het aantal trials:

```plaintext
Enter number of trials:
```

### Stap 3: Aantal iteraties invoeren

Tot slot kies je het aantal iteraties:

```plaintext
Enter number of iterations:
```

---

## Uitvoering en opslag

Het programma wordt uitgevoerd en:

1. De oplossingen en bijbehorende informatie worden opgeslagen.
2. In de terminal worden de moves, tijdsduur, en details over het proces weergegeven.
