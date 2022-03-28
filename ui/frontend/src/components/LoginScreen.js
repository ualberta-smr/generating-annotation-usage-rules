import { useLocation, useNavigate } from 'react-router-dom'
import './LoginScreen.scss'
import { BACKEND_URL, LS_USERNAME } from './constants';
import { useState } from 'react';

function LoginScreen() {

    const EMPTY_ERROR = {
        errorMarker: "",
        snackbarClass: "",
        errorMessage: ""
    };

    const [error, setError] = useState(EMPTY_ERROR)

    const navigate = useNavigate();
    const location = useLocation();

    const handleEnterEvent = (event) => {
        if (event.key === 'Enter') {
            const value = event.target.value
            if (value != null && value.trim() !== "") {
                const username = value.trim();

                fetch(`${BACKEND_URL}/users?q=${username}`)
                    .then(req => {
                        if (req.status === 404) {
                            // this user does not exist
                            setError({
                                errorMarker: "error-marker",
                                snackbarClass: "show",
                                errorMessage: `Incorrect username`
                            });
                            setTimeout(function(){ setError(EMPTY_ERROR); }, 3000);
                        } else if (req.status === 200) {
                            setError(EMPTY_ERROR);
                            window.localStorage.setItem(LS_USERNAME, username)
                            navigate("/home" + location.search);
                        }
                    }).catch(err => {
                        console.error(err)
                    })
            }
        }
    }

    return (
        <div className="app">
            <div className="heading">
                <h1>Rule Authoring Tool</h1>
            </div>
            <div className="login-section">
                <input className={`username ${error.errorMarker}`} type="text" placeholder='Username...' onKeyDown={handleEnterEvent} />
            </div>
            <div className={`snackbar ${error.snackbarClass}`}>{error.errorMessage}</div>
        </div>
    )
}

export default LoginScreen;