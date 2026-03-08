"""
Modul xarxaSocial.py
"""

from usuari import Usuari
from post import  Post ,Hashtag 


class iTICApp:
    """
    Representa la xarxa social iTICApp.

    >>> i = iTICApp()
    >>> i.afegeix_usuari("AH39", "AH39@gmail.com", "hola")
    >>> i.afegeix_hashtag("cosas")
    >>> i.publicar_post("AH39", "zzz", "primer post")
    """

    def __init__(self):
        self.__usuaris = {}
        self.__posts = {}
        self.__hashtags = {}

    def afegeix_usuari(self, nick, email, password):
        """
        >>> i = iTICApp()
        >>> i.afegeix_usuari("AH39", "AH39@gmail.com", "hola")
        >>> i.afegeix_usuari("AH39", "AH39@gmail.com", "hola")
        Error: ja existeix un usuari amb aquest nick
        """
        if nick in self.__usuaris:
            print("Error: ja existeix un usuari amb aquest nick")
        else:
            self.__usuaris[nick] = Usuari(nick, email, password)

    def afegeix_hashtag(self, id):
        """
        >>> i = iTICApp()
        >>> i.afegeix_hashtag("XXXX")
        >>> i.afegeix_hashtag("XXXX")
        Error: ja existeix aquest hashtag
        """
        if id in self.__hashtags:
            print("Error: ja existeix aquest hashtag")
        else:
            self.__hashtags[id] = Hashtag(id)

    def publicar_post(self, nick, id_hashtag, contingut_post):
        """
        >>> i = iTICApp()
        >>> i.afegeix_usuari("AH39", "AH39@gmail.com", "hola")
        >>> i.afegeix_hashtag("YYYY")
        >>> i.publicar_post("AH39", "adventure", "primer post")
        >>> i.publicar_post("NOEXISTE", "adventure", "primer post")
        Error: no existeix aquest usuari
        """
        if nick not in self.__usuaris:
            print("Error: no existeix aquest usuari")
            return

        # si el hashtag no existeix el creem
        if id_hashtag not in self.__hashtags:
            self.__hashtags[id_hashtag] = Hashtag(id_hashtag)

        # creem el post
        p = Post(contingut_post)
        p.registra_usuari(nick)
        p.afegeix_hashtag(self.__hashtags[id_hashtag])

        # afegim el post a l'usuari i al contenidor de posts
        self.__usuaris[nick].registra_post(p)
        self.__posts[p.id] = p

    def users(self):
        for u in self.__usuaris.values():
            print(u)
            if not u.get_posts():
                print(" Posts publicados:  no disponibles")

    def posts(self):
        llista = list(self.__posts.values())
        for p in reversed(llista):
            print(p)

    def llistarPostsUser(self, nick):
        """
        >>> i = iTICApp()
        >>> i.afegeix_usuari("AH39", "AH39@gmail.com", "hola")
        >>> i.afegeix_hashtag("zzzzzz")
        >>> i.publicar_post("AH39", "jajajaj", "primer post")
        >>> i.llistarPostsUser("AH39")
        ['primer post']
        """
        resultat = []
        for p in self.__usuaris[nick].get_posts():
            resultat.append(p.contingut)
        return resultat


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    i = iTICApp()
    i.afegeix_usuari("AH39", "AH39@gmail.com", "hola")
    i.afegeix_hashtag("nooooooo")
    i.publicar_post("AH39", "siiiiiiiiiii", "primer post")
    i.afegeix_usuari("AHMED", "AHMED@gmail.com", "adeu")
    i.afegeix_hashtag("hlaaaaa")
    i.publicar_post("AH39", "wwww", "segon post")
    i.publicar_post("AH39", "wwq", "tercer post")
    i.users()
    print("---")
    i.posts()
    print("---")
    print(i.llistarPostsUser("AH39"))
