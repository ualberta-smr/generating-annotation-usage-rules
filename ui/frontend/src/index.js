import React from "react";
import ReactDOM from "react-dom";
import "./index.css";
import reportWebVitals from "./reportWebVitals";
import LabelingScreen from "./components/LabelingScreen";
import ShortRulepad from "./monacoSyntaxHighlighting";

new ShortRulepad().register()

ReactDOM.render(
    <React.StrictMode>
        <LabelingScreen />
    </React.StrictMode>,
    document.getElementById("root")
);

reportWebVitals();
