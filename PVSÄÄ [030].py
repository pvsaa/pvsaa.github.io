import pandas as pd
import plotly.graph_objects as go
from datetime import datetime
import os
def cls():
    os.system('cls' if os.name=='nt' else 'clear')
def nykyinen():
    now = datetime.now()
    return now.strftime("%d/%m/%Y [%H:%M:%S]")
def efhk15():
    tulos = pd.read_csv("https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/EFHK?unitGroup=metric&include=hours&key=C4HYD595SZKMABVWYGRYF8YUG&contentType=csv")
    fname = "tiedostot/efhk15"
    f = open(fname + ".csv", "w")
    f.write(tulos.to_csv())
    f.close()
def luku1():
    df = pd.read_csv("tiedostot/efhk15" + ".csv")
    fig = go.Figure([go.Scatter(x=df['datetime'], y=df['temp'])])
    fig.update_layout(title="Juuso on paras!")
    fig.write_image("testikuva1.png")
def efhk_nykyinen():
    tulos = pd.read_csv("https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/EFHK?unitGroup=metric&include=current&key=C4HYD595SZKMABVWYGRYF8YUG&contentType=csv")
    fname = "tiedostot/efhk-nykyinen"
    f = open(fname + ".csv", "w")
    f.write(tulos.to_csv())
    f.close()
def meny():
    cls()
    df = pd.read_csv("tiedostot/efhk-nykyinen" + ".csv")
    päivä, tunti = str(df["datetime"][0]).split("T")
    print("Meny - " + nykyinen() + "\n")
    
    print("Lämpötila: " + str(df["temp"][0]) + " °C")
    print("Tuntuu kuin: " + str(df["feelslike"][0])+ " °C")
    print("Kastepiste: " + str(df["dew"][0]) + " °C\n")
    print("Kosteus: " + str(df["humidity"][0]) + " %")
    print("Ilmanpaine: " + str(df["sealevelpressure"][0]) + " hPa\n")
    print("Tuulen nopeus: " + str(int(df["windspeed"][0])/3.6) + " m/s")
    print("Tuulen suunta: " + str(df["winddir"][0]) + " °\n")
    print("Tiedot päivitetty: " + päivä + " " + tunti)
    
def start():
    cls()
    print("Peltovuren sää :)   Versio: 03   Juusdo \n")
    menu()
    
    
def menu():
    print("Menu: \n")
    com = input("""    [1] Meny
    [2] Nykyinen
    [3] Ruuvi 
    [4] Ennustus
    [5] Historia
    [6] Info / Asetukset
    [7] Quit \n
>>> """)
    if com == "1":
        meny()
    
    
start()