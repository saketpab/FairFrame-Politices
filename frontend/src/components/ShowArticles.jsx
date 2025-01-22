import {useEffect, useState} from 'react';


function ShowArticles({affiliation}){

    const [articles, setArticles] = useState('api not called yet');

    const aff = {affiliation: affiliation};
    console.log(aff);

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
                setArticles(data);
            }
                
                
            catch(error){
                    console.error('There was a problem with your fetch operation:', error);
            }
    };
    
    useEffect(() => {
        // Make the API call when the component mounts

        fetchData(aff);
        },[]);
    
    console.log(articles);
    return(articles)
}

export default ShowArticles;