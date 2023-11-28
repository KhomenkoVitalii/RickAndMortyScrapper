import { createBrowserRouter } from 'react-router-dom'
import App from '../pages/App'
import Home from '../pages/home/Home'
import Episode from '../pages/episodes/Episode';
import ErrorComponent from '../components/error/ErrorComponent';
import Seasons from '../pages/seasons/Seasons';
import Characters from '../pages/characters/Characters';


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
                path: '/seasons/',
                element: <Seasons />,
            },
            {
                path: '/characters/',
                element: <Characters />,
            },
            {
                path: '/my-collections/',
                element: <ErrorComponent />
            }
        ],
    }
]);

export default router;