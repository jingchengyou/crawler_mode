# 求职论坛信息爬虫

## 爬取信息：
- 邮箱 （最重要）
- 电话
- 发帖时间 （次重要）
- 标题

## 要求（按重要性排名）：
1. 邮箱相同，帖子不同，只留发帖时间最新的帖子
2. 一个帖子有多个邮箱，都保留，但是存储时，一行只保留一个邮箱
3. 帖子回复内容不爬


## MongoDB中数据项:
- article_id:字符串   (可选)文章id,全局唯一,多为链接中获取
- article:字符串 招聘信息文章内容
- article_link:字符串 文章链接
- title:字符串 文章标题
- update_time:字符串 最后更新或阅读时间
- publish_time:字符串 招聘信息发表时间
- email:列表 文章内容解析后的邮箱
- telephone:列表 电话
- status: 文章操作状态
    - not_done:文章未抓取
    - fetched:文章已抓取,但未解析
    - done: 文章已解析,获得邮箱,但未全局除重
    - one: 文章已除重,邮箱全局唯一,但未输出
    - output:文章已输出!!!!
    - not-used: 无用文件,垃圾箱
    