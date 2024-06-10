class Article:
    all= []
    
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self._title = str(title)
        Article.all.append(self)
 
    @property
    def title(self):
        return self._title
 
    @title.setter
    def title(self, title):
       if hasattr(self,"title"):AttributeError("Title cannot be changed")
       else:
            if isinstance(title,str):
                if 5<=len(title)<=50:
                    self._title=title
                else:ValueError("Title must be between 5 and 50 characheters")
            else:TypeError("Title must be a string")
  
    @property
    def author(self):
        return self._author

    @property
    def magazine(self):
        return self._magazine

    @author.setter
    def author(self, author):
        if isinstance(author, Author):
            self._author = author
        else:
            raise TypeError("Author must be of type Author")
    
    @magazine.setter
    def magazine(self, magazine):
        if isinstance(magazine, Magazine):
            self._magazine = magazine
        else:
            raise TypeError("Magazine must be of type Magazine")
     

class Author:

    all = []
    def __init__(self, name):
        self._name = name
        Author.all.append(self)
    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_names):
        self.new_names = new_names
        return self._name
    
    def articles(self):
        return [articles for articles in Article.all if articles.author == self]

    def magazines(self):
        return list(set([article.magazine for article in self.articles()]))
    
   
    def add_article(self, magazine, title):
        articles = Article(self, magazine, title)
        return articles
   
    
    def topic_areas(self):
        return list(set([article.magazine.category for article in self.articles()])) if self.articles() else None


    @staticmethod
    def list_authors():
        return [author.name for author in Author.all]

   

class Magazine:
    def __init__(self, name, category):
        self._name = name
        self._category = category
    
    @property
    def name(self):
        return self._name
    
    @property
    def category(self):
        return self._category
    
   
    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str):
            if 2 <= len(new_name) <= 16:
                self._name = new_name
            else: 
                ValueError("Name must be between 2 and 16 characters")
        else:
            TypeError("Name must be a string")   
   
    @category.setter
    def category(self, new_category):
        if isinstance(new_category, str):
            if len(new_category):
                self._category = new_category
            else:
                ValueError("Category must be longer than 0 characters")
        else:
            TypeError("Category must be a string")
    
    def articles(self):
        return [articles for articles in Article.all if articles.magazine == self]

    def contributors(self):
        return list(set([articles.author for articles in self.articles()]))

    def article_titles(self):
        titles = [articles.title for articles in self.articles()]
        return titles if titles else None
   
    def contributing_authors(self):
     
      authors = {}
      
      for article in self.articles():
         
          if article.author in authors:
             
              authors[article.author] += 1
          else:
              authors[article.author] = 1
      
      contributing_authors = [author for author, count in authors.items() if count >= 2]
      return contributing_authors if contributing_authors else None