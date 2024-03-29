import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './pages/App'
import { RouterProvider } from 'react-router-dom'
import router from './routes/AppRouter'
import { AppContextProvider } from './context/AppContext'

ReactDOM.createRoot(document.getElementById('root')).render(
  <>
    <AppContextProvider>
      <RouterProvider router={router}>
        <App />
      </RouterProvider>
    </AppContextProvider>
  </>,
)
