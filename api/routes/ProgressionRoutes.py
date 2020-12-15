"""
This is the step module and supports all the REST actions for the
step data
"""

# Load modules
from flask import request, jsonify, abort
from shared.config import app, db
from models import Progression, ProgressionSchema, Workflow, Image

# Implicit indicate to set the header to allow cross origin requests
from flask_cors import cross_origin

# Get an image progression
@app.route('/api/workflow/<workflow_id>/progressions/<progression_id>', methods=['GET'])
@cross_origin()
def get_progression(workflow_id, progression_id):

    # Get the progression requested
    progression = Progression.query.filter(Progression.id == progression_id).one_or_none()

    # Check if we got a progression
    if progression is not None:
    
        # Serialize the data for the response
        progression_schema = ProgressionSchema()
        data = progression_schema.dump(progression)
        return jsonify(data)

    # Otherwise, nope, didn't find that progression
    else:
        abort(404, "Progression not found for Id: {id} ".format(id=progression_id))

# Create an image progression and associate to the given workflow
@app.route('/api/workflow/<workflow_id>/progressions', methods=['POST'])
def add_image_progression(workflow_id):
    image_id = request.json['image_id']

    # Check if the workflow exist
    existing_workflow = (
        Workflow.query.filter(Workflow.id == workflow_id).one_or_none()
    )

    # Check if the image exist
    existing_image = (
        Image.query.filter(Image.id == image_id).one_or_none()
    )

    if (existing_workflow is not None) and (existing_image is not None):
        # Insert image to the first step of the workflow
        schema = ProgressionSchema()
        new_progression = Progression(
            workflow_id = workflow_id,
            image_id = image_id
        )
        # no need to specify status and position in the workflow : model default values

        # Save to the database
        db.session.add(new_progression)
        db.session.commit()

        # Serialize and return the newly created data in the response
        data = schema.dump(new_progression)

        return jsonify(data), 201

    # Otherwise, nope, data exists already
    else:
        abort(400, "Workflow or images does not exists ")


# Update image progression to next step in the workflow
@app.route('/api/workflow/<workflow_id>/progressions/<progression_id>/next', methods=['PUT'])
@cross_origin()
def move_image_progression_next(workflow_id, progression_id):

    # Check if the image progression object exist
    existing_progression = (
        Progression.query.filter(Progression.id == progression_id).one_or_none()
    )

    if (existing_progression is not None) and (existing_progression.status != "Validated"):
        # Move to next step
        """
            Check if we reached the last step, set status to validated, else update status
        """
        next_step = existing_progression.position + 1
        if (next_step >= 3):
            existing_progression.status = "Validated"
        else:
            existing_progression.status = "Status {position}".format(position=next_step)

        existing_progression.position = next_step


        # Update the progression to the database
        db.session.merge(existing_progression)
        db.session.commit()

        # Serialize and return the updated data in the response
        schema = ProgressionSchema()
        data = schema.dump(existing_progression)

        return jsonify(data), 201

    # Otherwise, nope, data exists already
    else:
        abort(400, "The image progression {id} does not exists  in the workflow".format(id=progression_id))


# Update image progression to prev step in the workflow
@app.route('/api/workflow/<workflow_id>/progressions/<progression_id>/prev', methods=['PUT'])
@cross_origin()
def move_image_progression_prev(workflow_id, progression_id):

    # Check if the image progression object exist
    existing_progression = (
        Progression.query.filter(Progression.id == progression_id).one_or_none()
    )

    if (existing_progression is not None) and (existing_progression.status != "Validated"):
        # Move to prev step and Check if we reached the first step

        prev_step = existing_progression.position - 1
        if (prev_step >= 1):
            existing_progression.position = prev_step
            existing_progression.status = "Status {position}".format(position=prev_step)

        # Update the progression to the database
        db.session.merge(existing_progression)
        db.session.commit()

        # Serialize and return the updated data in the response
        schema = ProgressionSchema()
        data = schema.dump(existing_progression)

        return jsonify(data), 201

    # Otherwise, nope, data exists already
    else:
        abort(400, "The image progression {id} does not exists in the workflow ".format(id=progression_id))


# Update image progression status in the workflow
@app.route('/api/workflow/<workflow_id>/progressions/<progression_id>/update_status', methods=['PUT'])
def update_image_progression_status(workflow_id, progression_id):

    update_status = request.json['status'] # if we want to rename the status on change

    # Check if the image progression object exist
    existing_progression = (
        Progression.query.filter(Progression.id == progression_id).one_or_none()
    )

    if (existing_progression is not None) and (update_status is not None):
        # Update only the image those are still in the workflow status != Validated
        if (existing_progression.position < 3):
            existing_progression.status = update_status
            # Update the progression to the database
            db.session.merge(existing_progression)
            db.session.commit()

            # Serialize and return the updated data in the response
            schema = ProgressionSchema()
            data = schema.dump(existing_progression)
            return jsonify(data), 201

        else:
            abort(400, "Error: The image progression status is Validated")

    # Otherwise, the data doesnt exist 
    else:
        abort(400, "The image progression {id} does not exists in the workflow ".format(id=progression_id))


# Delete image progression status in the workflow
@app.route('/api/workflow/<workflow_id>/progressions/<progression_id>', methods=['DELETE'])
def delete_image_progression(workflow_id, progression_id):

    # Check if the image progression object exist
    existing_progression = (
        Progression.query.filter(Progression.id == progression_id).one_or_none()
    )

    if existing_progression is not None:
        # Delete image progression from the workflow

        db.session.delete(existing_progression)
        db.session.commit()

        # Return delete confirmation message
        return jsonify({ "msg" : " Successfuly deleted progression {progression_id} from the workflow {workflow_id}".format(progression_id=progression_id, workflow_id = workflow_id) })


    # Otherwise, the data doesnt exist 
    else:
        abort(400, "The image progression {id} does not exists in the workflow ".format(id=progression_id))
