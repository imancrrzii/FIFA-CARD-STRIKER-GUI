import tkinter as tk
import random

def generate_player():
    getRP = getRandomPosition()
    getC = getClub()
    getRPa = getRandomPace()
    getRD = getRandomDribbling()
    getRS = getRandomShoot()
    getRpas = getRandomPass()
    getRDe = getRandomDef()
    getPhy = getRandomPhy()
    getNat = getNation()
    overall = (getRpas + getRDe + getRPa + getRD + getRS + getPhy) // 5

    output_text = "  //--------------\\\\\n"
    output_text += " ||       ///|\\\\\\  ||\n"
    output_text += " ||  {}   | O O |  ||\n".format(overall)
    output_text += " ||  {}   |  ^  |  ||\n".format(getRP)
    output_text += " ||        \\___/   ||\n"
    output_text += " ||  {}           ||\n".format(getC.upper())
    output_text += " ||  {}           ||\n".format(getNat.upper())
    output_text += " ||----------------||\n"
    output_text += " || {} PAC  {} DRI ||\n".format(getRPa, getRD)
    output_text += " || {} SHO  {} DEF ||\n".format(getRS, getRDe)
    output_text += " || {} PAS  {} PHY ||\n".format(getRpas, getPhy)
    output_text += "  \\\\--------------//"

    output_label.config(text=output_text)

def getRandomPosition():
    position = ["LW", "CF", "SS", "RW"]
    randomPosition = random.choice(position)
    return randomPosition

def getRandomPace():
    paceStriker = 65 + random.randint(0, 34)
    return paceStriker

def getRandomDribbling():
    dribblingStriker = 65 + random.randint(0, 34)
    return dribblingStriker

def getRandomShoot():
    shootStriker = 65 + random.randint(0, 34)
    return shootStriker

def getRandomPass():
    passStriker = 65 + random.randint(0, 34)
    return passStriker

def getRandomDef():
    DefStriker = 10 + random.randint(0, 49)
    return DefStriker

def getRandomPhy():
    phyStriker = 65 + random.randint(0, 34)
    return phyStriker

def getClub():
    tim = [
        "MNC", "MNU", "CHE", "RMA", "BAR", "ATM", "PSG", "LIV",
        "ARS", "VAL", "SEV", "ACM", "JUV", "BAY", "DOR", "NAP",
        "MON", "INT"
    ]
    randomTim = random.choice(tim)
    return randomTim

def getNation():
    nation = [
        "ARG", "FRA", "CRO", "MAR", "POR", "NTH", "BRA", "ENG",
        "SPA", "GER", "IDN", "URU", "ITA", "BLG"
    ]
    randomNegara = random.choice(nation)
    return randomNegara

# Create GUI
window = tk.Tk()
window.title("FIFA Card Generator")

generate_button = tk.Button(window, text="Generate Player", command=generate_player, bg="blue", fg="white")
generate_button.pack(pady=10)

output_label = tk.Label(window, font=("Courier New", 12), justify="left")
output_label.pack()

window.mainloop()
