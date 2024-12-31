import { useNavigate } from "react-router-dom";

function ProductButton(props) {

    const navigate = useNavigate();
  
    const handleClick = () => {
        navigate("/articles");
    }

    return(<button onClick= {handleClick}className="bg-blue-500 font-bold text-white py-3 px-6 rounded-lg shadow-lg hover:bg-blue-700 transition-all duration-300"> Use FairFrame</button>);
  
}

export default ProductButton