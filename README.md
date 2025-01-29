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
- **Random_algorithm**: Dit algoritme zet alle autos met hun corresponderende bewgingsmogelijkheden in een lijst. Uit deze lijst wordt een willekeurige auto gekozen om te bewegen. Dit wordt voor een bepaald aantal iteraties gedaan, of totdat het bord opgelost is. Dit algoritme weet alle Rush Hour borden op te lossen
- **Rando_heuristic**: Dit algoritme bouwt voort op het Random Algoritme, door er een heuristiek aan toe te voegen. De heuristiek die geïmplementeerd is, is het voorkomen van dubbele bordconfiguraties. Dit algoritme slaat de stappen reeks op, en zodra een bordconfiguratie voor de 2e keer voorbijkomt, worden alle tussenstappen verwijderd, en gaat het algoritme verder vanaf deze 'dubbele' stap. Dit algoritme weet alle Rush Hour borden op te lossen, en is na BFS ons best presterende algoritme.
- **Hillclimber**: HillClimber begint met door eerst een bord op te lossen door middel van het Random Algoritme. Vervolgens wordt dit opgeloste bord doorgegeven aan het HillClimber algoritme, die vervolgens de stappenreeks aanpast. Deze aanpassing is willekeurig, en kan bestaan uit het verwijderen van een stap, het omwisselen van 2 stappen, en het omdraaien van een richting van een bepaalde stap. Vervolgens wordt er gecontroleerd of het bord is opgelost, en of het aantal stappen om een oplossing te vinden is verminderd. Als dit aantal hetzelfde of minder is, wordt de nieuwe stappenreeks aangehouden. Dit wordt voor een bepaald aantal iteraties herhaald. Het HillClimber2 /HillClimber Optimized algoritme werkt hetzelfde als HillClimber, maar voorkomt het maken van deepcopies, waardoor het algoritme sneller en efficienter werkt. Dit algoritme weet elke Rush Hour bord op te lossen, en presteert beter dan het Random Algoritme.
- **SA**: Het Simulated Annealing Algoritme bouwt voort op het HillClimber Algoritme. Dit algoritme begint ook met een willekeurig opgelost bord, waarna het de stappenreeks probeert aan te passen om een snellere oplossing te vinden. Dit algoritme introduceert temperatuur, cooling rate en acceptatiefunctie. Dit algoritme accepteert door middel van de acceptatiefunctie en temperatuur soms ook minder goede oplossingen, waardoor het eventueel uit een lokaal optimum/minimum zou moeten komen. Per iteratie daalt de temperatuur volgens de cooling rate waardoor de kans op het accepteren van een minder 'goede' oplossing kleiner wordt. Dit algoritme hanteert een iets agressievere mutatie methode met als doel het snel vinden van een betere oplossing (en omdat zoals het nu geïmplementeerd is erg inneficient is dankzij de deepcopies die gemaakt worden). In onze case is het helaas niet gelukt om SA te optimaliseren, waardoor de runtime nu nog per iteratie verdubbelt. Hierdoor is het niet in staat om enkel van de borden op te lossen.

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