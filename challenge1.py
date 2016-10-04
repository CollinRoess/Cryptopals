'''	Cryptopals Crypto Challenge
	Set 1
	Challenge 1
	Convert hex to base64
	Collin Roess
	10/4/2016
'''

''' This does not work yet. It's a work in progress. 

import binascii
import base64
string=input()
byte=bytes(string, 'utf-8')

hex=binascii.hexlify(byte)
sixfour= base64.b64encode(hex, altchars=None)
print (sixfour)

'''