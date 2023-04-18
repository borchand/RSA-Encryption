import math as m
import numpy as np
import math

def check_prime(n : int):
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

def find_primes(min : int, max : int):
    """
    Return a list of prime numbers between min and max
    """
    
    return [i for i in range(min, max) if check_prime(i)]

def determine_e(k, n):
    """
    Determine e
    """
    primes = find_primes(3, n)
    
    for i in primes:
        if m.gcd(i, k) == 1:
            return i

def find_d(e, k):
    """
    Find d
    """
    
    i = 0
    d = round((1 + i * k) / e)

    while m.fmod(m.fmod(e,k)*m.fmod(d,k),k) != 1:
        i += 1
        d = round((1 + i * k) / e)
    return d
    
def create_keys(min : int, max : int):
    
    primes = find_primes(min, max)
    
    p = primes.pop()
    q = primes.pop()

    print("p", p, "q", q)
    k = (p - 1) * (q - 1)
    
    e = determine_e(k, min)

    d = find_d(e, k)

    return d, e, k

def encrypt(mes : str, min : int, max : int):
    """
    Encrypt a message
    """
    
    d, e, k = create_keys(min, max)
    
    num_mes = []
    for i in mes.lower():
        if ord(i) == 32: # space
            num_mes.append('32')
        elif ord(i) < 96 or ord(i) > 96 + 26: # special characters
            num_mes.append(99)
        else: # letters
            word_num = ord(i) - 96
            if word_num  < 10:
                num_mes.append('0' + str(word_num))
            else:
                num_mes.append(word_num)
    
    if len(num_mes) % 2 != 0:
        num_mes.append('32')
        
    encrypted = []

    for i in range(0, len(num_mes), 2):
        m = str(num_mes[i]) + str(num_mes[i+1])
        encrypted_m = np.power(int(m), e) % k
        encrypted.append(encrypted_m)
        
    return encrypted, d, e, k
   
def decrypt(encrypted, d, n):
    """
    Decrypt a message
    """
    
    decrypted = ""
    for i in encrypted:
        print(i)
        decrypted_m = np.mod(np.power(int(i), d),n)
        if decrypted_m < 1000:
            decrypted_m = '0' + str(decrypted_m)
        # split the decrypted message into two parts
        print(decrypted_m)
        decrypted_m1 = int(str(decrypted_m)[:2])
        decrypted_m2 = int(str(decrypted_m)[2:])
        print(decrypted_m1, decrypted_m2)
        print(decrypt_letter(decrypted_m1), decrypt_letter(decrypted_m2))
        decrypted += decrypt_letter(decrypted_m1) + decrypt_letter(decrypted_m2)
        
    return decrypted

def decrypt_letter(num_letter):
    if num_letter == 32: # space
        return ' '
    elif num_letter == 99: # special characters
        return '#'
    else: # letters
        return chr(num_letter + 96)
def main():

    mes = 'hello world'
    print(mes)
    
    encrypted, d, e, n = encrypt(mes, 10, 100)

    
    decrypted = decrypt(encrypted, d, n)
    print(decrypted)
    # print("e", e, "d", d, "n", n)
    # me = np.mod(np.power(4, e), n)

    # print(me)

    # print(me**d)
    return

if __name__ == "__main__":
    main()