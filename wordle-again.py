target = [None] * 5
wrong_space = {}
for i, result in enumerate(result_array):
	for j, state in enumerate(result):
		if state == ['absent', 'notguessed']:
			continue
		letter = guesses[i][j]
		if state == 'correct':
			target[j] = letter
		elif state == 'present':
			spaces = wrong_space.get(letter, [])
			spaces.append(j)
			wrong_space[letter] = spaces


