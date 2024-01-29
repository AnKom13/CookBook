import React, { useState, useEffect  } from "react";
import axios from "axios";
import { API_DJANGO } from '../api/config'
import { useParams } from "react-router-dom";

function Recipe() {
    const params = useParams();
    const [details, setDetails] = useState([]); 
    const [cat, setCat] = useState([]); 
    useEffect(() => {
        const fetchData = async () => {
          const res = await axios(`${API_DJANGO}/recipe/${params.idd}`)        
              setDetails(res.data)
          const tmp =  res.data[0].category
          const r = await axios(`${API_DJANGO}/category/${tmp}`)        
              setCat(r.data[0].name)
        }
        fetchData()

    }, []);

    return (
        <>
        Детальная информация о рецепте:
        <br></br>
        Категория: {cat}
        {details.map((item) =>(
            <div>
            <br></br>
            Название: {item.name}
            <br></br>
            Состав: {item.content}
            </div>
        ))
        }
        </>
    )
}

export default Recipe;
