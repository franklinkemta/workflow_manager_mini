import React, { Component } from 'react';
import { Card, CardImg, ButtonGroup, Button } from 'react-bootstrap';

import { connect } from 'react-redux';
import { nextProgression, prevProgression } from '../actions/progressionActions';
import { getWorkflowProgressions } from '../actions/workflowActions';

import PropTypes from 'prop-types';

class Progression extends Component {
  refreshProgressions  = () => {
    this.props.getWorkflowProgressions(this.props.progressionDetails.workflow_id)
  }
  handleNext = () => {
    this.props.nextProgression(this.props.progressionDetails);
    this.refreshProgressions()
  }
  
  handlePrev = () => {
    this.props.prevProgression(this.props.progressionDetails);
    this.refreshProgressions()
  }

  render () {
    
    const { progressionDetails } = this.props;

    return (
      <div>
        <Card>
            <Card.Img variant="top" height="200" src={ progressionDetails.image.url } />
                <Card.Body className="justify-content-center text-center ">
                    <ButtonGroup>
                    
                        <Button size="sm" variant="outline-info"><a href={ "http://127.0.0.1:5000/api/workflow/" + progressionDetails.workflow_id + "/progressions/" + progressionDetails.id }>View</a></Button>
                        <Button onClick={this.handlePrev} size="sm" variant="outline-secondary">Prev</Button>
                        <Button onClick={this.handleNext} size="sm" variant="outline-secondary">Next</Button>
                        
                    </ButtonGroup>
                    <p className=" mt-2 mb-0"> <b>  { progressionDetails.status } </b></p>
                </Card.Body>
                <Card.Footer>
                    <small className="text-muted">{ progressionDetails.timestamp }</small>
                </Card.Footer>
        </Card>

      </div>
    );
  }
}

Progression.protoTypes = {
    getWorkflowProgressions: PropTypes.func.isRequired,
    nextProgression: PropTypes.func.isRequired,
    prevProgression: PropTypes.func.isRequired,
    progression: PropTypes.object.isRequired
  }
  
  const mapStateToProps = (state) =>({
      progression: state.progression
  });
  
  export default connect(mapStateToProps, { getWorkflowProgressions, nextProgression, prevProgression })(Progression);