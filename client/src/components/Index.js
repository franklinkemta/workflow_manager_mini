import React, { Component } from 'react';
import { Container } from 'react-bootstrap';

export default class Index extends Component {
  render () {
    return (
      <div>
        <h6 className="justify-content-center text-center mt-4">Welcome, Select to display</h6>
        <p className="justify-content-center text-center mt-4">The flask api must be running at </p>
      </div>
    );
  }
}