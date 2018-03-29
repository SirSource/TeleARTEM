
create table Users(userID serial primary key, name varchar(20), email varchar(30), username varchar(20), password varchar(20), phone varchar(20));

create table Chats(chatID serial primary key, admin integer references Users(userID), name varchar(20));

create table Messages(messageID serial primary key, poster integer references Users(userID), chat integer references Chats(chatID), message varchar(120), timeStamp date, replyID integer references Messages(messageID));

create table Likes(likeID serial primary key, likeValue integer, message integer references Messages(messageID), userID integer references Users(userID));

create table Contacts(contactID serial primary key, holder integer references Users(userID), friend integer references Users(userID));

create table Members(memberID serial primary key, chat integer references Chats(chatID), userID integer references Users(userID));