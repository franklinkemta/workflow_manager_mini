from datetime import datetime
from enum import unique
from shared.config import db, ma # Import SQLAlchemy and Marshmallow Wrapper

# Step Model
class Step(db.Model):
    uid = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer, nullable=False, unique=True)
    timestamp = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )
    # Many to one relationship
    workflow_id = db.Column(db.Integer, db.ForeignKey('workflow.uid'), nullable=False)
    #__init__ method is implicit with SQLAlchemy

# Step Schema
class StepSchema(ma.Schema):
    class Meta:
        model = Step
        fields = ('uid', 'number', 'timestamp', 'workflow_id')
        sqla_session = db.session
