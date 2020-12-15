"""
This is the image module and supports all the REST actions for the
image data
"""

# Load modules
from flask import request, jsonify, abort
from shared.config import app, db
from models import Image, ImageSchema

# Get all images
@app.route('/api/image', methods=['GET'])
def get_all_images():
    # Create the list of images from our data
    images = Image.query.order_by(Image.id).all()
    # Serialize the data for the response
    images_schema = ImageSchema(many=True) # strict=true
    data = images_schema.dump(images)
    return jsonify(data)


# Get one image
@app.route('/api/image/<image_id>', methods=['GET'])
def get_image(image_id):
    # Get the requested image
    image = Image.query.filter(Image.id == image_id).one_or_none()

    # Check if we got an image
    if image is not None:
    
        # Serialize the data for the response
        image_schema = ImageSchema()
        data = image_schema.dump(image)
        return jsonify(data)

    # Otherwise, nope, didn't find that image
    else:
        abort(404, "Image not found for Id: {id} ".format(id=image_id))


# Create a new image for manipulation
@app.route('/api/image', methods=['POST'])
def create_image():
    
    # create image from url
    url = request.json['url']

    # Check if the image url exist
    existing_image = (
        Image.query.filter(Image.url == url).one_or_none()
    )

    if existing_image is None:
        # Insert image to the first step of the image
        schema = ImageSchema()
        new_image = Image(
            url = url
        )

        # Save to the database
        db.session.add(new_image)
        db.session.commit()

        # Serialize and return the newly created data in the response
        data = schema.dump(new_image)

        return jsonify(data), 201

    # Otherwise, nope, data exists already
    else:
        abort(400, "Image url already exists: {url} ".format(url=url))


# Update an image
@app.route('/api/image/<image_id>', methods=['PUT'])
def update_image(image_id):

    url = request.json["url"]

    # Get the image to update
    image = Image.query.filter(Image.id == image_id).one_or_none()

    # Check if we got a image
    if image is not None:

        image.url = url

        # Update the image
        db.session.merge(image)
        db.session.commit()

        # Serialize the data for the response
        image_schema = ImageSchema()
        data = image_schema.dump(image)
        return jsonify(data)

    # Otherwise, nope, didn't find that image
    else:
        abort(404, "Image not found for Id: {id} ".format(id=image_id))


# Delete an image
@app.route('/api/image/<image_id>', methods=['DELETE'])
def delete_image(image_id):

    # Get the image to update
    image = Image.query.filter(Image.id == image_id).one_or_none()

    # Check if we got a image
    if image is not None:

        # Delete the image
        db.session.delete(image)
        db.session.commit()

        # Return delete confirmation message
        return jsonify({ "msg" : " Successfuly deleted Image : {id} ".format(id=image_id) })

    # Otherwise, nope, didn't find that image
    else:
        abort(404, "Image not found for Id: {id} ".format(id=image_id))