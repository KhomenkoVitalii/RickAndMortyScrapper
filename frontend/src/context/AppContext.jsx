import React, { createContext, useContext, useReducer } from "react";
import { AppActionReducer } from './AppActionReducer'
import { useAuthEffect } from "./utils/AuthUtils";

const default_data = {
    is_authorized: false,
    userData: {
        username: null,
    },
};

export const AppContext = createContext({
    default_data
});

export const AppContextProvider = ({ children }) => {
    const [state, dispatch] = useReducer(AppActionReducer, default_data);

    useAuthEffect(dispatch);

    return <AppContext.Provider value={{ state, dispatch }}>
        {children}
    </AppContext.Provider>
}