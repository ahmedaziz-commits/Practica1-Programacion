import time 

class Post:
    contador_id=1
    def __init__(self,contenido):
        self.id = Post.contador_id 
        Post.contador_id += 1
        self.info = contenido 
        self.date = time.ctime()

    def __str__(self):
        return f"Post ID: {self.id} info: {self.info} Date: {self.date}"
    
    def __eq__(self, other):
        if not isinstance(other, Post):
            return False
        return self.id == other.id
class Hashtag:
    
    def __init__(self, Hashtag):
        self.id = Hashtag
    
    def __str__(self):
        return f"Hastag: {self.id}"
    
    def __eq__(self, other):
        if not isinstance(other, Hashtag):
            return False
        return self.id == other.id
if __name__=='__main__':
    post1=Post("Cal realitzar el possible per assolir l’impossible.")
    post2=Post("Tota accio provoca reaccions.")
    print(post1)
    print(post2)
    post3=Post("Cal realitzar el possible per assolir l’impossible.")
    print(post3.info)
    print(post1==post3)
    h1=Hashtag("adventure")
    h2=Hashtag("winter")
    print(h1)
    print(h1==h2)