import matplotlib.pyplot as plt

from maschinen import *
from platten import *

def prompt(options:list):
    print()
    output = ""
    for i in range(len(options)):
        output += f"[{i+1}]"+options[i]+"\n"
    print()
    inp = input(">>> ")
    return inp

def plotgraph(xvalues:list, yvalues:list, xaxis:str="x", yaxis:str="y", title:str="Verlaufsgraph"):
    if not type(xvalues[0]) is int:
        for i in range(len(xvalues)):
            plt.plot(xvalues[i],yvalues[i])
    else:
        plt.plot(xvalues,yvalues)
    
    plt.xlabel(xaxis)
    plt.ylabel(yaxis)
    plt.title(title)
    
    plt.show()

def calcmax(platten:list, maxk:list):
    if mlqs[0]:
        nm = l%m
        print(nm)

def plot_maschine(start:int, stopp:int, montage:Montage, loeten:Loeten, qs:Qualitaetspruefung):
    zeitliste = []
    for i in range(start, stopp):
        zeitliste.append(i)

    mk = montage.kapazitaet
    lk = loeten.kapazitaet
    qk = qs.kapazitaet

    m = []
    l = []
    q = []
    for i in range(stopp-start):
        if i == start:
            m.append(mk*i)
        if i == start+1:
            m.append(mk*i)
            m.append(lk*i)
            

    plt.plot(zeitliste, )
    
    plt.xlabel("Zeit")
    plt.ylabel("Platten")
    plt.title("Plattenfertigung")

    plt.show()

def main():
    #plotgraph([1,5,2,3,5,7,9],[2,2,3,4,5,6,8])
    return

if __name__ == "__main__":
    main()
