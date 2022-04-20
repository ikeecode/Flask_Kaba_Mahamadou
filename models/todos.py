# import sys
#
# sys.path.append('../')
# from index import db
#
# class Todo(db.Model):
#     userId    = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
#     id        = db.Column(db.Integer, primary_key=True, nullable=False)
#     title     = db.Column(db.String(200), nullable=False)
#     completed = db.Column(db.Boolean, nullable=False)
#
#     def __rep__(self):
#         return f"Todod(id:{self.id}, title:{self.title}, completed:{self.completed}, userId:{self.userId})"
