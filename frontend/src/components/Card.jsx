
import ABCnews from '../assets/ABCnews.png';
import cbs_news from '../assets/cbs_news.png';
import fox_news from '../assets/fox_news.png';
import pic from '../assets/pic.png';

function Card(props) {

    let hashMap = new Map();
    hashMap.set("ABC News", ABCnews);
    hashMap.set("CBS News", cbs_news);
    hashMap.set("Fox News", fox_news);
    hashMap.set("pic", pic);

    const image = hashMap.get(props.source);

    if (hashMap.has(props.source)){
        const image  = hashMap.get(props.source);
    }
    else{
        const image = hashMap.get("pic");
    }
    
  return (
    
    
    <a href={props.url} target="_blank" rel="noreferrer">
        <div className = "rounded-lg shadow-md p-4 bg-white m-4 flex hover:bg-red-100">
        
            <img src={image} alt = "Photo not available " className = "w-60 h-60"></img>

            <div className = "p-6  py-1">
                <h2 className = "text-3xl font-bold  text-gray-800 py-2">{props.title}</h2>
                <p className = "text-3x1  font-bold text-grey-600">{props.source}</p>
                <p className = "py-10">{props.description}</p>
            </div>
        </div>
    </a>
    
 /*
    <a href='https://jobright.ai/jobs/recommend?pos=100' target="_blank" rel="noreferrer">
        <div className = "rounded-lg shadow-md p-4 bg-white m-4 flex hover:bg-red-100">
        
            <img src={ABCnews} alt = "Photo not available " className = "w-60 h-60"></img>

            <div className = "p-6  py-1">
                <h2 className = "text-3xl font-bold  text-gray-800 py-2">Johnson meets with Republicans undecided on whether he should remain speaker</h2>
                <p className = "text-3x1  font-bold text-grey-600">ABC News</p>
                <p className = "py-10">President-elect Donald Trump said this week he plans to attend former President Jimmy Carter's funeral following a history of mutual criticism.
                Carter, who died on Dec. 29 at the age of 100, will be honored with a state funeral at Washington National Cathedral on Thursday, Jan. 9. President Joe Biden is expected to deliver the eulogy.
                "I'll be there. We were invited," Trump told reporters on Tuesday night, though he declined to say if he'd spoken with any members of the Carter family.</p>
            </div>
        </div>
    </a>
    */
    
    
    
  );
}

export default Card;