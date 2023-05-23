import os
import fnmatch
from bs4 import BeautifulSoup
import re

#Tukaj so spravljene vse funkcije, ki jih potrebujemo.

def naslovi_slik(directory):
    """Funkcija vrne tabelo vseh naslovov slik v vseh mapah. Zaenkrat bo delovala samo za zgodbe."""

    tabela_imen = []
    for root, dirs, files in os.walk(directory):
        for filename in files:
            if fnmatch.fnmatch(filename, '*.png'):
                tabela_imen.append(filename)
    return tabela_imen

def spremeni_naslov(naslov):
    """Funkcija spremeni naslov h1 in title"""

    # Read the HTML file
    with open('naloga/index.html', 'r', encoding='utf-8') as file:
        html_content = file.read()

    # Create a BeautifulSoup object
    soup = BeautifulSoup(html_content, 'html.parser')

    # Change h1
    h1_tag = soup.find('h1')
    h1_tag.string = naslov

    # Change the title
    title_tag = soup.find('title')
    title_tag.string = naslov

    # Save the modified HTML content to a new file
    with open('naloga/index.html', 'w', encoding='utf-8') as file:
        file.write(str(soup))

def spremeni_besedilo(besedilo):
    '''Spremeni besedilo'''
    # Read the HTML file
    with open('naloga/index.html', 'r', encoding='utf-8') as file:
        html_content = file.read()

    # Create a BeautifulSoup object
    soup = BeautifulSoup(html_content, 'html.parser')

    # Change p
    p_tag = soup.find('p')
    p_tag.string = besedilo


    # Save the modified HTML content to a new file
    with open('naloga/index.html', 'w', encoding='utf-8') as file:
        file.write(str(soup))

def spremeni_generated_blocks(block):
    '''Funkcija doda nov block v generated block'''

    #Kateri bloki obstajajo.


    # Read the JavaScript file
    with open('naloga/test.js', 'r', encoding='utf-8') as file:
        js_code = file.read()

    # Modify the "robot" array in Python
    modified_code = re.sub(r"(robot:\s*\[[^\]]*)", r" \1," + "\"{}\"".format(block), js_code)

    # Save the updated JavaScript code back to the file
    with open('naloga/test.js', 'w', encoding='utf-8') as file:
        file.write(modified_code)

def dodaj_grid(n, m):
    """Zapišemo grid(matriko), ki jo generiramo, v javascript fajl"""
    with open('naloga/test.js', 'r', encoding='utf-8') as file:
        content = file.read()

    pattern = r'tiles:\s*\[[^\]]+\]'
    replacement = f'tiles: {naredi_matriko(n, m)}'

    updated_content = re.sub(pattern, replacement, content)
    print(updated_content)

    """with open('naloga/test.js', 'w',encoding='utf-8') as file:
        file.write(updated_content)"""
    
def naredi_matriko(n, m):
    """Naredi matriko n x m, kjer so same enice"""
    matrix = [[1] * m for _ in range(n)]
    matrix_string = ""
    max_element_length = len(str(max(matrix[i][j] for i in range(n) for j in range(m))))

    for row in matrix:
        row_string = "[{}]".format(", ".join("{:<{}}".format(element, max_element_length) for element in row))
        matrix_string += "{}\n".format(row_string)

    shifted_matrix_string = ""
    lines = matrix_string.split('\n')
    for i, line in enumerate(lines):
        line = line.strip()
        shifted_matrix_string += 39 * " " + line + '\n'

    return "[" + shifted_matrix_string.strip() + "\n" + 39 * " " + "]"

