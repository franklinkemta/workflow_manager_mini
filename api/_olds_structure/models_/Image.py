from datetime import datetime
from shared.config import db, ma # Import SQLAlchemy and Marshmallow Wrapper

# Image Model
class Image(db.Model):
    uid = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(200), nullable=False, unique=True)
    name = db.Column(db.String(100), nullable=True)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    timestamp = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )
    #__init__ method is implicit with SQLAlchemy

# Image Schema
class ImageSchema(ma.Schema):
    class Meta:
        model = Image
        # fields = ('uid', 'url', 'name', 'created_at', 'updated_at', 'timestamp')
        # sqla_session = db.session

# Init Schema
#image_schema = ImageSchema(strict=True) # Disable warnings in the console
#images_schema = ImageSchema(many=True, strict=True) # Because we will fetch more than one item