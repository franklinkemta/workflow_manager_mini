from datetime import datetime
from enum import unique
from shared.config import db, ma # Import SQLAlchemy and Marshmallow Wrapper

# Workflow Model
class Workflow(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    create_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    timestamp = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )

    # One to many relationship
    progressions = db.relationship('Progression', backref='workflow', lazy=True)
    #__init__ method is implicit with SQLAlchemy


# Progression Model
class Progression(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    position = db.Column(db.Integer, nullable=False, default=1)
    status = db.Column(db.String(100), nullable=False, default="Status 1")
    create_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    timestamp = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )
    
    # Many to one relationship
    workflow_id = db.Column(db.Integer, db.ForeignKey('workflow.id'), nullable=False)
    # One to one relationship
    image_id = db.Column(db.Integer, db.ForeignKey('image.id'), nullable=False)
    image = db.relationship("Image", backref="progression")



# Image Model
class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(200), nullable=False, unique=True)
    create_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    timestamp = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )


# Image Schema
class ImageSchema(ma.Schema):
    class Meta:
        model = Image
        fields = ('id', 'url', 'create_date', 'timestamp')
        # sqla_session = db.session

# Progression Schema
class ProgressionSchema(ma.Schema):
    image = ma.Nested(ImageSchema)
    class Meta:
        model = Progression
        fields = ('id', 'position', 'status', 'create_date', 'timestamp', 'image', 'workflow_id')
        # sqla_session = db.session

# Workflow Schema
class WorkflowSchema(ma.Schema):
    # Serialize the relationship to avoid jsonify errors
    progressions = ma.Nested(ProgressionSchema, many=True)
    class Meta:
        model = Workflow
        fields = ('id', 'name', 'create_date', 'timestamp', 'progressions')
        # sqla_session = db.session