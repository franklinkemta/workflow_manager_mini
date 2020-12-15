import axios from 'axios';

import {
    GET_IMAGES,
    ADD_IMAGE,
    DELETE_IMAGE,
    IMAGES_LOADING
} from './types';


export const getImages = () => dispatch => {
    dispatch(setImageLoading()); // set loading to true
    axios.get("/api/image", { crossDomain: true})
      .then(res => {
        dispatch({
            type: GET_IMAGES,
            payload: res.data
        });
      })
}


export const addImage = (image) => dispatch => {
    dispatch({
        type: ADD_IMAGE,
        payload: image
    });
    console.log('created image', image);
}

export const deleteImage = (id) => dispatch => {
    dispatch({
        type: DELETE_IMAGE,
        payload: id
    });
}

export const setImageLoading = () => {
    return {
        type: IMAGES_LOADING
    }
}