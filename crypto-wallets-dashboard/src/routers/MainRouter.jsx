import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";

import NavBar from "../components/NavBar";

import RichListPage from "../pages/RichListPage";
import HomePage from "../pages/HomePage";

const MainRouter = () => {
    return(
        <Router>
            <NavBar/>
            <Routes>
                <Route path="/richlist/:network" element={<RichListPage/>} exact/>
                <Route path="/" element={<HomePage/>} exact/>
            </Routes>
        </Router>

    )
}

export default MainRouter;