import axios from 'axios';

import {
    GET_WORKFLOWS,
    GET_WORKFLOW_PROGRESSIONS,
    ADD_WORKFLOW,
    DELETE_WORKFLOW,
    WORKFLOWS_LOADING
} from './types';


export const getWorkflows = () => dispatch => {
    dispatch(setWorkflowLoading()); // set loading to true
    axios.get("/api/workflow", { crossDomain: true})
      .then(res => {
        dispatch({
            type: GET_WORKFLOWS,
            payload: res.data
        });
      })
}

export const getWorkflowProgressions = (id) => dispatch => {
    dispatch(setWorkflowLoading()); // set loading to true
    axios.get("/api/workflow/" + id + "/progressions", { crossDomain: true})
      .then(res => {
        dispatch({
            type: GET_WORKFLOW_PROGRESSIONS,
            payload: res.data
        });
      })
}


export const addWorkflow = (workflow) => dispatch => {
    dispatch({
        type: ADD_WORKFLOW,
        payload: workflow
    });
    console.log('created workflow', workflow);
}

export const deleteWorkflow = (id) => dispatch => {
    dispatch({
        type: DELETE_WORKFLOW,
        payload: id
    });
}



export const setWorkflowLoading = () => {
    return {
        type: WORKFLOWS_LOADING
    }
}