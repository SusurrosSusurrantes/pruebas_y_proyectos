#ingresa los nombres acá

nombres=["Alexander", "Zambrano", "Villegas"]

def ord_alf(cadena):
	alfabeto={
		"A": 1, "a": 1, "á": 1,
		"B": 2, "b": 2,
		"C": 3, "c": 3,
		"D": 4, "d": 4,
		"E": 5, "e": 5, "é":5,
		"F": 6, "f": 6,
		"G": 7, "g": 7,
		"H": 8, "h": 8, "í":8,
		"I": 9, "i": 9,
		"J": 10, "j": 10,
		"K": 11, "k": 11,
		"L": 12, "l": 12,
		"M": 13, "m": 13,
		"N": 14, "n": 14,
		"Ñ": 15, "ñ": 15,
		"O": 16, "o": 16, "ó":16,
		"P": 17, "p": 17,
		"Q": 18, "q": 18,
		"R": 19, "r": 19,
		"S": 20, "s": 20,
		"T": 21, "t": 21,
		"U": 22, "u": 22, "ú":22,
		"V": 23, "v": 23,
		"W": 24, "w": 24,
		"X": 25, "x": 25,
		"Y": 26, "y": 26,
		"Z": 27, "z": 27,
	}

	codigos=[]
	for letra in cadena:
		codigos.append(alfabeto[letra])
	return codigos

nombres.sort(key=ord_alf)

print (nombres)