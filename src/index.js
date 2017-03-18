import React from 'react';
import ReactDOM from 'react-dom';
import App from './components/App';
import {createStore} from 'redux'
import { Provider } from 'react-redux';
import combineReducers from './reducers/reducers'

let store = createStore(combineReducers)

let rootElement = document.getElementById('root')

ReactDOM.render(
	<Provider store={store}>
		<App />
	</Provider>,
	rootElement
);
