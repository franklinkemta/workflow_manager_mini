import React, { Component } from 'react';
import { Container } from 'react-bootstrap';

import axios from 'axios';

export default class AddWorkflow extends Component {
  state = {
    workflows: []
  }

  render () {
    return (
      <div>
        <b className="justify-content-center text-center mt-4">Add Workflow</b>
      </div>
    );
  }
}