# RushHourProject
Rush Hour is een ogenschijnlijk eenvoudig puzzeltje met een verrassend uitdagend karakter. In een veld van 6 hoog en 6 breed staat een rode auto, de jouwe, en die moet naar de uitgang. die recht voor je ligt. Maar andere voertuigen versperren de weg; auto’s van twee eenheden lang en trucks van drie eenheden lang, die alleen in hun rijrichting bewogen mogen worden. Ze mogen niet draaien. De opdracht is simpel: beweeg je auto naar buiten, of beter: schrijf een computerprogramma om dat voor je te doen.


# Experimenteren
Om de resultaten te reproduceren moet uw simpelweg de main.py functie roepen in uw terminal terwijl uw in de RushHourProject directory bent, hierna volgt een keuze menu om de verschillende borden te keizen en de verschillende algoritmes te runnen. 
De data voor BFS wordt automatisch opgeslagen in een csv met de naam van het bordgrote en de moeilijkheid van het bord. 
Vervolgs wordt er in de terminal de sequence van moves geprint en de tijd dat het gekost heeft om de functie te runnen.
Ook de oplossing wordt opgeslagen


# Om het programma te runnen

Om het programma te runnen moet je de volgende command in de terminal zetten terwijl je in de RushHourProject directory bent:

'''
$ python main.py

'''

Daarna volgt de eerste keuze menu om het algoritme te kiezen:

'''
Available algorithms:
  1. Random Algorithm
  2. Random + Heuristic
  3. Hill Climber
  4. Simulated Annealing
  5. Breadth First Search
  6. Depth First Search
  7. Hill Climber Optimized
Select an algorithm (1-7):

'''

Daarna volgt de keuze menu voor aantal trials

'''
Enter number of trials:

'''

Als laatste de keuze voor het aantal iteraties:

'''
Enter number of iterations:

'''

Het programma zal dan runnen en bewaard de oplossingen en de informatie