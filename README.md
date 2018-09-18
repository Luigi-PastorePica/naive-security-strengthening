# naive-security-strengthening
This is naive approach to a secondary level of protection on already encrypted data. 

It stores certain bits of the encrypted data in a separate file, which should be stored safely and in a different device. At the same time, the positions of those bits in the original encrypted file are filled with garbage. In this way, using the encryption key on the encrypted file will yield no useful data to an attacker. Only when the removed bits are placed in their proper position on the encrypted file will the data become "decryptable".
