## 需求

>在网易云音乐这个平台上，爬取一个用户的基本信息，汇总分析，并以图表形式展示出来，便于我们看到一个用户对音乐的喜好情况以及对音乐类软件的使用习惯。

### Input：
网易云音乐用户名  

### Output：
图表信息，对该用户的基本信息的分析汇总

### 如何根据用户名字定位到确定的用户？

爬虫去爬取网易云音乐的搜索数据，提供搜索分页功能，让使用者自己确认要搜索的用户。

### 图表展示数据的维度

* 头像
* 昵称
* 性别
* 等级
* 动态数量
* 关注数量
* 粉丝数量
* 自己创建的歌单的数量
* 收藏的歌单的数量
* 本周内听歌排行榜统计图(歌手和评论两个维度)
* 所有时间听歌排行榜统计图(歌手和评论两个维度)


## 分析

### 前端

react框架组件化开发，主要是搜索、搜索结果分页、图表数据展示三部分。

### 后端

基于tornado的一个web服务器，提供restful API，爬虫使用scrapy框架，向前端返回json数据。

## 计划

1.API文档的补充  
2.后端开发  
3.前端开发(暂时使用假数据mock)  
4.前后端联调