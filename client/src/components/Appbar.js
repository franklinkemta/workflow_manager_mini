import React, { Component } from 'react';
import { Nav } from 'react-bootstrap';

export default class Appbar extends Component {
  render () {
    return (
      <div>
        <h5 className="justify-content-center text-center mt-4"><a href="/" className="text-decoration-none text-dark" style={{ textDecoration: "none" }}>Mini API Client - Test</a></h5>
        <hr></hr>
        <Nav className="justify-content-center " activeKey="/">
          <Nav.Item>
            <Nav.Link eventKey="link-1" href="/workflows">Workflows</Nav.Link>
          </Nav.Item>
          <Nav.Item>
            <Nav.Link eventKey="link-2" href="/workflows/add">Create workflow</Nav.Link>
          </Nav.Item>
          <Nav.Item>
            <Nav.Link eventKey="link-3" href="/images">Images</Nav.Link>
          </Nav.Item>
          <Nav.Item>
            <Nav.Link eventKey="link-4" href="/images/add">Create Image</Nav.Link>
          </Nav.Item>
        </Nav>
        <hr></hr>
      </div>
    );
  }
}