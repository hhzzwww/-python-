
/*
    开发环境（windows）：phpstudy 安装使用简单
    生成环境（linux）： 可以给所有的人使用

    excel（office，wps）           sql（mysql,sqlite,sql server）
    maoyan.xlsx                   数据库（database）
    sheet 表                       数据表（tables）
    数据列                          字段
    数据行                          记录

 */

show databases; -- 展示数据库列表，相当于展示excel文件

-- 1.打开数据库
-- 创建数据库---相当于创建excel文件
create database python character set  'utf8mb4'; -- 一般设置为utf8，utf8mb4 是为了兼容emoji图片
-- 如果不是 utf8 编码不能存中文内容
-- 删除数据库
drop database python; -- 删除数据库列表中的python数据库

-- 创建数据表
use python; -- 使用数据库
show tables ;

-- sql不区分大小写
/*
 创建数据表
 CREATE TABLE 表名(
    字段名 字段类型[(长度)] [约束]
    字段名 字段类型[(长度)] [约束]
    ...
   字段名 字段类型[(长度)] [约束]
   字段名 字段类型[(长度)] [约束]
 );
 */

# char 固定长度的字符串 -- 固定长度储存储存空间
#varchar 变长度字符串 --按照实际长度储存空间  -- 最长255个字符
# datetime 时间类
# Text

drop table student; -- 删除学生表
create  table student(
    id int primary key auto_increment, -- 主键，数据约束的时候详细讲
    name varchar(20), -- 人名应该给多少位
    math float,
    chinese float,
    english float,
    phone  char(11)-- 电话号码应该是什么类型，以及给多长？

);

/*
 INSERT INTO 表名（字段列表）
 VALUES(字段值列表),(字段值列表),(字段值列表),(字段值列表);

 */

 -- 一般不手动插入 id 字段
insert into student(name,math,chinese,english) value ('张三','60','60','60'); -- 插入字段
insert into student(name,math,chinese,english) value ('李四','60','60','60');
insert into student(name,math,chinese,english) value ('王五','60','60','60');

insert into student(name,math,chinese,english)
values ('张三','60','60','60'),
       ('李四','60','60','60'),
       ('王五','60','60','60');
select * from student;


-- 查看数据表的信息
desc student;

use mysql;
show tables;
desc user;
select  * from user;  -- 查询 user表中数据

-- 数据类型

-- -----------------------------------------
drop table top100;
create  table top100(
    id int primary key auto_increment, -- 主键，数据约束的时候详细讲
    name varchar(20), -- 人名应该给多少位
    math float,
    chinese float,
    english float,
    phone  char(11)-- 电话号码应该是什么类型，以及给多长？

);
insert into top100(name,math,chinese,english)
value ('小明','60','60','60');

select * from top100;

-- 数据表修改
desc top100;
alter table top100 modify column  name varchar(200);

-- 新增字段
alter table top100 add column country varchar(20);

#UPDATE 表名 SET 字段名=值，字段名 = 值
#WHERE 筛选条件；
update top100 set country= '中国' where name = '小明';

-- 删除字段
alter table top100 drop  column country;

-- 重命名字段
alter table top100 change country country2 varchar(20);

drop table student;
insert into student(name,math,chinese,english)
values ('张三','60','60','60'),
       ('李四','60','60','60'),
       ('王五','60','60','60');
insert into student(name,math,chinese,mysql.student.english) value ('张三','60','60','60'); -- 插入字段
insert into student(name,math,chinese,mysql.student.english) value ('李四','60','60','60');
insert into student(name,math,chinese,mysql.student.english) value ('王五','60','60','60');
select * from student;

-- 更新数据
/*  UPDATE 表名 SET 字段名 = 值，字段名 = 值 WHERE 筛选条件;*/
UPDATE student SET chinese = 100 WHERE name = '张三';
UPDATE  student SET  english = 100 WHERE id = 2;


-- 删除数据
/* DELETE FROM 表名 WHERE 筛选条件；*/
delete  from student where id = 1;

-- 数据查询功能
/* select * from student;*/
select * from student;
select name, math from student;

-- 查询去重
select math,english from student;
select distinct math,english from student;

-- 条件查询
/* 比较运算符 = > < !=
   逻辑运算符 and not or
   身份运算符 in not
   模糊匹配 like _ % 下划线代替一个字符|%代替很多字符
 */
-- 数学小于100的分数
select * from student where  math< 100;

-- 数学成绩 大于 50 ，小于 80的成绩查询
select * from student where math < 80 and math > 50;
-- 数学成绩 大于 50 ，小于 80,英语成绩大于50的成绩查询
select * from student where math < 80 and math > 50 and english > 50;
-- 数学成绩 大于 50 ，小于 80,英语成绩大于80或小于70的成绩查询
select * from student where math < 80 and math > 50 and (english > 80 or english < 70);


-- 不看小明的成绩
select * from student where name not in ('小明');

-- 模糊匹配
-- 数学成绩为60的学生
-- 15.6英寸的游戏本  like '*15.6*' 或者like '*15.6英寸的游戏_'
select * from student where math like '60';

-- 排序 升序 asc(默认),降序 desc
select * from student
where math like '60' order by math desc; -- desc 表示降序 -- order by 字段 根据某一个字段进行排序，默认是升序

-- 类型排序
select * from student order by math;
#多重类型排序
select * from student order by math,english;

-- 常用函数
-- 数据库中总共有多少个商品
select count(*) as total from student;
select count(*) as total from student where name = '李四';
select count(*) as total from student where name = '王五';

#分组查询
#查看一下数学成绩为60分的有多少个学生
select * from student order by math = '60';

#从student查询名字为name的有多少人，计算总数记为total，然后计算 name 的平均数学成绩 --按照name的升序排序
select name,count(*) as total,avg(math) as avg_math from student group by name;


-- 案例
-- 创建数据库
show databases ;
create database hzw_18080008 character set 'utf8mb4';

use hzw_18080008;
drop table  jd;

create table jd(
    id int primary key auto_increment,
    name varchar(255),
    price float,
    commit varchar(20),
    shop_name varchar(100)
);

desc jd;

insert into jd(name,price,commit,shop_name)
value ("华为笔记本电脑MateBook 14 2021款 14.0英寸11代酷睿i5 16G 512G 锐炬显卡/2K触控轻薄本 /多屏协同 深空灰","5499.00","10万+条评价","华为京东自营官方旗舰店"),
("荣耀笔记本MagicBook X 14 2021 14英寸全面屏轻薄笔记本电脑 （i3 8GB 256GB多屏协同）冰河银","3199.00","10万+条评价","荣耀京东自营旗舰店"),
("惠普(HP)战66四代 14英寸轻薄笔记本电脑(英特尔酷睿11代i5 16G 512G 400尼特高色域 一年上门+意外 2年电池)","4299.00","20万+条评价","惠普京东自营官方旗舰店"),
("联想小新Air14Plus英特尔酷睿i5 14英寸全面屏轻薄笔记本电脑(i5-1155G7 16G 512G 2.2K屏 MX450独显)银","5298.00","20万+条评价","联想京东自营旗舰店"),
("联想ThinkPad E14 酷睿i7 14英寸轻薄笔记本电脑(i7-1165G7 16G 512G 100%sRGB)银","5898.00","5万+条评价","ThinkPad京东自营旗舰店"),
("联想笔记本电脑小新Air14锐龙版 14英寸全面屏办公轻薄本(6核R5-5500U 16G 512G 高色域 WiFi6)深空灰","3999.00","20万+条评价","联想京东自营旗舰店"),
("联想笔记本电脑 小新Air14Plus锐龙版 14英寸全面屏高性能独轻薄(6核R5-5600U 16G 512G 2.2K屏 满血MX450)灰","4799.00","20万+条评价","联想京东自营旗舰店"),
("惠普（HP）战66 四代 15.6英寸轻薄笔记本电脑（i5-1135G7 16G 512G 高色域 一年上门+意外 2年电池）","4999.00","20万+条评价","惠普京东自营官方旗舰店"),
("华硕（ASUS）VivoBook15 11代英特尔酷睿 15.6英寸轻薄办公笔记本电脑 i5-1135G7 16G 512G固态 锐炬显卡 银色","3999.00","5万+条评价","华硕电脑官方旗舰店"),
("戴尔(DELL)游匣G15 15.6英寸游戏笔记本电脑(八核i7 16G 512G RTX3060显卡 165Hz 100%sRGB高色域)耀夜黑","6499.00","20万+条评价","戴尔京东自营官方旗舰店"),
("攀升MaxBook P1X英特尔4核 15.6英寸商务办公手提轻薄笔记本电脑（10代J4125 12G 256G）2022新","1699.90","1万+条评价","攀升京东自营官方旗舰店"),
("戴尔笔记本电脑Dell灵越16Plus 英特尔酷睿16英寸轻薄全能本设计师 i7-11800H 32G 1TB RTX3060 3K屏 灰蓝","11499.00","5万+条评价","戴尔京东自营官方旗舰店"),
("RedmiBook Pro 14增强版 14英寸轻薄笔记本电脑（标压i5-11320H MX450 16+512G 2.5K全面屏 铝合金机身）灰","5599.00","5万+条评价","小米京东自营旗舰店"),
("联想ThinkBook 14 锐龙版(BGCD) 2021款 14英寸轻薄笔记本电脑(R5 5600U 16G 512G 高色域 Win11)","4099.00","10万+条评价","ThinkPad京东自营旗舰店"),
("联想ThinkBook 14 2021款 酷睿版(0SCD) 酷睿i5 14英寸轻薄笔记本(i5-1155G7 16G 512G 高色域 Win11)","4299.00","2万+条评价","ThinkPad京东自营旗舰店"),
("联想笔记本电脑 拯救者R9000X 15.6英寸高性能轻薄游戏本(锐龙8核R7-5800H 16G 512G RTX3060 2.5k 165Hz)灰","7999.00","10万+条评价","联想京东自营旗舰店"),
("小米 RedmiG 2021酷睿版 16.1英寸游戏笔记本电脑(十一代酷睿i5 11260H 16G 512G RTX3050 144Hz电竞屏)","5799.00","2万+条评价","小米京东自营旗舰店"),
("戴尔(DELL)游匣G15 15.6英寸游戏笔记本电脑(11代英特尔酷睿i5-11260H 16G 512G RTX3050 120Hz )耀夜黑","5799.00","20万+条评价","戴尔京东自营官方旗舰店"),
("联想拯救者R9000P 2021款电竞游戏笔记本电脑 RTX3060独显 八核新锐龙R7-5800H 16G内存 512G固态 标配版 16英寸 2.5K超高清｜165Hz专业电竞屏","8999.00","10万+条评价","联想华东授权专卖店"),
("联想笔记本电脑 拯救者Y7000P 英特尔酷睿i7 15.6英寸电竞游戏本(11代i7-11800H 16G 512G RTX3060 165Hz )黑","7999.00","5万+条评价","联想京东自营旗舰店"),
("荣耀MagicBook 14 2021 锐龙版 14英寸全面屏轻薄笔记本电脑(R5 5500U 16G 512G 7nm 多屏协同 高色域)冰河银","3999.00","5万+条评价","荣耀京东自营旗舰店"),
("联想笔记本电脑 拯救者Y7000P 15.6英寸高性能电竞游戏本(11代i7-11800H 16G 512G RTX3050Ti 165Hz高色域屏)","7299.00","5万+条评价","联想京东自营旗舰店"),
("联想拯救者R9000P 16英寸游戏笔记本电脑(新锐龙 8核 R7-5800H 16G 512G RTX3050Ti 2.5k 165Hz100%sRGB)灰","7299.00","10万+条评价","联想京东自营旗舰店"),
("ROG幻16 2022 第12代英特尔酷睿16英寸设计师高性能游戏笔记本电脑(i7-12700H 16G 512G RTX3060 2.5K165Hz)","11499.00","2000+条评价","玩家国度ROG京东自营官方旗舰店"),
("小米RedmiG 16.1英寸 2021款锐龙版 游戏电竞笔记本电脑( 8核 R7-5800H 16G 512G RTX3060 144Hz电竞屏)","6999.00","2万+条评价","小米京东自营旗舰店");

select * from jd;

truncate jd; -- 清空数据表
select  * from hzw_18080008.jd;


-- 查询 电影名，评分，关注数
select name,price,commit from hzw_18080008.jd;

-- 求所有电影的平均分数 保留两位小数
select  round(avg(price),2) from hzw_18080008.jd;
-- 查询每部电影中评分 最高、最低、平均评分、数量
select max(price) as max_price,
       min(price) as min_price,
       round(avg(price),1) as avg_price,
       count(*) as total
from hzw_18080008.jd;

-- 查询所有价格大于平均价格的笔记本，并且按评分降序排序
select avg(price) from hzw_18080008.jd;
select * from hzw_18080008.jd where price > 5975;









