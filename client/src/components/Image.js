import React, { Component } from 'react';
import { Card, CardImg, ButtonGroup, Button } from 'react-bootstrap';

import { connect } from 'react-redux';
import { deleteImage } from '../actions/imageActions';

import PropTypes from 'prop-types';

class Image extends Component {
  
  handleDelete = () => {
    this.props.deleteImage(this.props.imageDetails.id);
  }

  render () {
    
    const { imageDetails } = this.props;

    return (
      <div>
        <Card>
            <Card.Img variant="top" height="200" src={imageDetails.url} />
                <Card.Body className="justify-content-center text-center ">
                    <ButtonGroup>
                    
                        <Button size="sm" variant="outline-info"><a href={ "http://127.0.0.1:5000/api/image/" + imageDetails.id }>View</a></Button>
                        <Button onClick={this.handleDelete} size="sm" variant="outline-secondary">Delete</Button>
                        
                    </ButtonGroup>
                    <p className=" mt-2 mb-0"> <b>  { imageDetails.status } </b></p>
                </Card.Body>
                <Card.Footer>
                    <small className="text-muted">{ imageDetails.timestamp }</small>
                </Card.Footer>
        </Card>

      </div>
    );
  }
}

Image.protoTypes = {
    deleteImage: PropTypes.func.isRequired,
    image: PropTypes.object.isRequired
  }
  
  const mapStateToProps = (state) =>({
      image: state.image
  });
  
  export default connect(mapStateToProps, { deleteImage })(Image);