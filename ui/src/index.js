import React from "react";
import ReactDOM from "react-dom";
import "./index.css";
import reportWebVitals from "./reportWebVitals";
import LabelingScreen from "./components/LabelingScreen";

ReactDOM.render(
    <React.StrictMode>
        <LabelingScreen />
    </React.StrictMode>,
    document.getElementById("root")
);

reportWebVitals();
