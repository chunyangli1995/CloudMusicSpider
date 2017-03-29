import React from 'react';

export default class SearchResult extends React.Component {
	
	constructor(props) {
	    super(props);
	    this.state = {}
  	}
	
	componentWillMount() {
		alert(this.props.location.state.search_content)
	}
	
	render() {
		return (
			<h></h>
		)
	}
}
