def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.

    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext, plaintext, keyword, m = "", list(plaintext), list(keyword.lower()), 0
    while len(keyword) < len(plaintext):
        keyword += keyword
    for letter in plaintext:
        encletter = keyword[m]  
        move = ord(encletter) - ord('a')
        newletter = ord(letter) + move
        if ord('A') <= newletter <= ord('Z') and ord('A') <= ord(letter) <= ord('Z') or ord('z') >= newletter >= ord('a') and ord('z') >= ord(letter) >= ord('a'):
            ciphertext += chr(newletter)
        elif newletter > ord ('Z') and ord('A') <= ord(letter) <= ord('Z') or newletter > ord('z') and ord('a') <= ord(letter) <= ord('z'):
            ciphertext += chr(newletter-26)
        elif ord(letter) < ord('A') or ord('Z') < ord(letter) < ord('a') or ord(letter) > ord('z'):
            ciphertext += letter
        m += 1
    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.

    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext, ciphertext, keyword, m = "", list(ciphertext), list(keyword.lower()), 0
    while len(keyword)<len(ciphertext):
        keyword += keyword
    for letter in ciphertext:
        encletter  = keyword[m]  
        move = ord(encletter)-ord('a')
        newletter = ord(letter)-move

        if ord('A') <= newletter <= ord('Z') and ord('A') <= ord(letter) <= ord('Z') or ord('z') >= newletter >= ord('a') and ord('z') >= ord(letter) >= ord('a'):
            plaintext += chr(newletter)
        elif ord(letter) < ord('A') or ord('Z') < ord(letter) < ord('a') or ord(letter) > ord('z'):
            plaintext += letter
        elif newletter < ord ('A') and ord ('A') <= ord(letter) <= ord('Z') or  newletter < ord('a') and ord('a')<=ord(letter)<=ord('z'):
            plaintext += chr(newletter+26)
        m += 1
    return plaintext
