from datetime import datetime
from enum import unique
from shared.config import db, ma # Import SQLAlchemy and Marshmallow Wrapper

# Workflow Model
class Workflow(db.Model):
    uid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    timestamp = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )

    # One to many relationship
    steps = db.relationship('Step', backref='workflow', lazy=True)
    #__init__ method is implicit with SQLAlchemy

# Workflow Schema
class WorkflowSchema(ma.Schema):
    class Meta:
        model = Workflow
        fields = ('uid', 'name', 'timestamp', 'steps')
        sqla_session = db.session
