import React from "react";
import ReactDOM from "react-dom";
import "./index.css";
import reportWebVitals from "./reportWebVitals";
import LabelingScreen from "./screens/labeling/ExperimentalLabelingScreen";

ReactDOM.render(
    <React.StrictMode>
        <LabelingScreen />
    </React.StrictMode>,
    document.getElementById("root")
);

reportWebVitals();
