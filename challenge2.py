'''	Cryptopals Crypto Challenge
	Set 1
	Challenge 2
	Fixed XOR
	Collin Roess
	10/4/2016
'''



import binascii
import base64

string=int(input(), 16)
xorkey=int(input(), 16)

result=hex((string) ^ (xorkey))
print (result)

'''
Example:

	1c0111001f010100061a024b53535009181c
	
When XOR'd against:

	686974207468652062756c6c277320657965
	
Should produce:

	746865206b696420646f6e277420706c6179
	
'''