import React from 'react'
import { Link, BrowserRouter, Routes, Route, Router } from 'react-router-dom'
import RecipeList from './RecipeList'
import Recipe from './Recipe';
import CategoryList from './CategoryList';
import SwaggerUI from "swagger-ui-react"
import "swagger-ui-react/swagger-ui.css"

function Main() {

    return (
      <BrowserRouter>
      <main>
        <header>Главная страница учебный пример Django - React</header>
        <hr></hr>

        <br></br>
        <Link to='/api'>API</Link>
        <br></br>
        <Link to={`category/`} >Категории блюд</Link>
        <br></br>
        <Routes>
          <Route path="recipe/:idd"  element={<Recipe />} />
          <Route path="category/:id/recipe/"  element={<RecipeList />} />
          <Route path="category/" element={<CategoryList />} />
          <Route path='/api' element={<SwaggerUI url="api.yaml" />} />
        </Routes>
      </main>
      </BrowserRouter>  
    )
  }

export default Main;

