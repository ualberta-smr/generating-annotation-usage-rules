import { useLocation, useNavigate } from 'react-router-dom'
import './LoginScreen.scss'

function LoginScreen() {

    const navigate = useNavigate();
    const location = useLocation();

    const handleEnterEvent = (event) => {
        if (event.key === 'Enter') {
            const value = event.target.value
            if (value.trim() !== "") {
                window.localStorage.setItem("RVT:Username", value.trim())
                navigate("/home" + location.search);
            }
        }
    }

    return (
        <div className="app">
            <div className="heading">
                <h1>Rule Authoring Tool</h1>
            </div>
            <div className="login-section">
                <input className='username' type="text" placeholder='Username...' onKeyDown={handleEnterEvent} />
            </div>
        </div>
    )
}

export default LoginScreen;