"""
This is the workflow module and supports all the REST actions for the
workflow data
"""

# Load modules
from os import name
from flask import request, jsonify, abort
from shared.config import app, db
from models import Workflow, WorkflowSchema, Progression, ProgressionSchema

# Implicit indicate to set the header to allow cross origin requests
from flask_cors import cross_origin

# Get all workflows
@app.route('/api/workflow', methods=['GET'])
@cross_origin()
def get_all_workflows():
    # Create the list of workflows from our database
    workflows = Workflow.query.order_by(Workflow.id).all()
    # Serialize the data for the response
    workflows_schema = WorkflowSchema(many=True) # strict=true
    data = workflows_schema.dump(workflows)

    return jsonify(data)


# Get one workflow
@app.route('/api/workflow/<workflow_id>', methods=['GET'])
def get_workflow(workflow_id):
    # Get the requested workflow
    workflow = Workflow.query.filter(Workflow.id == workflow_id).one_or_none()

    # Check if we got a workflow
    if workflow is not None:
    
        # Serialize the data for the response
        workflow_schema = WorkflowSchema()
        data = workflow_schema.dump(workflow)
        return jsonify(data)

    # Otherwise, nope, didn't find that workflow
    else:
        abort(404, "Workflow not found for Id: {id} ".format(id=workflow_id))


# Create a workflow
@app.route('/api/workflow', methods=['POST'])
def add_workflow():
    name = request.json['name']

    # Check if the name already exist
    existing_workflow = (
        Workflow.query.filter(Workflow.name == name).one_or_none()
    )

    if existing_workflow is None:
        # Create a new workflow
        schema = WorkflowSchema()
        new_workflow = Workflow(name = name)

        # Add the workflow to the database
        db.session.add(new_workflow)
        db.session.commit()

        # Serialize and return the newly created data in the response
        data = schema.dump(new_workflow)

        return jsonify(data), 201

    # Otherwise, nope, data exists already
    else:
        abort(400, "Workflow {name} already exists ".format(name=name))


# Update a workflow
@app.route('/api/workflow/<workflow_id>', methods=['PUT'])
def update_workflow(workflow_id):

    name = request.json['name']

    # Get the workflow to update
    workflow = Workflow.query.filter(Workflow.id == workflow_id).one_or_none()

    # Check if we got a workflow
    if workflow is not None:

        workflow.name = name

        # Update the workflow
        db.session.merge(workflow)
        db.session.commit()

        # Serialize the data for the response
        workflow_schema = WorkflowSchema()
        data = workflow_schema.dump(workflow)
        return jsonify(data)

    # Otherwise, nope, didn't find that workflow
    else:
        abort(404, "Workflow not found for Id: {id} ".format(id=workflow_id))


# Delete a workflow
@app.route('/api/workflow/<workflow_id>', methods=['DELETE'])
def delete_workflow(workflow_id):

    # Get the workflow to update
    workflow = Workflow.query.filter(Workflow.id == workflow_id).one_or_none()

    # Check if we got a workflow
    if workflow is not None:

        # Delete the workflow
        db.session.delete(workflow)
        db.session.commit()

        # Return delete confirmation message
        return jsonify({ "msg" : " Successfuly deleted Workflow : {id} ".format(id=workflow_id) })

    # Otherwise, nope, didn't find that workflow
    else:
        abort(404, "Workflow not found for Id: {id} ".format(id=workflow_id))


# Get workflows images progressions
@app.route('/api/workflow/<workflow_id>/progressions', methods=['GET'])
@cross_origin()
def get_workflow_progression(workflow_id):
    # Get the workflow requested
    workflow = Workflow.query.filter(Workflow.id == workflow_id).one_or_none()

    # Check if we found the workflow
    if workflow is not None:
        # Query images progressions ordered by their position asc
        progressions = Progression.query.filter(Progression.workflow_id == workflow.id).order_by(Progression.position).all()
        # Serialize the data for the response
        progressions_schema = ProgressionSchema(many=True) # strict=true
        data = progressions_schema.dump(progressions)
        return jsonify(data)

    # Otherwise, nope, didn't find that workflow
    else:
        abort(404, "Workflow not found for Id: {id} ".format(id=workflow_id))