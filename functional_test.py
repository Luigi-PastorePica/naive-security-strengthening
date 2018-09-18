from cryptography.fernet import Fernet
from bitstring import BitArray, BitStream
from clipboard import copy, paste                 # Used for demonstrative purposes only
from os import urandom


copy("secret_message.txt")

# fpath = raw_input("Please input file path ")
fpath = "secret_message.txt"
word_length = 8

key = Fernet.generate_key()
f = Fernet(key)
bit_pos_test = [1, 3, 5, 7]      # Hardcoded positions. Demonstrative purposes.
                            # Should generate them automatically
offsite_bits = BitStream()
# print "offsite bits"
# print offsite_bits.bin

with open(fpath, 'rb') as file:
    token = f.encrypt(file.read())
    print
    # print "Token"
    # print
    # print token
    # print
    # print
    # print "Key"
    # print
    # print key
    # print
    # print
    # print "Original message"
    # print
    # print f.decrypt(token)
    data_stream = BitStream(bytes=token)
    i = 0
    # print 'encrypted token'
    print "Original token in binary"
    print
    print data_stream.bin
    # traverse all of the data stream in steps of size word_length
    # While data_stream.cut(word_length) is probably more efficient, value of n is useful here
    for n in range(0, len(data_stream), word_length):
        # print str(data_stream.read(word_length)) + " " + str(i)
        # i += 1
        for m in range(0, word_length):
            # print n, m
            if m in bit_pos_test:
                # print data_stream[n+m]  #debugging
                if data_stream[n+m] is True:
                    offsite_bits.append('0b1')
                else:
                    offsite_bits.append('0b0')
                # Using urandom because of cryptographic security and because it is supported on major OSs
                # Replaces the bits at bit_pos (within each word) with randomly generated bits.
                data_stream.overwrite(bin(ord(urandom(1)) % 2), m+n)
    print
    print "Exchanged bits token"
    print
    print data_stream.bin
    print
    # f.decrypt(data_stream.bytes)
    print "Stored bits"
    print
    print offsite_bits.bin

    for n in range (0, len(data_stream), word_length):
        for m in range (0, word_length):
            if m in bit_pos_test:
                data_stream.overwrite(offsite_bits.read(1), m+n)
    # print f.decrypt(data_stream.bytes)
