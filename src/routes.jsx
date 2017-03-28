import App from './components/App';
import { IndexRoute, Route } from 'react-router'
import React from 'react';
import Search from './components/Search'
import SearchResult from './components/SearchResult'
import User from './components/User'

export default (
	<Route path='/' component={App}>
		<IndexRoute component={Search} />
		<Route path='search' component={Search} />
		<Route path='searchresult' component={SearchResult} />
		<Route path='user' component={User} />
	</Route>
)
