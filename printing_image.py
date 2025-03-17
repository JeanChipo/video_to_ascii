from time import sleep
import os

def printvid()->None:
    height = determine_height()
    os.system('cls')
    with open("./ascii_art.txt", 'r') as ascii :
        cpt = 0
        for line in ascii:
            cpt += 1
            print(line, end='')
            if cpt >= height:
                sleep(1/60)
                print("\033[H\033[J", end="")
                cpt = 0

def determine_height():
    i = 1
    with open("./ascii_art.txt", 'r') as ascii:
        while ascii.readline()[0] != '=':
            i += 1
        return i
