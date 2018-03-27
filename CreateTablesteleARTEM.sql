create table Users(userID serial primary key,user_first_name varchar(20), user_last_name varchar(30),user_email varchar(30), user_phone varchar(15);

create table UserPassword(userPassID serial primary key, userID references Users(userID));

create table Ulike(uLikeID serial primary key, userID references Users(userID));

create table Contacts(contact_ID serial primary key, userID references Users(userID), contact_first varchar(20), contact_last varchar(20), contact_phone varchar(20), contact_email varchar(20));

create table message(m_id serial primary key, userID references Users(userID), m_thread integer, );

create table Conversation(conv_ID serial primary key, creatorID references Users(userID));

create table UsersInConversation(user_convID serial primary key, conv_ID references Conversation(conv_ID), userID varchar(20));



