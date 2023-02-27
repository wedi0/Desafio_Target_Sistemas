sp = 67836.43
rj = 36678.66
mg = 29229.88
es = 27165.48
outros = 19849.53

# 100% do faturamento é igual ao valor total somado. 
total = sp + rj + mg + es + outros

# Representação que cada estado teve dentro do valor total mensal da distribuidor:
print(f"O estado de SP participa {((sp * 100)/total):.2f}%")
print(f"O estado de RJ participa {((rj * 100)/total):.2f}%")
print(f"O estado de MG participa {((mg * 100)/total):.2f}%")
print(f"O estado de ES participa {((es * 100)/total):.2f}%")
print(f"Os outros estados participam {((outros * 100)/total):.2f}%")