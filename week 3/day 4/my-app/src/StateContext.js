import React, { createContext, useContext, useReducer } from "react";

// Initial state
const initialState = {
  currYear: '',
};

// Action types
export const PICK_YEAR = "Pick the current year";
const DECREMENT = "DECREMENT";

// Reducer function
const reducer = (state, action) => {
  let newState = undefined;
  const oldState = state;
  switch (action.type) {
    case PICK_YEAR:
      newState = { ...state, currYear: action.year };
      break;
    case DECREMENT:
      newState = { ...state, count: state.count - 1 };
      break;
    default:
      return state;
  }
  console.log(`${JSON.stringify(oldState)} -> ${JSON.stringify(newState)}`);
  return newState;
};

// Create context
const StateContext = createContext();

// Provide a custom hook to use the state context
export const useGlobalContext = () => useContext(StateContext);

// Provide a context provider component with useReducer
export const StateProvider = ({ children }) => {
  const [state, dispatch] = useReducer(reducer, initialState);

  return (
    <StateContext.Provider value={{ state, dispatch }}>
      {children}
    </StateContext.Provider>
  );
};
