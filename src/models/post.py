import uuid
import datetime
from src.common.database import Database

__author__ = 'alee'

class Post(object):

    def __init__(self, blog_id: object, title: object, content: object, author: object,
                 created_date: object = datetime.datetime.utcnow(),
                 _id: object = None) -> object:
        self.created_date=created_date
        self._id=uuid.uuid4().hex if _id is None else _id
        self.blog_id=blog_id
        self.title=title
        self.content=content
        self.author=author

    def save_to_mongo(self):
        Database.insert(collection='posts',
                        data=self.json())

    def json(self):
        return {
            '_id':self._id,
            'blog_id':self.blog_id,
            'title':self.title,
            'content':self.content,
            'author':self.author,
            'created_date':self.created_date
        }
    @classmethod
    def from_mongo(cls,id):
        #Post.from_mongo(123)
        post_data = Database.find_one(collection='posts',query={'_id':id})
        return cls(**post_data)

    @staticmethod
    def from_blog_id(id):
        return [post for post in Database.find(collection='posts',query={'blog_id':id})]