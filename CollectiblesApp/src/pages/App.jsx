import { useState } from 'react'
import { Outlet } from 'react-router-dom';
import Header from '../components/header/Header';
import Footer from '../components/footer/Footer';
import Starfield from '../components/background/Starfield';

function App() {
  return (
    <>
      <Header />
      <Outlet />
      <Footer />
      <Starfield
        starCount={1000}
        starColor={[255, 255, 255]}
        speedFactor={0.05}
        backgroundColor="black"
      />
    </>
  )
}

export default App;