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

    plt.plot([1,2,3],[5,8,2])
    
    plt.xlabel(xaxis)
    plt.ylabel(yaxis)
    plt.title(title)
    
    plt.show()

def calcmax(platten:list, maxk:list):
    if mlqs[0]:
        nm = l%m
        print(nm)

def plot_maschine(plattenanzahl:int, montage:Montage, loeten:Loeten, qs:Qualitaetspruefung):
    zeitliste = []
    for i in range(1, plattenanzahl):
        zeitliste.append(i)

    mk = montage.kapazitaet
    lk = loeten.kapazitaet
    qk = qs.kapazitaet

    pm = 0
    pl = 0
    pq = 0

    fertige = 0

    while True:
        fertige += pq

        qr = pq + pl
        pl = 0
        if qr > qk:
            pq = qk
            pl += qr - qk

        lr = pl + pm
        pm = 0
        if lr > lk:
            pl = pk
            pm += lr - lk

        mr = pm + mk
        plattenanzahl -= mk
        if mr > mk:
            pm = mk
            plattenanzahl += mr - mk
            

    plt.plot(zeitliste, )
    
    plt.xlabel("Zeit")
    plt.ylabel("Platten")
    plt.title("Plattenfertigung")

    plt.show()

def main():
    plotgraph([1,2,3,4,5,6,7],[2,3,4,5,6,8,10])
    return

if __name__ == "__main__":
    main()
