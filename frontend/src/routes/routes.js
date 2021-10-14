import React, { Component } from 'react';
import { BrowserRouter as Router } from 'react-router-dom';
import Route from 'react-router-dom/Route';

import Login from './Login';
import Cadastro from './Cadastro';
import ListaWebsites from './Websites';
import ListaSetores from './Setores';

import '../Styles/App.css';

class Routes extends Component{
    render() {
        return (
            <div className="App">
                <Router>
                    <div>
                        <Route path="/" exact component={Login} />
                        
                        <Route path="/cadastro" exact component={Cadastro} />

                        <Route path="/websites" exact component={ListaWebsites} />

                        <Route path="/listasetores/:idwebsite" exact component={ListaSetores} />

                    </div>
                </Router>
            </div>
        );
    }
}

export default Routes;