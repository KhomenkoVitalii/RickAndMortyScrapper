import { createBrowserRouter } from 'react-router-dom'
import App from '../pages/App'
import Home from '../pages/home/Home';

const router = createBrowserRouter([
    {
        path: "/",
        element: <App />,
        loader: rootLoader,
        children: [
            {
                index: true,
                element: <Home />
            },
        ],
    }
]);

export default router;