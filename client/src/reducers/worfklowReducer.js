import {
    GET_WORKFLOWS,
    GET_WORKFLOW_PROGRESSIONS,
    DELETE_WORKFLOW,
    WORKFLOWS_LOADING,
    ADD_WORKFLOW
} from '../actions/types';

const initialState = {
    workflows: [],
    workflowProgressions: [],
    loading: false
}

const WorkflowReducer = function(state = initialState, action) {
    switch (action.type) {
        case GET_WORKFLOWS:
            return {
                ...state,
                workflows: action.payload,
                loading: false
            };
        case GET_WORKFLOW_PROGRESSIONS:
            return {
                ...state,
                workflowProgressions: action.payload,
                loading: false
            };
        case DELETE_WORKFLOW:
            return {
                ...state,
                workflows: state.workflows.filter(instance => instance.id !== action.payload)
            };
        case ADD_WORKFLOW:
            const workflows = state.workflows.filter(instance => instance.id !== action.payload.id)
            return {
                ...state,
                workflows: [...workflows, action.payload]
            }
        
        case WORKFLOWS_LOADING:
            return {
                ...state,
                loading: true
            }

        default:
            return state;
    }
}

export default WorkflowReducer