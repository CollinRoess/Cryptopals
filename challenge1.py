'''	Cryptopals Crypto Challenge
	Set 1
	Challenge 1
	Convert hex to base64
	Collin Roess
	10/4/2016
'''



import binascii
import base64
string=binascii.unhexlify(bytes(input(), 'utf-8'))


encoded = binascii.b2a_base64(string)
print (encoded)


''' 
Example:

String:

	49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d

Should Produce:

	SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t

'''