import React, { useState } from 'react'
import Card from '../components/Card'
import ArticlesButton from '../components/ArticlesButton'
import CardList from '../components/CardList'


function ArticlesPage() {

    const [articles, setArticles] = useState([]);


    const fetchArticles = (fetchedArticles) => {
        setArticles(fetchedArticles);
        console.log(fetchedArticles);
    }

    return (
        <>
        <div className = " pl-4 pt-4 flex flex-col">
            <h2 className = "font-mono top-4 left-4 text-5xl font-bold text-blue-500">FairFrame </h2>
            <h2 className = "font-mono top-4 left-4 text-5xl font-bold text-blue-500">Politices</h2>
        </div>

        <div className = " justify-center gap-4 ">
            <ArticlesButton label="Democratic" color="bg-blue-500" colorHov = "bg-green-700" fetchArticlesFunc = {fetchArticles} />
            <ArticlesButton label="Republican" color="bg-red-500" colorHov = "bg-green-700" fetchArticlesFunc = {fetchArticles}/>
        </div>
        
            <div className="relative min-h-screen">
                <div className="absolute bottom-0 right-0  bg-gray-200 p-6 rounded-lg w-full sm:w-5/6 md:w-5/6 lg:w-5/6 xl:w-5/6 h-[100%] overflow-y-auto">
                    <div className="flex flex-col gap-4">

           
                    <CardList articles={articles} />
                    
                    </div>
                </div>
            </div>
            
            
            
        </>

    )
}

export default ArticlesPage

