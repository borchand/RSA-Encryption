import math as m
import numpy as np
import random as r
import utils

# The RSA class is a Python implementation of the RSA encryption algorithm, which generates public and
# private keys for encrypting and decrypting messages.
class RSA:
    def __init__(self, min:int = 10, max:int = 100, e:int = None, d:int = None, n:int = None):
        """
        The function initializes an RSA encryption object with methods for encryption and decryption, and
        the ability to generate public and private keys.
        
        :param min: The minimum value for generating a random prime number in the RSA key generation
        process, defaults to 10
        :type min: int (optional)
        :param max: The maximum value for generating prime numbers in the RSA key generation process,
        defaults to 100
        :type max: int (optional)
        :param e: `e` is the public key used in the RSA algorithm for encryption. It is an integer value
        :type e: int
        :param d: `d` is the private key used in the RSA algorithm for decryption. It is calculated based on
        the values of `e` and `n`, and is kept secret by the owner of the private key
        :type d: int
        :param n: `n` is a positive integer that is the product of two large prime numbers. It is used as
        part of the RSA algorithm for encryption and decryption
        :type n: int
        """

        self.encrypt_letter = lambda letter_as_num:  utils.encrypt_letter(letter_as_num, self.e, self.n)
        self.decrypt_letter = lambda encrypted_letter: utils.decrypt_letter(encrypted_letter, self.d, self.n)
        
        self.min = min
        self.max = max
        if e and d and n:
            self.e = e
            self.d = d
            self.n = n
        else:
            self.create_keys()
    
    def check_prime(self, n : int):
        """
        This is a Python function that checks whether a given integer is a prime number or not.
        
        :param n: an integer that we want to check if it is a prime number
        :type n: int
        :return: The function is checking if the input integer `n` is a prime number or not. If `n` is a
        prime number, the function returns `True`. Otherwise, it returns `False`.
        """
        if n == 2:
            return True
        
        if n <= 1  or n % 2 == 0:
            return False

        for i in range(3, m.ceil(m.sqrt(n)) + 1, 2):
            if n % i == 0:
                return False
            
        return True

    def find_primes(self, min:int, max:int):
        """
        The function returns a list of prime numbers within a given range.
        
        :param min: The minimum value of the range of numbers to check for prime numbers
        :type min: int
        :param max: The "max" parameter is the maximum value up to which the function will search for prime
        numbers. The function will return a list of all prime numbers found between the "min" and "max"
        values (inclusive)
        :type max: int
        :return: a list of all prime numbers between the minimum and maximum values (inclusive) provided as
        arguments to the function. The function uses the `check_prime` method to determine if a number is
        prime or not.
        """
        
        return [i for i in range(min, max+1) if self.check_prime(i)]
    
    def get_keys(self):
        """
        The function returns a dictionary containing the values of "e", "d", and "n".
        :return: A dictionary containing the values of "e", "d", and "n" attributes of the object.
        """
  
        return {"e" : self.e, "d" : self.d, "n" : self.n}
    
    def determine_e(self):
        """
        This function determines the value of e by finding the first prime number greater than 2 that is
        coprime with k.
        :return: the value of the instance variable `self.e`.
        """

        primes = self.find_primes(3, self.n)
        
        for i in primes:
            if m.gcd(i, self.k) == 1:
                self.e = i
                return self.e

    def find_d(self):
        """
        This function finds the value of 'd' using the 'k' and 'e' values.
        :return: The function `find_d` is returning the value of `self.d`.
        """

        self.d = utils.find_d(self.k, self.e)
        return self.d

    def create_keys(self):
        """
        The function creates public and private keys for encryption and decryption using two prime numbers.
        """
    
        primes = self.find_primes(self.min, self.max)
        
        # choose two prime numbers
        self.p = primes.pop(r.randint(0, len(primes)-1))
        self.q = primes.pop(r.randint(0, len(primes)-1))

        # calculate k (φ(n))
        self.k = (self.p - 1) * (self.q - 1)
        # calculate n
        self.n = self.p * self.q

        self.determine_e()
        self.find_d()

    def encrypt(self, mes : str):
        """
        This function takes a string message as input, converts each letter to its corresponding encrypted
        letter using a helper function, and returns the encrypted message as a list of integers.
        
        :param mes: The parameter "mes" is a string that represents the message that needs to be encrypted.
        The method takes each letter of the message, converts it to its corresponding ASCII code using the
        ord() function, encrypts the letter using the encrypt_letter() method, and appends the encrypted
        letter to a list
        :type mes: str
        :return: The `encrypt` method returns the `encrypted_mes` list, which contains the encrypted version
        of the input message.
        """

        encrypted_mes = []
        for letter in mes.lower():
            letter_as_num = ord(letter)
            encrypted_letter = self.encrypt_letter(letter_as_num)
            encrypted_mes.append(encrypted_letter)
        
        self.encrypted_mes = encrypted_mes

        return self.encrypted_mes
    
    def get_encrypted_mes(self):
        """
        This function returns the encrypted message.
        :return: The method `get_encrypted_mes` is returning the encrypted message stored in the object's
        `encrypted_mes` attribute.
        """
        return self.encrypted_mes

    def decrypt(self, encrypted_mes = None):
        """
        This is a Python function that decrypts an encrypted message by iterating through each encrypted
        letter and using a helper function to decrypt it.
        
        :param encrypted_mes: The encrypted message that needs to be decrypted. It is an optional parameter
        and if not provided, the method will use the previously stored encrypted message
        :return: The decrypted message as a string is being returned.
        """

        self.decrypted = ""
        if encrypted_mes:
            self.encrypted_mes = encrypted_mes

        for encrypted_letter in self.encrypted_mes:

            decrypt_chunk = self.decrypt_letter(encrypted_letter)
            self.decrypted += chr(decrypt_chunk)
        
        return self.decrypted

if __name__ == "__main__":
    
    # The code is creating an instance of the RSA class with minimum and maximum values for generating
    # prime numbers, and then generating public and private keys using those prime numbers. It then
    # encrypts the message "hello world!" using the generated public key and prints the encrypted
    # message. It then decrypts the encrypted message using the generated private key and prints the
    # decrypted message.
    rsa = RSA(100, 300)

    keys = rsa.get_keys()
    print("Keys:", keys)
    
    mes = "hello world!"
    print("Message:", mes)
    print("Encrypted message:", rsa.encrypt(mes))
    print("Decrypted message:", rsa.decrypt())

    # This code is creating a new instance of the RSA class with the same public and private keys as the
    # original instance (using the `keys` dictionary obtained from the original instance), and then
    # decrypting the encrypted message obtained from the original instance by passing it as an argument to
    # the `decrypt` method of the new instance. The decrypted message is then printed.
    encrypted_mes = rsa.get_encrypted_mes()
    new_rsa = RSA(e=keys["e"], d=keys["d"], n=keys["n"])
    print(new_rsa.decrypt(encrypted_mes=encrypted_mes))