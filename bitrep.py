from cryptography.fernet import Fernet
from bitstring import BitArray, BitStream
from clipboard import copy, paste                 # Used for demonstrative purposes only
from os import urandom

# Hard coded file path copied to clipboard. Used for demonstrative purposes only


class BitRep(object):

    def __init__(self, position_list = None,
                 position_list_size = 4, word_length = 8):

        self.word_len = word_length
        if position_list is None:
            self.pos_list = self.list_gen(self.pos_size)
            self.pos_size = position_list_size
        elif hasattr(position_list, '__iter__'):
            for elem in position_list:
                if isinstance(elem, (int, long)):
                    if elem < self.word_len:
                        pass
                    else:
                        raise ValueError("Value is larger than word_length")
                else:
                    raise TypeError("Non-integer value in position_list")
            self.pos_list = position_list
            self.pos_size = len(self.pos_list)
        else:
            raise TypeError("position_list type should be iterable or NoneType object")

    def list_gen(self, list_size):
        bit_pos = []
        while len(bit_pos) < list_size:
            pos = ord(urandom(1)) % self.word_len
            if pos not in bit_pos:
                bit_pos.append(pos)
            else:
                pass
        return bit_pos

    def bit_rep(self, file_path):
        key = Fernet.generate_key()
        f = Fernet(key)
        offsite_bits = BitStream()
        with open (file_path,'rb') as file:
            token = f.encrypt(file.read())
            data_stream = BitStream(bytes=token)
            # traverse all of the data stream in steps of size word_length
            # While data_stream.cut(word_length) is probably more efficient, value of n is useful here
            for n in range(0, len(data_stream), self.word_len):
                for m in range(0, self.word_len):
                    if m in self.pos_list:
                        if data_stream[n+m] is True:
                            offsite_bits.append('0b1')
                        else:
                            offsite_bits.append('0b0')
                            # Using urandom because of cryptographic security and because it is supported on major OSs
                            # Replaces the bits at bit_pos (within each word) with randomly generated bits.
                        data_stream.overwrite(bin(ord(urandom(1)) % 2), m+n)
        return data_stream, offsite_bits, key

    def bit_back(self, data_stream, offsite_bits, key):
        f = Fernet(key)
        for n in range (0, len(data_stream), self.word_len):
            for m in range (0, self.word_len):
                if m in self.pos_list:
                    data_stream.overwrite(offsite_bits.read(1), m+n)

        return f.decrypt(data_stream.bytes)


bit_pos_test = [1, 3, 5, 7]

rep = BitRep(position_list=bit_pos_test)

token, rem_bits, pswrd = rep.bit_rep("secret_message.txt")

orig_file = rep.bit_back(token, rem_bits, pswrd)

print token.bin
print
print rem_bits.bin
print
print pswrd
print
print orig_file

# rep2 = BitRep(position_list_size=4, word_length=8)

rep01 = rep.bit_rep("secret_message.txt")
rep02 = rep.bit_rep("secret_message_2.txt")
rep03 = rep.bit_rep("secret_message_3.txt")
rep04 = rep.bit_rep("secret_message_4.txt")
word_length = 8
the_list = [rep01, rep02, rep03, rep04]

def xor(p, q):
    if p != q:
        return True
    else:
        return False

guess_bits = BitStream(length=word_length)

for elem in the_list:
    hack_token = BitStream(bytes=elem[0])
    for n in range(word_length):
        if xor(guess_bits[n], hack_token[n]):
            guess_bits[n] = '0b1'
            print "here"
        else:
            guess_bits[n] = '0b0'


print guess_bits.bin



