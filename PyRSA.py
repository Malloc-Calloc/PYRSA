from random import randint, randrange
def IS_PRIME(n):#Miller-Rabin primality check.
	k=10
	def check(a, s, d, n):
		x = pow(a, d, n)
		if x == 1:
			return True
		for i in xrange(s - 1):
			if x == n - 1:
				return True
			x = pow(x, 2, n)
		return x == n - 1
	s = 0
	d = n - 1

	while d % 2 == 0:
		d >>= 1
		s += 1
	for i in xrange(k):
		a = randrange(2, n - 1)
		if not check(a, s, d, n):
			return False
	return True
def KEYGEN():
	Key_P = randint(2**1023, 2**1024)#Initial pseudorandom value of P
	Key_Q = randint(2**1020, 2**1021)#Initial pseudorandom value of Q
	while not IS_PRIME(Key_P):#Primality check for P using IS_PRIME function
		Key_P = randint(2**1023, 2**1024)#Recalculation of pseudorandom value of P if not prime.
	while not IS_PRIME(Key_Q):#Primality check for Q using IS_PRIME function
		Key_Q = randint(2**1023, 2**1024)#Recalculation of pseudorandom value of Q if not prime.
	Key_N = Key_P * Key_Q#Calculation of n.
	Key_PhiN = (Key_P - 1) * (Key_Q - 1)#Calculation of phi(n).
	Key_E = randint(2, (Key_PhiN - 1))#Initial pseudorandom value of e.
	while not IS_PRIME(Key_E):#Primality check for E using IS_PRIME function.
		Key_E = randint(2, (Key_PhiN - 1))#Recalculation of pseudorandom value of e.
	OldRemainder = Key_E#Set OldRemainder to be equil to e.
	Remainder = Key_PhiN#Set Remainder to be equil to Phi of n.
	i = 0#Bezout coefficient variable, inital value.
	Oldi = 1#Previous value Bezout coefficient variable, inital value.
	while Remainder:#While a non-zero remainder is found in the long division below.
		OldRemainder, (Q, Remainder) = Remainder, divmod(OldRemainder, Remainder)#Paralell assignment of Q equals the quotient of the pair OldRemainder & Remainder via long division and OldRemainder now equals Remainder.
		i, Oldi = Oldi - Q*i, i#Paralell assignment Oldi equals i and i equals Oldi minus Q multiplied by i.
	Key_D = (Oldi % Key_PhiN)#Final calculation of d.
	return (Key_N, Key_E, Key_D)#Return values to be used as private and public keys.
def MAIN():
	Plain_Text = "Hello World"#Plain text.
	Bytes_Plain_Text = str.encode(Plain_Text)#Plain text converted to bytes.
	Int_Plain_Text = int(Bytes_Plain_Text.encode('hex'), 16)#Plain text converted to Integer for printing.
	Key_N, Key_E, Key_D = KEYGEN()#Generate RSA keys.
MAIN()
