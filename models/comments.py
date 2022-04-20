# import sys
# sys.path.append('../')
# from index import db
#
# class Comment(db.Model):
#     postId = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)
#     id     = db.Column(db.Integer, primary_key=True, nullable=False)
#     name   = db.Column(db.String(200), nullable=False)
#     email  = db.Column(db.String(200), nullable=False)
#     body   = db.Column(db.Text, nullable=False)
#
#     def __rep__(self):
#         return f"postId:{self.postId}, id:{self.id}, name:{self.name}, email:{self.email}"
