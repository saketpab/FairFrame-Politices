import Card from './Card';

function CardList({ articles }) {

  //const articles = [articlesa]

  //console.log(Array.isArray(articles));

  return (
    <div className="card-list">
      {articles.map((article,index) => (
        <Card 
            key={article.id || index}
            url={article.url} 
            title={article.article_title}
            source={article.source}
            description={article.description}
        />
      ))}
    </div>
  );
}

export default CardList;