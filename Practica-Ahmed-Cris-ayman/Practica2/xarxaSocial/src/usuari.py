"""
Modul usuari.py
"""

def xifrat_cesar(text):

    resultat = ""
    for c in text:  
        if c.isalpha():
            base = ord('A') if c.isupper() else ord('a')
            resultat += chr((ord(c) - base + 2) % 26 + base)
        else:
            resultat += c
    return resultat


class Usuari:
 """
    Classe que representa un usuari d'una xarxa social.

    Exemple d'ús:

    >>> u = Usuari("Ayman", "ayman@mail.com", "1234")
    >>> u.nick
    'Ayman'
    >>> u.email
    'ayman@mail.com'
"""
   
def __init__(self, nick, email, password):
        self.nick = nick
        self.__email = email  
        self.__password = xifrat_cesar(password)
        self._posts = []
"""
        Constructor de la classe Usuari.

        :param nick: nom d'usuari
        :param email: correu electrònic
        :param password: contrasenya
"""
def get_email(self):
 """
        dona el email del usuari.

        >>> u=Usuari("Ayman", "ayman@mail.com", "1234")
        >>> u.get_email()
        'ayman@mail.com'
 """

   
 return self.__email

def set_email(self, nou_email):
        """
        Estableix un nou correu electrònic per a l'usuari.

        >>> u = Usuari("Ayman", "ayman@mail.com", "1234")
        >>> u.set_email("nou_email@mail.com")
        >>> u.get_email()
        'nou_email@mail.com'
        """
        self.__email = nou_email

def get_password(self):
        """
        Retorna la contrasenya xifrada de l'usuari.

        >>> u = Usuari("Ayman", "ayman@mail.com", "1234")
        >>> u.get_password()
        '1234'
        """
      
        return self.__password

def set_password(self, nou_password):
        """
        Estableix una nova contrasenya xifrada per a l'usuari.

        >>> u = Usuari("Ayman", "ayman@mail.com", "1234")
        >>> u.set_password("new_password")
        >>> u.get_password()
        'new_password'
        """
        self.__password = xifrat_cesar(nou_password)

def registra_post(self, post):
        """
        Registra una nova publicació per a l'usuari.

        >>> u = Usuari("Ayman", "ayman@mail.com", "1234")
        >>> u.registra_post("Primer post")
        >>> u.get_posts()
        ['Primer post']
        """
        
        self._posts.append(post)
        

def get_posts(self):
        """
        Retorna totes les publicacions de l'usuari.

        >>> u = Usuari("Ayman", "ayman@mail.com", "1234")
        >>> u.registra_post("Primer post")
        >>> u.get_posts()
        ['Primer post']
        """
        return self._posts

def __eq__(self, altre):
        """
        Compara dos usuaris per veure si tenen el mateix nom de l'usuari (nick).

        >>> u1 = Usuari("Ayman", "ayman@mail.com", "1234")
        >>> u2 = Usuari("Ayman", "other@mail.com", "abcd")
        >>> u1 == u2
        True
        >>> u3 = Usuari("Joan", "joan@mail.com", "1234")
        >>> u1 == u3
        False
        """
      
        return self.nick == altre.nick

def __str__(self):
        """
        Retorna una cadena amb la informació de l'usuari.

        >>> u = Usuari("Ayman", "ayman@mail.com", "1234")
        >>> u.set_email("nou_email@mail.com")
        >>> u.set_password("new_password")
        >>> u.registra_post("Primer post")
        >>> print(u)
        Usuari: Ayman
        Email: nou_email@mail.com
        Encrypted password: new_password
        Published posts:
        Primer post
        """
        info = "Usuari: " + self.nick
        info += " Email: " + self.__email
        info += " Encripted password: " + self.__password
        if self._posts:
            info += "\nPublished posts:"
            for p in self._posts:
                info += "\n" + str(p)
        return info


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    p1 = Usuari("AH39", "AH39@gmail.com", "penedeiman x eerin")
    p2 = Usuari("AHMED", "AH394@gmail.com", "penedeerin")
    print(p1)
    print(p2)
    p3 = Usuari("AH39", "AH3944@gmail.com", "domingoguapo")
    print(p3.nick)
    print(p1 == p3)
