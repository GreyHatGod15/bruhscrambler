#Copyright 2022 LegenDrags

# Permission is hereby granted, free of charge, to any person
# obtaining a copy of this software and associated documentation 
# files (the "Software"), to deal in the Software without restriction, 
# including without limitation the rights to use, copy, modify, merge,
# publish, distribute, sublicense, and/or sell copies of the Software, 
# and to permit persons to whom the Software is furnished to do # 
# so, subject to the following conditions:

# The above copyright notice and this permission notice shall be 
# included in all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF 
# ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT 
# LIMITED TO THE WARRANTIES OF MERCHANTABILITY, 
# FITNESS FOR A PARTICULAR PURPOSE AND 
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR 
# COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES 
# OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, 
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN 
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER 
# DEALINGS IN THE SOFTWARE.

# Hello There, thanks for checking this out.
# You are free to modify or publish this but credits please.
# Alse include this license document.

# This algorithm checks if a word "helloworld" is in the scrambled word "lohesgwballdorlsaqvsw"
# Ofcourse the above is an example

# This method works by storing how many times a letter has appeared in the scrambled word
# and checking if the required word's data matches with this.
# Returns True or False depending on the result.
# Average Speed: 0.001 seconds (tested on arch linux)

# Stored Data Example:
# Scrambled Word: abkbabk
# Word to check: baka
# Times a letter has appeared in scrambled word
# times = {
# 	"a": 2,
# 	"b": 3,
#	 "k": 2
# }
# Times a letter has appeared in required word
# wtimes stands for word_times
# wtimes = {
# 	"a": 2,
# 	"b": 1,
# 	"k": 1
# }
# Since the required word's letters are in the Scrambled word's letters, its a match

def unscramble(scrambled, word):
	# Create lists for detected letters, unique letters, and times appeared
	det_let = []
	unique = []
	times = {}
	# Iterate through the scrambled word
	for letter in scrambled:
		# if the letter has not already appeared
		if not letter in det_let:
			# append it to the uniques
			unique.append(letter)
		# add the letter to the detected letters list
		det_let.append(letter)
	# Iterate through the detected letters list
	for letter in det_let:
		# creating key and value pairs for letter
		# to prevent errors, we do the try except
		try:
			# this pulls an Exception if this is the first loop
			times[letter]
		except KeyError:
			# if it is the first loop, assign the key and value pair
			times[letter] = 0
		# increment the value for the appeared letter
		times[letter] += 1
	
	# the same thing for required word
	wdet = [] # detected letters in word
	wunique = [] # unique letters in word
	wtimes = {} # number of times a letter has appeared in word
	# Iterate through the required word 
	for letter in word:
		# if the letter has not appeared before
		if not letter in wdet:
			# add it to the unique letters
			wunique.append(letter)
		# else add it to the detected letters list
		wdet.append(letter)
	# Iterate through the detected letters 
	for letter in wdet:
		# make key and value pairs 
		try:
			# check if this is first loop
			wtimes[letter]
		except KeyError:
			# if it is first loop assign the new key and value pairs 
			wtimes[letter] = 0
		# increment the value of the detected letter
		wtimes[letter] += 1
	
	# final checking
	res = True
	# Iterate through the detected letters in required word 
	for letter in wdet:
		# if letter is in scrambled word
		if letter in unique:
			try:
				# check if the required number of letters are in scrambled word
				if not times[letter] >= wtimes[letter]:
					# if there arent, we know the word isn't in scrambled
					# make result False
					res = False
					# exit for loop
					break
			# if the letter isnt there in scrambled word ( this wont happen tho)
			except KeyError:
				# same thing, exit for loop with False result 
				res = False
				break
		else:
			# if letter isnt there in scrambled word, exit for loop
			res = False
			break
	# return final result
	return res


# Example
def main():
	# random huge scrambled word ( read the Scrambled word pls)
	scrambled = "icallthisthebruhunscramblingmethodbecauseitdoessussythingsthedevelopersnameisscrambledinthistextlolidontknowwhatimtypingtheremightbetyposopls"
	# totally random required word
	word = "dragsbruhakalegendrags"
	# get the unscramble result
	result = unscramble(scrambled, word)
	# print result
	print(result)

if __name__ == "__main__":
	# import time ( very very important to show time taken )
	import time
	# store start time
	start = time.time()
	# call main()
	main()
	# store end time
	end = time.time()
	# show time taken
	print("Executed in",end-start, "seconds")
