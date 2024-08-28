butacas = [True, False, True, False, True, False]

desocupadas = 0
for butaca in butacas:
    if not butaca:
        desocupadas = desocupadas + 1

print("Hay ", desocupadas, " butacas desocupadas.")