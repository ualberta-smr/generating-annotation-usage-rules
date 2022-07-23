import './NewPackageCreationScreen.scss'
import { BACKEND_URL } from './constants';
import { useState } from 'react';

function NewPackageCreationScreen() {

    const [username, setUsername] = useState(null);
    const [packageName, setPackageName] = useState(null)
    const [file, setFile] = useState(null);

    const EMPTY_ERROR = {
        errorMarker: "",
        snackbarClass: "",
        errorMessage: ""
    };

    const [error, setError] = useState(EMPTY_ERROR)

    const handleChangeUsername = (e) => {
        setUsername(e.target.value)
    }

    const handleChangePackageName = (e) => {
        setPackageName(e.target.value)
    }

    const handleChangeFile = (e) => {
        setFile(e.target.files[0])
    }

    const handleSend = () => {
        const data = new FormData()
        data.append('rulesFile', file)

        const packageNamePart = packageName ? `&packageName=${packageName}` : ""; 

        fetch(`${BACKEND_URL}/packages?username=${username}${packageNamePart}`, {
            method: 'POST',
            body: data
        }).then(resp => {
            if (resp.status === 200) {
                // success
                setError({
                    errorMarker: "",
                    snackbarClass: "show",
                    errorMessage: `Success`
                });
            } else if (resp.status === 409) {
                // username already exists
                setError({
                    errorMarker: "error-marker",
                    snackbarClass: "show",
                    errorMessage: `Username already exists`
                });
            } else if (resp.status >= 400 && resp.status <= 499) {
                // failed to process the request
                setError({
                    errorMarker: "",
                    snackbarClass: "show",
                    errorMessage: `Unknown error`
                });
            }
            setTimeout(function(){ setError(EMPTY_ERROR); }, 3000);
        })
    }

    return (
        <div className="app-package">
            <div className="heading">
                <h1>Create New Package</h1>
            </div>
            <div className="package-section">
                <input onChange={handleChangeUsername} className={`username ${error.errorMarker}`} type="text" placeholder='Username' />
                <input onChange={handleChangePackageName} className={`username`} type="text" placeholder='Package name' />
                <input onChange={handleChangeFile} className={`username file`} type="file" multiple={false} accept="application/json, text/json"/>
                <button onClick={handleSend} className='username'>Create</button>
            </div>
            <div className={`snackbar ${error.snackbarClass}`}>{error.errorMessage}</div>
        </div>
    )
}

export default NewPackageCreationScreen;