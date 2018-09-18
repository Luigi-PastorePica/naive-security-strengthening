import hashlib
import bitstring

m = hashlib.sha512()
m.update("Nobody inspects")
l = m.copy()
print m     # Hash object info
print l     # Hash object copy info
for n in range (100):
    m.update(" the spammish repetition")
# print 'This is the digest method'
# print m.digest()
print 'This is the hexdigest method'
print m.hexdigest()              # Return the digest of the strings passed to the update() method so far. This is a string of digest_size bytes which may contain non-ASCII characters, including null bytes.
print l.hexdigest()

print 'This is the digest_size method'
print m.digest_size     # The size of the resulting hash in bytes.
print l.digest_size
print 'This is the block_size method'
print m.block_size      # The internal block size of the hash algorithm in bytes.
print l.block_size
# print hashlib.algorithms
# print hashlib.algorithms_guaranteed
# print hashlib.algorithms_available

a = bitstring.BitArray(bin='1101000011110100') # Can also be written as (0b1101......)
print
print a.hex

b = bitstring.BitArray(hex=m.hexdigest())
print b.hex
print b
print b.bytes

