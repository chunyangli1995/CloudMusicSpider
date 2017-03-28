import React from 'react';
import style from '../css/base.css'

export default class App extends React.Component {
	
	render(){
		return (
			<div>
				{this.props.children}
			</div>
		)
	}
	
}
