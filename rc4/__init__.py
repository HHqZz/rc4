# Copyright (C) 2016 Jurriaan Bremer.
# See the file 'LICENSE.txt' for copying permission.

def rc4(data, key):                              # Crée une fonction nommée rc4 qui prend 2 arguments : une data et une clé.
    """RC4 encryption and decryption method."""  
    S, j, out = range(256), 0, []            #Defini simplement les variables S et j et out :  S est un ensemble de valeur de 0 a 255 ;
                                            # j est = 0 et out est un tableau vide .

    for i in range(256):  #pour i allant de 0 a 255 ;
        j = (j + S[i] + ord(key[i % len(key)])) % 256       # j ( qui est 0 ) prend la valeur de j + S[i]  ( cest a dire un nombre de 0 a 255)
        S[i], S[j] = S[j], S[i]                                 # + ord ( clé (passé en argument dans rc4)[i modulo la longeur de la clé])) modulo 256
                    # La fonction ord(...) retourne la valeur de l'identifiant numérique correspondant de son argument.
            #  ord("A") renvoie la valeur 65 car A est à la 65ieme position dans la table ASCII
            # # rf table ASCII :   http://www.asciitable.com/index/asciifull.gif

    i = j = 0  # on réinitialise les variables i et j
    for ch in data:   # ch n'a jamais été défini, ca m'etonnerait pas qu'il y ait une erreur ici ? sinon ch = charactere , donc
            # ch va parcouris data rentré en argument dans rc4
        i = (i + 1) % 256  #calcul pour i simple, pareil pour j...
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]  # Si je me trompe pas dans la syntaxe, S a la position i prend la valeur de S a la position j et inversement
        out.append(chr(ord(ch) ^ S[(S[i] + S[j]) % 256])) # signifie qu'on ajoute un charactere à la liste out déclarée dans la fonction rc4.
        #la fonction chr est l'inverse de ord. Avec chr on passe d'un entier comme 65 a sa lettre dans la table ascii A donc chr(65)=A .

    return "".join(out) # je comprends pas trop ce return et il est tres important ^^
# je suppose que le Main commence ici : 

if __name__ == "__main__":
    buf = rc4("Hello World", "rc4") # on utilise la fonction rc4  avec Hello world comme data et rc4 comme clé
    assert rc4(buf, "rc4") == "Hello World" # on rajoute une condition qui retourne faux si elle est pas verifiée
    print "Ran 1 test.." # print classique
