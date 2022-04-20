# import sys
#
# sys.path.append('../')
# from index import db
#
# class Album(db.Model):
#     userId    = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
#     id        = db.Column(db.Integer, primary_key=True, nullable=False)
#     title     = db.Column(db.String(200), nullable=False)
#     photos    = db.relationship('Photo', backref='album')
#
#     def __rep__(self):
#         return f"userId:{self.userId}, id:{self.id}, title:{self.title}"
#
#
#
# # class Photo(db.Model):
# #     albumId      = db.Column(db.Integer, db.ForeignKey('album.id'), nullable=False)
# #     id           = db.Column(db.Integer, primary_key=True, nullable=False)
# #     title        = db.Column(db.String(200), nullable=False)
# #     url          = db.Column(db.String(200), nullable=False)
# #     thumbnailUrl = db.Column(db.LargeBinary, nullable=False)
# #
# #     def __rep__(self):
# #         return f"Photo(albumId:{self.albumId}, id:{self.id}, title:{self.title}, url:{self.url})"
