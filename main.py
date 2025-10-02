"""TP Palindromes, 02.10"""

import unicodedata
import string

#### Fonction secondaire

def ispalindrome(p : str) -> bool :
    """Renvoie si oui on non p est un palindrome"""
    # supprime les accents
    se = ''.join(c for c in unicodedata.normalize('NFD', p)
        if unicodedata.category(c) != 'Mn')
    #supprime la ponctuation
    se = ''.join(c for c in se if c not in string.punctuation)
    # supprime les espaces et met tout en minuscule
    se = se.replace(" ", "").lower()
    n = len(se)
    for i in range(n//2): # on s'arrête à la moitié de la chaîne
        if se[i] != se[-i-1]: # vérifie si la première et la dernière lettre sont les mêmes
            return False
    return True

#### Fonction principale

def main():
    """Vérifie quelques palindromes"""
    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie"]:
        print(s, ispalindrome(s))


if __name__ == "__main__":
    main()
