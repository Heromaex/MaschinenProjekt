import matplotlib.pyplot as plt

from maschinen import *

# Fragt den Nutzer, welche Option er aus einer Liste wählen möchte
def prompt(title:str, options:list):
    print()
    if len(options) == 0:
        print("Keine Auswahl vorhanden")
        return
    output = ""
    # Listet die gegebenen Optionen auf
    for i in range(len(options)):
        output += f"[{i+1}] "+options[i]+"\n"
    print(output)
    # Fragt nach einer Eingabe der Nummer
    # und gibt sie zum Nutzen des Programms zurück
    while True:
        inp = input(">>> ")
        try:
            int(inp)
        except TypeError:
            continue
        # Checks for valid inputs
        if inp == "":
            return
        if (int(inp) <= len(options)) and (int(inp) > 0):
            break
    return int(inp)

# Erstellt einen einzelnen Graphen mit gegebenen x- und y-Werten
# Optional können die Achsen und der Titel des Graphen auch umbenannt werden
def plotgraph(xvalues:list, yvalues:list, xaxis:str="x", yaxis:str="y", title:str="Verlaufsgraph", labels:list=[]):
    # Erstellt den virtuellen Graphen mit den Werten
    for i in range(len(yvalues)):
        if len(labels) > 0:
            plt.plot(xvalues,yvalues[i],label=labels[i])
        else:
            plt.plot(xvalues,yvalues[i])

    if len(labels) > 0:
        plt.legend()
    
    # Benennt die Achsen und setzt den Titel
    plt.xlabel(xaxis)
    plt.ylabel(yaxis)
    plt.title(title)
    
    # Rendert den erstellten Graphen
    plt.show()

def main():
    #plotgraph([1,2,3,4,5,6,7],[2,3,4,5,6,8,10])
    return

if __name__ == "__main__":
    main()
