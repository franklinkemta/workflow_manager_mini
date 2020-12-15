"""
This file serve for database initialization
"""

import os
from shared.config import db
# from app import db # this db object fits more the runtime state better than the previous one

# Import models for initialization

from models import Workflow, Image, Progression

# Delete database file if it exists currently
if os.path.exists("shared/db.sqlite"):
    os.remove("shared/db.sqlite")

# Create the database
db.create_all()


#--------------- // Mes Customs Test Values // ------------- #

WORKFLOW = [
    { "name": "Workflow 1" },
    { "name": "Workflow 2" },
    { "name": "Workflow 3" }
]

IMAGE = [
    { "url": "https://image.freepik.com/free-psd/white-car-isolated_176382-1481.jpg" },
    { "url": "https://image.freepik.com/free-psd/retro-coupe-car-mockup_338035-11773.jpg" },
    { "url": "https://image.freepik.com/free-psd/white-car-isolated_176382-1482.jpg" },
    { "url": "https://image.freepik.com/free-psd/antique-car-1950-mockup_338035-12919.jpg" },
    { "url": "https://image.freepik.com/free-psd/suv-4x4-car-mockup_338035-7780.jpg" },
    { "url": "https://image.freepik.com/free-psd/suv-4x4-car-2008-mockup_338035-4123.jpg" },
    { "url": "https://image.freepik.com/free-psd/white-sport-car_176382-1598.jpg" },
    { "url": "https://image.freepik.com/free-psd/hatchback-car-2011-mockup_338035-2381.jpg" },
    { "url": "https://image.freepik.com/free-psd/white-off-road-car_176382-1593.jpg" },
    { "url": "https://image.freepik.com/free-psd/hatchback-car-2009-mockup_338035-2279.jpg" },
]

# Add some images to workflows
PROGRESSION = [
    { "workflow_id": 1, "image_id": 1 },
    { "workflow_id": 1, "image_id": 2 },
    { "workflow_id": 1, "image_id": 3 },
    { "workflow_id": 2, "image_id": 4 },
    { "workflow_id": 2, "image_id": 3 },
    { "workflow_id": 2, "image_id": 5 },
    { "workflow_id": 2, "image_id": 6 },
    { "workflow_id": 2, "image_id": 7 },
]

# Insert the test data in the database
for workflow in WORKFLOW:
    wf = Workflow(name=workflow.get("name"))
    db.session.add(wf)

for image in IMAGE:
    img = Image(url=image.get("url"))
    db.session.add(img)

for progression in PROGRESSION:
    pg = Progression(image_id=progression.get("image_id"), workflow_id=progression.get("workflow_id"), )
    db.session.add(pg)


db.session.commit() # commit the changes to the db