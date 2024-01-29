import React, { useState, useEffect  } from "react";
import axios from "axios";
import { API_DJANGO, API_REACT } from '../api/config'
import { Link } from "react-router-dom";

function CategoryList() {
    const [details, setDetails] = useState([]); 
    useEffect(() => {
        const fetchData = async () => {
          const res = await axios(`${API_DJANGO}category/`)        
              setDetails(res.data)
        }
        fetchData()
        console.log('details2 ->', API_DJANGO)
    }, []);

    return (
        <>
        Категории:
        <ul>
        {details.map((item) =>(
               <li>
               <Link to={`${API_REACT}category/${item.id}/recipe/`} key={item.id}>{item.name}</Link>
               </li>
        ))
        }
        </ul>
        </>
    )
}

export default CategoryList;
