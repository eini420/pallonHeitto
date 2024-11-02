import math

# heippa tässä muutos!!


# Painovoima-arvot eri taivaankappaleille
painovoimat = {
    "1": ("Maa", 9.81),      # m/s^2
    "2": ("Kuu", 1.62),      # m/s^2
    "3": ("Mars", 3.71),     # m/s^2
    "4": ("Jupiter", 24.79), # m/s^2
    "5": ("Aurinko", 274.0)  # m/s^2
}

def laske_heiton_parametrit(alkunopeus, kulma_asteina, painovoima):
    # Muutetaan kulma radiaaneiksi
    kulma_radiaaneina = math.radians(kulma_asteina)
    
    # Lasketaan alkunopeuden vaaka- ja pystysuuntakomponentit
    alkunopeus_x = alkunopeus * math.cos(kulma_radiaaneina)
    alkunopeus_y = alkunopeus * math.sin(kulma_radiaaneina)
    
    # Lasketaan lentoaika
    lentoaika = (2 * alkunopeus_y) / painovoima
    
    # Lasketaan maksimikorkeus
    maksimi_korkeus = (alkunopeus_y ** 2) / (2 * painovoima)
    
    # Lasketaan kantama
    kantama = alkunopeus_x * lentoaika
    
    return lentoaika, maksimi_korkeus, kantama

def main():
    # Kysytään käyttäjältä taivaankappaleen valinta
    print("Tätä muokattu:")
    print("Missä haluat heittää palloa? Valitse yksi seuraavista:")
    print("1. Maa\n2. Kuu\n3. Mars\n4. Jupiter\n5. Aurinko")
    valinta = input("Anna valintasi (1, 2, 3, 4 tai 5): ")
    
    # Tarkistetaan valinta ja haetaan vastaava painovoima
    if valinta in painovoimat:
        taivaankappale, painovoima = painovoimat[valinta]
    else:
        print("Virheellinen valinta. Aja ohjelma uudelleen ja valitse kelvollinen vaihtoehto.")
        return

    # Kysytään käyttäjältä alkunopeus ja kulma
    alkunopeus = float(input("Anna alkunopeus (m/s): "))
    kulma_asteina = float(input("Anna lähtökulma (astetta): "))
    
    # Lasketaan heiton parametrit
    lentoaika, maksimi_korkeus, kantama = laske_heiton_parametrit(alkunopeus, kulma_asteina, painovoima)
    
    # Näytetään tulokset
    print(f"\nTulokset pallon heittämiselle kohteeseen {taivaankappale}:")
    print(f"Painovoima: {painovoima} m/s^2")
    print(f"Lentoaika: {lentoaika:.2f} sekuntia")
    print(f"Maksimikorkeus: {maksimi_korkeus:.2f} metriä")
    print(f"Kantama: {kantama:.2f} metriä")

if __name__ == "__main__":
    main()
