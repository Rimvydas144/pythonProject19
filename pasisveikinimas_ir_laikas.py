# def name_surname(vardas, pavarde):
#     print(f' Labas, {vardas} {pavarde}')
import time


def time_hi(laikas, vardas, pavarde):
    if 6 <= laikas < 12:
        print(f'Labas rytas, {vardas} {pavarde}')
    elif 12 <= laikas < 18:
        print(f'Laba diena, {vardas} {pavarde}')
    elif 18 <= laikas < 22:
        print(f'Labas vakaras, {vardas} {pavarde}')
    else:
        print(f'Labanakt, {vardas} {pavarde}')

time_hi(10, "Adomai", "Adomaiti")

time.sleep(10)