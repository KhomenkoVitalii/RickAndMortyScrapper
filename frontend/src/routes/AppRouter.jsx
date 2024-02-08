import React, { useEffect } from 'react';
import { createBrowserRouter, useNavigate } from 'react-router-dom'
import App from '../pages/App'
import Home from '../pages/home/Home'
import ErrorComponent from '../components/error/ErrorComponent';
import Seasons from '../pages/seasons/Seasons';
import Characters from '../pages/characters/Characters';
import IsAuthorized from '../utils/IsAuthorized';
import SignIn from '../components/signin/SignIn';
import SignUp from '../components/signup/SignUp';
import AuthPage from '../pages/auth/AuthPage';
import MyCollection from '../pages/myCollection/MyCollection';


const PrivateRoute = ({ component: Component, is_authorized, redirectPath, ...args }) => {
    const navigate = useNavigate();

    useEffect(() => {
        if (!is_authorized) {
            console.log("User is not authorized!");
            navigate(redirectPath);
        }
    }, [is_authorized, navigate, redirectPath]);

    return is_authorized ? <Component {...args} /> : null;
};

const router = createBrowserRouter([
    {
        path: "/",
        element: <App />,
        errorElement: <ErrorComponent />,
        children: [
            {
                index: true,
                element: <Home />
            },
            {
                path: '/login/',
                element: <AuthPage />,
                children: [
                    {
                        path: 'sign-in/',
                        element: <SignIn />
                    },
                    {
                        path: 'sign-up/',
                        element: <SignUp />
                    },
                ],
            },
            {
                path: '/seasons/',
                element: <Seasons />,
            },
            {
                path: '/characters/',
                element: <Characters />,
            },
            {
                path: '/my-collection/',
                element: <PrivateRoute
                    authorized={IsAuthorized}
                    redirectPath="/login/sign-in/"
                    component={MyCollection}
                />
            }
        ],
    }
]);

export default router;