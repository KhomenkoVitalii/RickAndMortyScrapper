import { createBrowserRouter } from 'react-router-dom'
import App from '../pages/App'
import Home from '../pages/home/Home'
import Episode from '../pages/episodes/Episode';
import ErrorComponent from '../components/error/ErrorComponent';


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
                path: '/episodes/',
                element: <Episode />,
            }
        ],
    }
]);

export default router;