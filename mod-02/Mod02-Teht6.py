# Kirjoita ohjelma, joka arpoo ja tulostaa kaksi erilaista numerolukon koodia:
# kolmenumeroisen koodin, jonka kukin numeromerkki on väliltä 0..9.
# nelinumeroisen koodin, jonka kukin numeromerkki on väliltä 1..6.

import random

satunaisluku1 = str(random.randint(0, 9))
satunaisluku2 = str(random.randint(0, 9))
satunaisluku3 = random.randint(0, 9)
print(f"Koodi 1: {satunaisluku1}{satunaisluku2}{satunaisluku3}")

satunaisluku4 = str(random.randint(0, 6))
satunaisluku5 = str(random.randint(0, 6))
satunaisluku6 = str(random.randint(0, 6))
satunaisluku7 = str(random.randint(0, 6))
print(f"Koodi 2: {satunaisluku4}{satunaisluku5}{satunaisluku6}{satunaisluku7}")
