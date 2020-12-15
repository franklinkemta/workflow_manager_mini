import React, { Component, Suspense, lazy } from "react";
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';

// Components
import Appbar from "./components/Appbar";

import { Container } from 'react-bootstrap';


// Add Redux Store
import { Provider } from "react-redux";
import store from "./store";

// Css
import "bootstrap/dist/css/bootstrap.css";
import './App.css';

// Routes components imports
const Index = lazy(() => import('./components/Index'));
const Workflows = lazy(() => import('./components/Workflows'));
const AddWorkflow = lazy(() => import('./components/AddWorkflow'));
const Images = lazy(() => import('./components/Images'));
const AddImage = lazy(() => import('./components/AddImage'));

class App extends Component {
  render() {
    return (
      <Provider store={store}>
        <div className="App">
          <Appbar />
          <Container>
          <Router>
            <Suspense fallback={<div>Loading...</div>}>
              <Switch>
                <Route exact path="/" component={Index}/>
                <Route exact path="/workflows" component={Workflows}/>
                <Route path="/workflows/add" component={AddWorkflow}/>
                <Route exact path="/images" component={Images}/>
                <Route path="/images/add" component={AddImage}/>
              </Switch>
            </Suspense>
          </Router>
          </Container>
        </div>
      </Provider>
    );
  }
}


export default App;