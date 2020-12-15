import axios from 'axios';

import {
    GET_PROGRESSION,
    ADD_PROGRESSION,
    DELETE_PROGRESSION,
    NEXT_PROGRESSION,
    PREV_PROGRESSION,
    UPDATE_PROGRESSION_STATUS,
    PROGRESSIONS_LOADING
} from './types';


export const getProgression = () => dispatch => {
    dispatch(setProgressionsLoading()); // set loading to true
    // rember proxy on the package.json
    dispatch({
        type: GET_PROGRESSION
    });
}

export const nextProgression = (progression) => dispatch => {
    dispatch(setProgressionsLoading()); // set loading to true
    axios.put("/api/workflow/" + progression.workflow_id + "/progressions/" + progression.id + "/next", { crossDomain: true})
      .then(res => {
        dispatch({
            type: NEXT_PROGRESSION,
            payload: res.data
        });
      })
}

export const prevProgression = (progression) => dispatch => {
    dispatch(setProgressionsLoading()); // set loading to true
    axios.put("/api/workflow/" + progression.workflow_id + "/progressions/" + progression.id + "/prev", { crossDomain: true})
      .then(res => {
        dispatch({
            type: PREV_PROGRESSION,
            payload: res.data
        });
      })
}


export const addProgression = (progression) => dispatch => {
    dispatch({
        type: ADD_PROGRESSION,
        payload: progression
    });
    console.log('created progression', progression);
}

export const deleteProgression = (id) => dispatch => {
    dispatch({
        type: DELETE_PROGRESSION,
        payload: id
    });
}

export const setProgressionsLoading = () => {
    return {
        type: PROGRESSIONS_LOADING
    }
}