**Rush Hour** is een ogenschijnlijk eenvoudig puzzeltje met een verrassend uitdagend karakter. In een veld van 6 hoog en 6 breed staat een rode auto (de jouwe), en die moet naar de uitgang die recht voor je ligt. Andere voertuigen versperren echter de weg: auto's van twee eenheden lang en trucks van drie eenheden lang, die alleen in hun rijrichting bewogen mogen worden. Ze mogen niet draaien.  
De opdracht is simpel: **beweeg je auto naar buiten** of, beter nog, **schrijf een computerprogramma om dat voor je te doen**.

---

### Structuur

De hierop volgende lijst beschrijft de belangrijkste mappen en files in het project, en waar je ze kan vinden:

- **/code**: bevat alle code van dit project
  - **/code/algorithms**: bevat de code voor de algoritmes
  - **/code/classes**: bevat de twee benodigde classes voor deze case
  - **/code/visualisation**: bevat de code om de visualitaties te maken zoals uit de presentatie
- **/data**: bevat de verschillende databestanden die wij hebben gegenereerd tijdens het runnen

- **main.py**: Dit is de file die je moet runnen om het programma uit te voeren en de algoritmes en andere parameters te kunnen kiezen

### Werking van algoritmes

- **BFS**: BFS (Breadth-First Search) verkent alle mogelijke zetten in Rush Hour niveau voor niveau, beginnend bij de initiële opstelling. Het gebruikt een queue om staten te onderzoeken en controleert of de rode auto de uitgang bereikt. Dit garandeert de kortste oplossing. Het gebruikt namelijk een FIFO methode.
- **DFS**: DFS (Depth-First Search) verkent Rush Hour door zo diep mogelijk één pad van zetten te volgen tot het einde of een doodlopend spoor, en keert dan terug om andere paden te proberen. Het gebruikt een stack om staten bij te houden en vindt niet per se de kortste oplossing omdat het LIFO volgorde gebruikt. DFS is minder efficiënt voor Rush Hour dan BFS, maar kan wel een oplossing vinden.
- **Hillclimber**: 
- **Random_algorithm**:  
- **Rando_heuristic**: 
- **SA**:

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


## Auteurs
- Pieter Wassink
- Kaj Westendorp