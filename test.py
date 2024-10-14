# # Testi eli pääohjelma:
#
# def etsi_kallein(taulut):
#     kallein = taulut[0]
#     for taulu in taulut:
#         if taulu['hinta'] > kallein['hinta']:
#             kallein = taulu
#     return kallein
#
#
# taulut = [
#     {'nimi': 'Meri', 'hinta': 1280},
#     {'nimi': 'Tyttö', 'hinta': 3100},
#     {'nimi': 'Ilta', 'hinta': 2500},
# ]
#
# kallein = etsi_kallein(taulut)
# print(f"Kallein taulu on: {kallein["nimi"]}")
# print(f"On hinnaltaan: {kallein["hinta"]}€")


# def etsi_kallein(tuotteet):
#     kallein = tuotteet[0]
#     for tuote in tuotteet:
#         if tuote['price'] > kallein['price']:
#             kallein = tuote
#     print(f"Kallein tuote: {kallein['item']}")
#     print(f"On hinnaltaan: {kallein['price']}€")
#
#     kallein_item = lista[0]
#     kallein_hinta = kallein['price']
#     for tuote in tuotteet:
#         if tuote['price'] > kallein_hinta:
#             kallein_item = tuote
#             kallein_hinta = tuote['price']
#         return kallein_item, kallein_hinta
#
# lista = [
#     {'item': 'Apple', 'price': 1.8},
#     {'item': 'Banana', 'price': 3.1},
#     {'item': 'Orange', 'price': 2.5},
# ]
#
#
# kallein = etsi_kallein(lista)
# print(f"Kallein tuote: {kallein[0]['item']}")
# print(f"On hinnaltaan: {kallein[1]}€")
#
# # Haluttu tulos:
# # Kallein tuote: Banana
# # On hinnaltaan: 3.1€
#
#
# # etsi_kallein(lista)

def listalle(numbers):
    numbers = list(range(1, numbers + 1))

    lista = []
    for x in numbers:
        if x % 2 != 0:
            x = x + 1
            lista.append(x)
    return lista


num = 7
into = listalle(num)
print(into)
