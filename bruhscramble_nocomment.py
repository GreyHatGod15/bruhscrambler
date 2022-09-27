def unscramble(scrambled, word):
	det_let = []
	unique = []
	times = {}
	for letter in scrambled:
		if not letter in det_let:
			unique.append(letter)
		det_let.append(letter)
	for letter in det_let:
		try:
			times[letter]
		except KeyError:
			times[letter] = 0
		times[letter] += 1
	
	wdet = []
	wunique = []
	wtimes = {}
	for letter in word:
		if not letter in wdet:
			wunique.append(letter)
		wdet.append(letter)
	for letter in wdet:
		try:
			wtimes[letter]
		except KeyError:
			wtimes[letter] = 0
		wtimes[letter] += 1
	
	res = True
	for letter in wdet:
		if letter in unique:
			try:
				if not times[letter] >= wtimes[letter]:
					res = False
					break
			except KeyError:
				res = False
				break
		else:
			res = False
			break
	return res


def main():
	scrambled = "icallthisthebruhunscramblingmethodbecauseitdoessussythingsthedevelopersnameisscrambledinthistextlolidontknowwhatimtypingtheremightbetyposopls"
	word = "dragsbruhakalegendrags"
	result = unscramble(scrambled, word)
	print(result)

if __name__ == "__main__":
	import time
	start = time.time()
	main()
	end = time.time()
	print("Executed in",end-start, "seconds")
