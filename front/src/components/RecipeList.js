import React, { useState, useEffect  } from "react";
import axios from "axios";
import { API_DJANGO, API_REACT } from '../api/config'
import { Link, useParams } from "react-router-dom";

function RecipeList() {
    const params = useParams();
    const [details, setDetails] = useState([]); 
    useEffect(() => {
        const fetchData = async () => {
          const res = await axios(`${API_DJANGO}category/${params.id}/recipe/`)        
              setDetails(res.data)
        }
        fetchData()
  //      console.log('details2 ->', details)
    }, []);

    return (
        <>
        Рецепты:
        <ul>
        {details.map((item) =>(
               <li>
               <Link to={`${API_REACT}recipe/${item.id}`} key={item.id}>{item.name}</Link>
               </li>
        ))
        }
        </ul>
        </>
    )
}

export default RecipeList;
