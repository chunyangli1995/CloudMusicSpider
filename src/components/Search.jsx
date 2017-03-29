import React from 'react'
import style from '../css/Search.css'

export  default class Search extends React.Component {
	
	constructor(props) {
	    super(props);
	    this.state = {
	    	search_content: '输入要检索的网易云音乐用户名...'
	    }
	    this.handleClick = this.handleClick.bind(this);
  	}
	
	handleClick() {
    	this.props.history.push(
    		{ 
    			pathname: '#searchresult', 
    			state: { search_content: this.state.search_content } 
    		}
    	);
  	}
	
	render() {
		return (
			<div className='searchUser'>
				<input type='text' onChange={
					(event) => {
                    	this.state.search_content = event.target.value;
                	}
				} placeholder={this.state.search_content} ref='input' />
				<button onClick = {this.handleClick}>
					Search
				</button>
			</div>
		)
	}
}
