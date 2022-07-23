import React from "react";
import ReactDOM from "react-dom";
import "./index.css";
import reportWebVitals from "./reportWebVitals";
import LabelingScreen from "./components/LabelingScreen";
import ShortRulepad from "./monacoSyntaxHighlighting";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import LoginScreen from "./components/LoginScreen";
import NewPackageCreationScreen from "./components/NewPackageCreationScreen";

new ShortRulepad().register()

ReactDOM.render(
    <React.StrictMode>
        <BrowserRouter>
            <Routes>
                <Route path="/" element={<LoginScreen />} />
                <Route path="/home" element={<LabelingScreen />} />
                <Route path="/package" element={<NewPackageCreationScreen />} />
            </Routes>
        </BrowserRouter>
    </React.StrictMode>,
    document.getElementById("root")
);

reportWebVitals();
