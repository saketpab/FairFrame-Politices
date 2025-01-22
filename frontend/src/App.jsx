import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import {BrowserRouter, Routes, Route} from 'react-router-dom'
import HomePage from './routes/HomePage'
import ArticlesPage from './routes/ArticlesPage'

function App() {

  

  return (
    <>
      <div>
       <BrowserRouter>
        <Routes>
          <Route index element={<HomePage/>} />
          <Route path = "/home" element={<HomePage/>} />
          <Route path = "articles" element = {<ArticlesPage/>} />
        </Routes>
       </BrowserRouter>
      </div>
      
    </>
  )
}

export default App

