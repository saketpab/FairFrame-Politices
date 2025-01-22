//import React, {useState, useEffect} from 'react';
//import useArticles from '../BackendCalls';
import ShowArticles from './ShowArticles';


function ArticlesButton({label,color,colorHov,fetchArticlesFunc }) {

    //const mess = useArticles();
    //console.log(mess);
    //ShowArticles(label);
  
    const handleClick = async () => {

        //console.log(cards)
        //ShowArticles(label);
        const fetchData = async (aff) => {

            try{
                const response = await fetch('http://127.0.0.1:8000/api/sum', {
                    method: 'POST',
                    headers: {
                      'Content-Type': 'application/json',
                    },
                    body: JSON.stringify(aff),
                  });

                if(!response.ok){
                    throw new Error('Network response was not ok');
                }
                const data = await response.json();
                //setArticles(data);
                return data;
            }
                
                
            catch(error){
                    console.error('There was a problem with your fetch operation:', error);
                    return null;
            }
        };
        console.log(label);
        const articles = await fetchData({affiliation: label});
        //console.log(articles.filteredArticles);

        fetchArticlesFunc(articles.filteredArticles);


        //console.log("in hnadleClick");
        //ShowArticles
    }

    return(<button onClick= {handleClick}className= {`${color} font-bold text-white w-40 py-3 px-6 rounded-lg shadow-lg hover:${colorHov} transition-all duration-300`}> {label}</button>);
  
}

export default ArticlesButton