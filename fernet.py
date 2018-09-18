from cryptography.fernet import Fernet
from bitstring import BitArray, BitStream
from sys import getsizeof

key = Fernet.generate_key()
f = Fernet(key)
print "This is the key"
print key
# token1 = f.encrypt(b"a secret")
# token2 = f.encrypt(b"a secret message that keeps growing and growing")
with open("/Volumes/Transcend/Twilit_Zero/Dropbox/Luigi A/LaGuardia/Spring I 2016/MAC 283/MAC283 Project/secret_message.txt", "r") as file:
    token3 = f.encrypt(file.read())
    print type(file.read())
# print "The first token is: "
# print len(token1)
# print token1
# print "The second token is: "
# print len(token2)
# print token2
print "The third token is: "
print len(token3)
print getsizeof(token3)
print token3

# print f.decrypt(token1)
# print f.decrypt(token2)
print f.decrypt(token3)
a = BitStream(bytes=token3)
print f.decrypt(a.bytes)
