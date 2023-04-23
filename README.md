# SRP - RSA encryption

This is a project based on my <a href="https://github.com/borchand/RSA-Encryption/blob/main/%20srp-2020.pdf">SRP</a> (specialised study project) from Danish high school. The code implementation can be fund under the folder <a href="https://github.com/borchand/RSA-Encryption/tree/main/python_code">python_code</a>.


## RSA encryption
RSA encryption is developed by Ron Rivest, Adi Shamir and Len Adleman in 1977. It is based on the prime factorization problem. In order to encrypt and decrypt, two public keys🔑🔑 ($n$, $e$) and a private key🔐 $d$ is needed. They can be fund by the following steps:

1) Choose two prime numbers $p$ and $q$, the set $n=p\cdot q$
2) Calculate $\phi(n) = (p - 1)(q - 1)$
3) Choose a whole number, so $0 < e <\phi(n)$ and $\text{gcd}(e, \phi(n)) = 1$
4) Calculate $d$ so, $ed \equiv 1 (\text{mod } \phi(n))$
  
Now that the keys are fund, we can use them to encrypt. As follows
```math
c = m^e (\text{mod } n)
```
where $m$ is the messeage and $0 < m < n$. Note that $m$ needs to be smaller than $n$. This is why my implementation of RSA splits each sentence into individual letter.

When decrypting we use

```math
m = c^d (\text{mod } n)
```

Why does this work? Let start by substituting $c$ in when calculating $m$

```math
m = c^d (\text{mod } n) = (m^e (\text{mod } n))^d (\text{mod } n)
```
This can be written as

```math
m = m^{ed}(\text{mod } n)
```
Since $\text{gcd}(m, n) = 1$, we can rewrite $m$ as
```math
m = m^{ed(\text{mod } \phi(n))}(\text{mod } n)
```

The key $d$ is chosen such that $ed \equiv 1 (\text{mod } \phi(n))$. This can also be written as $ed(\text{mod } \phi(n)) = 1$.
Therefore we can now write

```math
m = m^{1}(\text{mod } n) = m (\text{mod } n)
```
This only applies when $\text{gcd}(e, \phi(n) = 1)$.

## The prime factorization problem
To break the RSA encryption we need to find the private key $d$, which is calculated based on $e$ and $\phi(n)$. Luckily we know the $e$ as it is a public key. So, we "only" need to find $\phi(n)$. We know $\phi(n) = (p-1)(q-1)$. This means we need to find $p$ and $q$ in order to find $\phi(n)$. This is where the other key $n$ comes into play. We know
```math
n = p\cdot q
```
We can use Fermat's method to find $p$ and $q$. Fermat's method tells us that $n$ is an uneven whole number, that can factorized only if there is a solution to $n = x^2-y^2$ where $x$ and $y$ must be whole numbers. Since $x$ and $y$ ar whole number $n$ can be written as

```math
n = x^2-y^2 = (x+y)(x-y)
```
To find $x$ and $y$ we use

```math
x^2 - n = y^2
```
When a solution where $x$ and $y$ are whole numbers is fund, we can now find $p$ and $q$
```math
n = (x+y)(x-y) = p\cdot q \Rightarrow p = x+y \wedge q = x-y
```

