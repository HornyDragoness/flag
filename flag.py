def flag(N):
	class ArgumentError(Exception):
		pass

	if not isinstance(N, int) or N % 2 != 0 or N <= 0:
		raise ArgumentError("N should be an integer even number")

	# Creating the lines before the circle
	output_string = ('#' * (N * 3 + 2) + '\n')
	for i in range(int(N / 2)):
		output_string += ('#' + ' ' * (N * 3) + '#\n')

	# Creating first half of the circle
	for i in range(0, N, 2):
		output_string += ('#' + ('*' + 'o' * i + '*').center(3 * N, ' ') + '#\n')

	# Second half of the circle and the lines are mirrored
	output_string += output_string[-2::-1]

	return output_string
