import React from 'react'
import style from '../css/Search.css'

export  default class Search extends React.Component {
	render() {
		return (
			<div className='searchUser'>
				<input type='text' placeholder='输入要检索的网易云音乐用户名...' ref='input' />
				<button>
					Search
				</button>
			</div>
		)
	}
}
