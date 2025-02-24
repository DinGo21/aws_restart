def	isPrime(n):
	i = 2

	while i < n:
		if n % i == 0:
			return 0
		i += 1
	return 1

def	printPrimes():
	outfile = open("result.txt", 'w')

	for i in range(1, 251):
		if isPrime(i):
			outfile.write(str(i) + '\n')
	outfile.close()

if __name__ == "__main__":
	printPrimes()
