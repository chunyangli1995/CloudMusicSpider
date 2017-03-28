import { Router, hashHistory } from 'react-router'
import routes from './routes'
import React from 'react';
import ReactDOM from 'react-dom';


ReactDOM.render(
	<Router history={ hashHistory }>
		{ routes }
	</Router>,
	document.getElementById('root')
);
