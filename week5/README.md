# Task 1
**Install MySQL server**

<img width="350" alt="MySQL" src="https://github.com/user-attachments/assets/bc159e7d-41fd-4366-9da6-4f37a64b9844" />

___

# Task 2
**Create database and table in your MySQL server**

**建立 website 資料庫**  
```sql
-- 建立 website 資料庫
CREATE DATABASE website;
```
<img width="643" alt="creat-database" src="https://github.com/user-attachments/assets/a957efe5-ff0f-48e7-ae08-b2168e6f501e" />

**建立 member 資料表**  
```sql
-- 建立 member 資料表，包含欄位：id、name、username、password、follower_count 和 time
CREATE TABLE member (
    -> id BIGINT AUTO_INCREMENT PRIMARY KEY,
    -> name VARCHAR(255) NOT NULL,
    -> username VARCHAR(255) NOT NULL,
    -> password VARCHAR(255) NOT NULL,
    -> follower_count INT UNSIGNED NOT NULL DEFAULT 0,
    -> time DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
    -> );
```
<img width="502" alt="creat-table-member" src="https://github.com/user-attachments/assets/9d29ba54-cfb3-4e97-9676-edd57e821a6c" />

* member 資料表資訊 
<img width="714" alt="describe-member" src="https://github.com/user-attachments/assets/2a7db469-90a0-4f7f-946f-fd7e03b072b1" />

___

# Task 3
**SQL CRUD （建立、刪除、查詢、更新）**

* INSERT a new row to the member table where name, username and password must
be set to test. INSERT additional 4 rows with arbitrary data.
```sql
-- 插入一筆資料到 member 資料表，其中 name、username 和 password 都設置為 'test'
INSERT INTO member (name, username, password)
    -> VALUES ('test', 'test', 'test');
-- 插入另外四筆資料到 member 資料表，其中包含任意的資料
INSERT INTO member (name, username, password, follower_count)
    -> VALUES
    -> ('Henry', 'henry1107', '123456', 999),
    -> ('Cundi', 'cundi520', '654321', 888),
    -> ('Tom', 'tom8787', '87654321', 666),
    -> ('Alex', 'alex3838', 'password', 100);
```
<img width="550" alt="tesk3 1-1" src="https://github.com/user-attachments/assets/06e13ccf-d9a5-43b8-9dac-911921e0ce3c" />
<img width="707" alt="task3 1" src="https://github.com/user-attachments/assets/018a0514-4553-44b6-847f-a162de4f5bf6" />


* SELECT all rows from the member table.
```sql
-- 查詢 member 資料表中的所有資料
SELECT * FROM member;
```
<img width="715" alt="member" src="https://github.com/user-attachments/assets/57888cf9-4707-48ea-ba68-87bf68034aca" />

* SELECT all rows from the member table, in descending order of time.
```sql
-- 按照 time 欄位的降序排序，查詢 member 資料表中的所有資料
SELECT * FROM member ORDER BY time DESC;
```
<img width="715" alt="timeDESC" src="https://github.com/user-attachments/assets/eeca2996-71b8-4d3c-bd40-d5f5c9b2f1d6" />

* SELECT total 3 rows, second to fourth, from the member table, in descending order
of time. Note: it does not mean SELECT rows where id are 2, 3, or 4.
```sql
-- 按照 time 欄位的降序排序，查詢 member 資料表中的 第 2 到 第 4 行 資料
SELECT * FROM member ORDER BY time LIMIT 3 OFFSET 1;
```
<img width="711" alt="Limit" src="https://github.com/user-attachments/assets/869909ba-1db1-4a03-a001-0ed557db42f6" />

* SELECT rows where username equals to test.
```sql
-- 查詢 member 資料表中 username 等於 'test' 的所有資料
SELECT * FROM member WHERE username = 'test';
```
<img width="721" alt="user-test" src="https://github.com/user-attachments/assets/9e1bfb43-ab38-4db7-b14f-c01c0a4200a0" />

* SELECT rows where name includes the es keyword.
```sql
-- 查詢 member 資料表中 name 包含 'es' 關鍵字的所有資料
SELECT * FROM member WHERE name LIKE '%es%';
```
<img width="719" alt="name-es" src="https://github.com/user-attachments/assets/de2f3f4c-3ccb-41df-b857-f967b70f5b7a" />

* SELECT rows where both username and password equal to test.
```sql
-- 查詢 member 資料表中 username 和 password 都等於 'test' 的所有資料
SELECT * FROM member WHERE username = 'test' AND password = 'test';
```
<img width="714" alt="usernameANDpassword" src="https://github.com/user-attachments/assets/0fcc874f-78cf-4327-a290-0583e06255da" />

* UPDATE data in name column to test2 where username equals to test.
```sql
-- 更新 member 資料表中 username 等於 'test' 的 name 欄位為 'test2'
UPDATE member SET name = 'test2' WHERE username = 'test';
```
<img width="716" alt="updatename" src="https://github.com/user-attachments/assets/aa09532d-d2d2-4c24-a65f-42f6da4a7aea" />

___

# Task 4
**SQL Aggregation Functions (聚合函數)**
* SELECT how many rows from the member table.
```sql
-- 查詢 member 資料表中的總行數
SELECT COUNT(*) AS total_rows FROM member;
```
<img width="694" alt="countRows" src="https://github.com/user-attachments/assets/1d649964-a461-4d60-93f7-cd13b70d1e73" />

* SELECT the sum of follower＿count of all the rows from the member table.
```sql
-- 查詢 member 資料表中 follower_count 欄位的總和
SELECT SUM(follower_count) AS total_followers FROM member;
```
<img width="715" alt="sumfollower" src="https://github.com/user-attachments/assets/161e2898-940a-4e55-bb1f-16506e7ab2a5" />

* SELECT the average of follower＿count of all the rows from the member table.
```sql
-- 查詢 member 資料表中 follower_count 欄位的平均值
SELECT AVG(followers_count) AS average_followers FROM member;
```
<img width="716" alt="avgfollowers" src="https://github.com/user-attachments/assets/7c4ee710-b14f-4791-a8f7-d5ea4ac0dea0" />

* SELECT the average of follower＿count of the first 2 rows, in descending order of follower_count, from the member table.
```sql
-- 查詢 member 資料表中 follower_count 欄位的前兩行數據的平均值（按 follower_count 欄位降序排列）
SELECT AVG(followers_count) AS average_top2_followers
FROM (
SELECT follower_count
FROM member
ORDER BY follower_count DESC
LIMIT 2
) AS top2;
```
<img width="608" alt="avgfollowerslimit" src="https://github.com/user-attachments/assets/560efd5b-8f13-4670-b010-6d7502a0d6ed" />

___

# Task 5
**SQL JOIN(合併查詢）**
* Create a new table named message, in the website database. designed as below:
```sql
-- 創建 message 資料表，包含欄位：id、member_id、content、like_count 和 time，
-- 並設置 member_id 為 FOREIGN KEY (外鍵)，引用 member 資料表的 id 欄位
CREATE TABLE message(
id BIGINT AUTO_INCREMENT PRIMARY KEY,
member_id BIGINT NOT NULL,
content VARCHAR(255) NOT NULL,
like_count INT UNSIGNED NOT NULL DEFAULT 0,
time DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
FOREIGN KEY (member_id) REFERENCES member(id)
);
```
<img width="718" alt="messagetable" src="https://github.com/user-attachments/assets/b6fa5c49-bb8e-4e03-9f85-1abb0a2b6377" />

* INSERT Sample data
```sql
-- 插入 範例資料 到 message 資料表，member_id 由子查詢獲取對應的 member 資料表中的 id
INSERT INTO message (member_id, content, like_count)
VALUES
((SELECT id FROM member WHERE username = 'henry1107'), 'Hello from Henry!', 10),
((SELECT id FROM member WHERE username = 'cundi520'), 'Hello from Cundi!', 20),
((SELECT id FROM member WHERE username = 'tom8787'), 'Hello from Tom!', 30),
((SELECT id FROM member WHERE username = 'alex3838'), 'Hello from Alex!', 5),
((SELECT id FROM member WHERE username = 'test'), 'Hello from Test!', 15);
```
<img width="718" alt="insertsampledata" src="https://github.com/user-attachments/assets/cf301b09-dbb9-4809-b83a-5a9ca6dfbfd6" />


* SELECT all messages, including sender names. We have to JOIN the member table to get that.
```sql
-- 查詢所有訊息，包括發送者的名字，使用 JOIN 將 message 資料表與 member 資料表進行連接
SELECT message.*, member.name AS sender_name
FROM message
JOIN member ON message.member_id = member.id;
```
<img width="720" alt="join" src="https://github.com/user-attachments/assets/b356b619-4bf6-4e64-be81-9566cd8fe64a" />


* SELECT all messages, including sender names, where sender username equals to test. We have to JOIN the member table to filter and get that.
```sql
-- 查詢所有訊息，包括發送者的名字，並選擇發送者的 username 等於 'test' 的資料，使用 JOIN 將 message 資料表與 member 資料表進行連接
SELECT message.*, member.name AS sender_name
FROM message
JOIN member ON message.member_id = member.id
WHERE member.username = 'test';
```
<img width="721" alt="joinwhere" src="https://github.com/user-attachments/assets/7e7e8ac2-a4a7-4383-82d2-e18542272dd9" />


* Use SELECT, SQL Aggregation Functions with JOIN statement, get the average like count of messages where sender username equals to test.
```sql
-- 查詢發送者 username 等於 'test' 的資料的 平均 like_count，使用 JOIN 將 message 資料表與 member 資料表進行連接
SELECT AVG(message.like_count) AS average_like_count
FROM message
JOIN member ON message.member_id = member.id
WHERE member.username = 'test';
```
<img width="715" alt="avgjoin" src="https://github.com/user-attachments/assets/098358c3-51d6-45eb-bc7f-69f492ba2780" />

* Use SELECT, SQL Aggregation Functions with JOIN statement, get the average like count of messages GROUP BY sender username.
```sql
-- 查詢資料的平均 like_count，按照發送者 username 分群，使用 JOIN 將 message 資料表與 member 資料表進行連接
SELECT member.username, AVG(message.like_count) AS average_like_count
FROM message
JOIN member ON message.member_id = member.id
GROUP BY member.username;
```
<img width="719" alt="avggroupby" src="https://github.com/user-attachments/assets/2a2d25dd-5ff0-4d24-ba43-c4509a8f4a49" />

