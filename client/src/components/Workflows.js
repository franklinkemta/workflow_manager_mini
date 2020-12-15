import React, { Component } from 'react';
import { Container, ButtonGroup, Button, Form, Row, Col } from 'react-bootstrap';

import { connect } from 'react-redux';
import { getWorkflows, getWorkflowProgressions, deleteWorkflow } from '../actions/workflowActions';

// Components
import Progression from "./Progression";

import PropTypes from 'prop-types';

class Workflows extends Component {
  
  state = {
    workflowSelect: null,
  };

  componentDidMount() {
    this.props.getWorkflows();
  }

  onDeleteClick = (id) => {
		this.props.deleteWorkflow(id);
  }
  
  handleWorkflowSelect = (e) => {
    
    if (e.target.value) {
      this.setState({ workflowSelect: e.target.value });
      // this.setState({ progressions: e.target.value.progressions });
      this.props.getWorkflowProgressions(e.target.value);
    }
    
  };

  render () {
    const { workflows, workflowProgressions } = this.props.workflow;
    return (
      <div>
        <Form.Group controlId="exampleForm.ControlSelect1">
          <Form.Row>
            <Form.Label column="sm">
              <b className=" text-center mt-4">Workflows Images Progression</b>
            </Form.Label>
            <Col lg="2">
              <Form.Control size="sm" 
                as="select" placeholder="Workflow"
                onChange={this.handleWorkflowSelect}
              >
                <option value={null} defaultValue>Select workflow</option>
                {workflows.map(({ id, name }) => (
                  <option key={id} value={id}>{name}</option>
                ))}
              </Form.Control>
            </Col>
            
            <Col lg="3">
              <ButtonGroup>
                <Button
                        variant="outline-primary"
                        size="sm"
                      >[+] Insert image</Button>
                <Button
                        variant="outline-secondary"
                        size="sm"
                      >- Delete workflow</Button>
              </ButtonGroup>
            </Col>
          </Form.Row>
        </Form.Group>
        <Container>
					<Row>
              {workflowProgressions.map((progression) => (
                  <Col className="mb-2" key={progression.id} lg="3">
                    <Progression progressionDetails={progression}/>
                  </Col>
							))}
					</Row>

				</Container>
      </div>
    );
  }
}

Workflows.protoTypes = {
  getWorkflows: PropTypes.func.isRequired,
  getWorkflowProgressions: PropTypes.func.isRequired,
	workflow: PropTypes.object.isRequired
}

const mapStateToProps = (state) =>({
	workflow: state.workflow
});

export default connect(mapStateToProps, { getWorkflows, getWorkflowProgressions, deleteWorkflow })(Workflows);