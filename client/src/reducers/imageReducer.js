import {
    GET_IMAGES,
    ADD_IMAGE,
    DELETE_IMAGE,
    IMAGES_LOADING
} from '../actions/types';

const initialState = {
    images: [],
    loading: false
}

const ImageReducer = function(state = initialState, action) {
    switch (action.type) {
        case GET_IMAGES:
            return {
                ...state,
                images: action.payload,
                loading: false
            };
        case DELETE_IMAGE:
            return {
                ...state,
                images: state.images.filter(image => image.title !== action.payload)
            };
        case ADD_IMAGE:
            const images = state.images.filter(image => image.title !== action.payload.title)
            return {
                ...state,
                images: [...images, action.payload]
            }
        case IMAGES_LOADING:
            return {
                ...state,
                loading: true
            }

        default:
            return state;
    }
}

export default ImageReducer