#Element Checker
from pyscript import display, document

nonmetals = {
    "Kr": ('Krypton', 36, 83.798), "C": ('Carbon', 6, 12.011), "Se": ('Selenium', 34, 78.971), "H": ('Hydrogen', 1, 1.008),
    "Rn": ('Radon', 86, 222), "Cl": ('Chlorine', 17, 35.45), "O": ('Oxygen', 8, 15.999), "Xe": ('Xenon', 54, 131.29),
    "N": ('Nitrogen', 7, 14.007), "Br": ('Bromine', 35, 79.904), "He": ('Helium', 2, 4.0026), "S": ('Sulfur', 16, 32.06),
    "F": ('Fluorine', 9, 18.998), "I": ('Iodine', 53, 126.90), "Ne": ('Neon', 10, 20.180), "Ar": ('Argon', 18, 39.948),
    "P": ('Phosphorus', 15, 30.974),
}

def element_checker(event):
    document.getElementById("element").innerHTML = ""
    symbol = document.getElementById("non_elements").value.strip().capitalize()
    name, number, mass = nonmetals.get(symbol, ('Element not found', '?', '?'))
    display(f"{name}: atomic number {number}, atomic mass {mass}", target="element")