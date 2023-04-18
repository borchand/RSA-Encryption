import math as m
import numpy as np
import random as r

class RSA:
    def __init__(self, min:int = 10, max:int = 100):

        self.d_calc = lambda : m.fmod(m.fmod(self.e, self.k) * m.fmod(self.d, self.k), self.k)
        self.encrypt_letter = lambda letter_as_num: np.mod(pow(letter_as_num, self.e), self.n)
        self.decrypt_letter = lambda encrypted_letter: np.mod(pow(int(encrypted_letter), int(self.d)), self.n)
        self.min = min
        self.max = max

        self.create_keys()
    
    def check_prime(self, n : int):
        """
        Check if a number is prime or not
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
        Return a list of prime numbers between min and max
        """
        
        return [i for i in range(min, max+1) if self.check_prime(i)]
    
    def determine_e(self):
        """
        Determine e
        """
        primes = self.find_primes(3, self.n)
        
        for i in primes:
            if m.gcd(i, self.k) == 1:
                self.e = i
                return self.e

    def find_d(self):
        """
        Find d
        """
        i = 0
        self.d = round((1 + i * self.k) / self.e)

        while self.d_calc() != 1:
            i += 1
            self.d = round((1 + i * self.k) / self.e)

    def selected_primes(self):
        return self.p, self.q

    def create_keys(self):
    
        primes = self.find_primes(self.min, self.max)
        

        self.p = primes.pop(r.randint(0, len(primes)-1))
        self.q = primes.pop(r.randint(0, len(primes)-1))

        self.k = (self.p - 1) * (self.q - 1)

        self.n = self.p * self.q
        self.determine_e()
        self.find_d()

    def encrypt(self, mes : str):
        """
        Encrypt a message
        """

        encrypted_mes = []
        for letter in mes.lower():
            letter_as_num = ord(letter)
            encrypted_letter = self.encrypt_letter(letter_as_num)
            encrypted_mes.append(encrypted_letter)
        
        self.encrypted_mes = encrypted_mes

        return self.encrypted_mes
    
    def decrypt(self):
        """
        Decrypt a message
        """

        self.decrypted = ""

        for encrypted_letter in self.encrypted_mes:

            decrypt_chunk = self.decrypt_letter(encrypted_letter)
            self.decrypted += chr(decrypt_chunk)
        
        return self.decrypted

if __name__ == "__main__":
    rsa = RSA(100, 200)
    print("Selected primes:", rsa.selected_primes())

    mes = "hello world!"
    print("Message:", mes)
    print("Encrypted message:", rsa.encrypt(mes))
    print("Decrypted message:", rsa.decrypt())