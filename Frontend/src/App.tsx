import NavBar from './NavBar'
import { Outlet } from 'react-router'
import { useState } from 'react'

function App() {
  const [loggedIn, setLoggedIn] = useState(false);

  return (
    <>
      <NavBar loggedIn={loggedIn}/>
      <Outlet/>
    </>
  )
}

export default App
