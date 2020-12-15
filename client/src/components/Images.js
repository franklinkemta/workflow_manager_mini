import React, { Component } from 'react';
import { Container, ButtonGroup, Button, Form, Row, Col } from 'react-bootstrap';

import { connect } from 'react-redux';
import { getImages, addImage } from '../actions/imageActions';

// Components
import Image from "./Image";

import PropTypes from 'prop-types';

class Images extends Component {
  
  state = {
    imageSelect: null,
  };

  componentDidMount() {
    this.props.getImages();
  }

  onDeleteClick = (id) => {
		this.props.deleteImage(id);
  }
  
  handleImageSelect = (e) => {
    
    if (e.target.value) {
      this.setState({ imageSelect: e.target.value });
    }
    
  };

  render () {
    const { images } = this.props.image;
    return (
      <div>
        <Form.Group controlId="exampleForm.ControlSelect1">
          <Form.Row>
            <Form.Label column="sm">
              <b className=" text-center mt-4">Raw Images</b>
            </Form.Label>
          </Form.Row>
        </Form.Group>
        <Container>
					<Row>
              {images.map((image) => (
                  <Col className="mb-2"  key={image.id} lg="3">
                    <Image imageDetails={image}/>
                  </Col>
							))}
					</Row>

				</Container>
      </div>
    );
  }
}

Images.protoTypes = {
  getImages: PropTypes.func.isRequired,
  addImage: PropTypes.func.isRequired,
	image: PropTypes.object.isRequired
}

const mapStateToProps = (state) =>({
	image: state.image
});

export default connect(mapStateToProps, { getImages, addImage })(Images);