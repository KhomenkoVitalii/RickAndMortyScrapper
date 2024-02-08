const LOGIN_ACTION = "LOGIN";
const LOGOUT_ACTION = "LOGOUT";

export const LoginAction = (userData) => {
    localStorage.setItem("user", JSON.stringify(userData));

    const payload = {
        is_authorized: true,
        userData: userData,
    }

    return { type: LOGIN_ACTION, ...payload }
}

export const LogoutAction = (defaultData) => {
    localStorage.removeItem("user");

    const payload = {
        is_authorized: false,
        userData: defaultData,
    }

    return { type: LOGOUT_ACTION, ...payload }
}

export const AppActionReducer = (state, action) => {
    switch (action.type) {
        case LOGIN_ACTION: {
            return { ...state, user: action.payload };
        }

        case LOGOUT_ACTION: {
            return { ...state, user: action.payload };
        }

        default: return state;
    }
}