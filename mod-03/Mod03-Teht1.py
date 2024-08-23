'''
Kirjoita ohjelma, joka kysyy kalastajalta kuhan pituuden senttimetreinä. Jos kuha on alamittainen, ohjelma käskee laskea kuhan takaisin järveen ilmoittaen samalla käyttäjälle, montako senttiä alimmasta sallitusta pyyntimitasta puuttuu. Kuha on alamittainen, jos sen pituus on alle 37 cm.
'''

kuha = int(input("Anna kuhan pituus: "))
if kuha <= 37:
    alamittainen = 37 - kuha
    print(f"Kuha on {alamittainen} sentimetria lyhempi, kuin sallitua. Ole hyvä ja laskee kuha takasiin järveen.")
else:
    print("Kuha on ok!")
