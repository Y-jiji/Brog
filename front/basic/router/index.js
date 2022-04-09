import React, {Component} from "react";
import { HashRouter, Switch, Route, Redirect } from 'react-router-dom';
import login from "@/basic/login"
import signup from "@/basic/signup"

export default class RouteConfig extends Component{
    render(){
        return(
            <HashRouter>
                <Switch>
                    <Route path="/login" component={login} />
                    <Route path="/signup" component={signup} />
                    <Redirect to="/" />
                </Switch>
            </HashRouter>
        )
    }
}