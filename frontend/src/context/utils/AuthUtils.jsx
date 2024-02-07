import { useEffect } from 'react';
import { LoginAction } from '../AppActionReducer'

export const useAuthEffect = (dispatch) => {
    useEffect(() => {
        const userData = localStorage.getItem('user');

        if (userData) {
            const parsedUserData = JSON.parse(userData);

            dispatch(loginAction(parsedUserData));
        }
    }, [dispatch]);
};