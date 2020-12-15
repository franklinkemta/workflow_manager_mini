import {
    NEXT_PROGRESSION,
    PREV_PROGRESSION,
    UPDATE_PROGRESSION_STATUS,
    GET_PROGRESSION,
    ADD_PROGRESSION,
    DELETE_PROGRESSION,
    PROGRESSIONS_LOADING
} from '../actions/types';

const initialState = {
    progression: null,
    loading: false
}

const ProgressionReducer = function(state = initialState, action) {
    switch (action.type) {
        case NEXT_PROGRESSION:
            return {
                ...state,
                progression: action.payload,
                loading: false
            };
        case PREV_PROGRESSION:
            return {
                ...state,
                progression: action.payload,
                loading: false
            };
        case GET_PROGRESSION:
            return {
                ...state,
                progression: action.payload,
                loading: false
            };
        case DELETE_PROGRESSION:
            return {
                ...state,
                progression: null
            };
        case ADD_PROGRESSION:
            return {
                ...state,
                progression: action.payload
            }
        case PROGRESSIONS_LOADING:
            return {
                ...state,
                loading: true
            }

        default:
            return state;
    }
}

export default ProgressionReducer