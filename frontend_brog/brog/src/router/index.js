import App from '../test9'

import Error from "../pages/Error"
import Login from "../pages/Login"
import Signup from "../pages/Signup"
import Center from '../pages/Center'
import Reader from '../pages/Reader'
import { HashRouter,Route, Routes } from 'react-router-dom'

const BaseRouter = () =>{
    return (
        <HashRouter>
            <Routes>
                <Route path = '/' element = {<App />}>
                    <Route path='/login' element = {<Login />}></Route>
                    <Route path='/signup' element = {<Signup />}></Route>
                    <Route path='/center' element = {<Center />}></Route>
                    <Route path='/reader' element = {<Reader />}></Route>
                </Route>
                <Route path = "*" element={<Error />}></Route>
            </Routes>
        </HashRouter>
    )
}

export default BaseRouter;

