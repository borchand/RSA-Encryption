import math as m
import numpy as np

# `d_calc` is a lambda function that calculates the value of `(e*d) mod k`, where `e` and
# `d` are the public and private keys respectively, and `k` is the totient of `n`. This value
# is used in the process of finding the private key `d`.
d_calc = lambda e, k, d: m.fmod(m.fmod(e, k) * m.fmod(d, k), k)


# `encrypt_letter` is a lambda function that takes in a letter represented as a number
# (ASCII code) and encrypts it using the RSA algorithm. It does this by raising the letter to
# the power of the public key `e` and taking the modulus of the result with `n`. The resulting
# value is the encrypted letter.
encrypt_letter = lambda letter_as_num, e, n: np.mod(pow(letter_as_num, e), n)

# `decrypt_letter` is a lambda function that takes in an encrypted letter (represented as
# a number) and decrypts it using the RSA algorithm. It does this by raising the encrypted
# letter to the power of the private key `d` and taking the modulus of the result with `n`.
# The resulting value is the decrypted letter (represented as a number).
decrypt_letter = lambda encrypted_letter, d, n: np.mod(pow(int(encrypted_letter), int(d)), n)



def find_d(k:int, e:int):
        """
        This function finds the value of d by iterating through a formula until a certain condition is met.
        """
        
        i = 0
        d = round((1 + i * k) / e)

        while d_calc(e, k, d) != 1:
            i += 1
            d = round((1 + i * k) / e)

        return d


