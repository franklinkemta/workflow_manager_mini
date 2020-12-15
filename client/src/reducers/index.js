// Root Reducer
import { combineReducers } from 'redux';
import worfklowReducer from './worfklowReducer';
import progressionReducer from './progressionReducer';
import imageReducer from './imageReducer';

export default combineReducers({
    workflow: worfklowReducer,
    progression: progressionReducer,
    image: imageReducer,
}); // With all the reducers combined