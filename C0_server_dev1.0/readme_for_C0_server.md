一定要先运行initialize
一定要先运行initialize
一定要先运行initialize




接口说明：

/
创建队伍的测试GUI

/submitnewteam
需要post方法
加入队伍确认：
需要议项：
username         #学号
studentname   #学生名字 HTML escaped
password         #md5 hased, used for authentifacation
teamtype         # html escaped
peoplenum      #需要人数
description       # html escaped

这里会自动生成一个队伍请求的流水号RUID


/jointest
加入队伍测试GUI

/jointeam
需要post方法
加入队伍确认：
需要议项：
username         #学号
studentname   #学生名字 HTML escaped
password         #md5 hased, used for authentifacation
ruid        	        #想要加入队伍的RUID



/teamtable
已创建的队伍（返回的是csv看着有点奇怪）

/viewteam
需要url议项：
ruid   #就是流水号

查看队伍成员

/stuc
需要url议项：
un   #学号
pwd  #哈希过的密码

查看学生创建的队伍


/stuj
需要url议项：
un   #学号
pwd  #哈希过的密码

查看学生加入的队伍