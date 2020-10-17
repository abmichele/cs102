import typing as tp


def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
    Encrypts plaintext using a Caesar cipher.

    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = ""
    plaintext = list(plaintext)  
    for var in plaintext:
        if ord('A')<=ord(var)<ord('Z') and ord('A')<=ord(var)+shift<=ord('Z'):
            newletter = chr(ord(var) + shift)
        elif ord(var)<ord('A') or ord('a')>ord(var)>ord('Z') or ord(var)>ord('z'):
            newletter=var
        elif var=="Z":
            newletter = chr(ord('A') + shift - 1)
        elif ord(var)<ord('Z') and ord(var)+shift>ord('Z'):
            newletter=chr(ord(var)+shift-26)
        elif ord(var)>=ord('a') and ord(var)<=ord('z'):
            if ord(var)+shift>ord('z'):
                newletter=chr(ord(var)+shift-26)
            else:
                newletter=chr(ord(var)+shift)
        ciphertext+=newletter
    return ciphertext

def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    """
    Decrypts a ciphertext using a Caesar cipher.

    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ""
    ciphertext=list(ciphertext)
    for var in ciphertext:
        if ord(var)-shift>=ord('A') and ord(var)<ord('Z'):
            newletter=chr(ord(var)-shift)
        elif ord(var)<ord('A') or ord('a')>ord(var)>ord('Z') or ord(var)>ord('z'):
            newletter=var
        elif ord(var)-shift<ord('A') and ord('A')<ord(var)<ord('Z'):
            newletter=chr(ord(var)-shift+26)
        elif ord(var)>=ord('a') and ord(var)-shift>=ord('a'):
            newletter=chr(ord(var)-shift)
        elif ord(var)>=ord('a') and ord(var)-shift<ord('a'):
            newletter=chr(ord(var)-shift+26)
        
        plaintext+=newletter
    return plaintext


d = {"python", "java", "ruby"}
def caesar_breaker_brute_force(ciphertext: str, dictionary: tp.Set[str]) -> int:
    """
    Brute force breaking a Caesar cipher.
    """
    best_shift = 0
    ciphertext=list(ciphertext.lower)
    for word in dictionary:
        word=list(word)
        if ciphertext == word:
            best_shift=0
        else:
            a=ord(ciphertext[0])-ord(word[0])
            b=ord(ciphertext[1])-ord(word[1])
            if a < 0:
                a+=26
            if b < 0:
                b+=26
            if a==b:
                best_shift=a
    return best_shift
