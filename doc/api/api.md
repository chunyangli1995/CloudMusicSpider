##  GET /search

### description

搜索网易云音乐上的某种内容，并返回json数据。(比如搜索用户)

### params:

s: 要搜索的内容  
pageNum: 页码  
type: 搜索的类型(用户是1002)

### 返回结果


	http://localhost:8888/search?type=1002&s=%E6%9D%8E%E6%98%A5%E9%98%B3&pageNum=1

	{
		result: {
			userprofiles: [
				{
					defaultAvatar: false,
					province: 110000,
					authStatus: 0,
					followed: false,
					avatarUrl: "http://p1.music.126.net/QSY6BnxR8LpT2iBsM9RMuw==/2873023883426817.jpg",
					accountStatus: 0,
					gender: 1,
					city: 110108,
					birthday: -2209017600000,
					userId: 115005584,
					userType: 0,
					nickname: "李春阳_YY",
					signature: "程序员",
					description: "",
					detailDescription: "",
					avatarImgId: 2873023883426817,
					backgroundImgId: 2002210674180201,
					backgroundUrl: "http://p1.music.126.net/o3G7lWrGBQAvSRt3UuApTw==/2002210674180201.jpg",
					authority: 0,
					mutual: false,
					expertTags: null,
					djStatus: 0,
					vipType: 0,
					remarkName: null,
					avatarImgIdStr: "2873023883426817",
					backgroundImgIdStr: "2002210674180201",
					followeds: 3,
					follows: 0,
					eventCount: 0,
					playlistCount: 3,
					playlistBeSubscribedCount: 0
				},
				{
					defaultAvatar: false,
					province: 410000,
					authStatus: 0,
					followed: false,
					avatarUrl: "http://p1.music.126.net/vHF2M7XmoL6qwNXeFbb11g==/1382086116461710.jpg",
					accountStatus: 0,
					gender: 1,
					city: 410100,
					birthday: -2209017600000,
					userId: 137570254,
					userType: 0,
					nickname: "李春阳指导",
					signature: "",
					description: "",
					detailDescription: "",
					avatarImgId: 1382086116461710,
					backgroundImgId: 2002210674180199,
					backgroundUrl: "http://p1.music.126.net/VTW4vsN08vwL3uSQqPyHqg==/2002210674180199.jpg",
					authority: 0,
					mutual: false,
					expertTags: null,
					djStatus: 0,
					vipType: 0,
					remarkName: null,
					avatarImgIdStr: "1382086116461710",
					backgroundImgIdStr: "2002210674180199",
					followeds: 1,
					follows: 1,
					eventCount: 0,
					playlistCount: 3,
					playlistBeSubscribedCount: 0
				}
			],
			userprofileCount: 27
		},
		code: 200
	}


## GET /user/(user_id)

### description

获得一个用户在网易云音乐上的一些基本数据。

### 返回结果

	http://127.0.0.1:8888/user/109284159
	{
		songsall: [
			{
		      "playTime": 217779,
		      "authors_info": [
		        {
		          "author_name": "Charlie Puth",
		          "author_link": "http://music.163.com/artist?id=90331"
		        },
		        {
		          "author_name": "Selena Gomez",
		          "author_link": "http://music.163.com/artist?id=140196"
		        }
		      ]
    		},
			{
		      "playTime": 150824,
		      "authors_info": [
		        {
		          "author_name": "花粥",
		          "author_link": "http://music.163.com/artist?id=8103"
		    	}
			  ],
 			}
		]
		collectlistCount: 19
	}
