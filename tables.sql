create table account(
    `id` int NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `username` varchar(50) NOT NULL UNIQUE,
    `email` varchar(100) NOT NULL,
    `password` varchar(50) NOT NULL,
    `token` varchar(200)
);

create table captcha(
    `email` varchar(100) NOT NULL PRIMARY KEY,
    `captcha` varchar(50) NOT NULL,
    `expire` timestamp
);

create table profile(
    `username` varchar(50) NOT NULL PRIMARY KEY,
    `nickname` varchar(50),
    `avatar` varchar(200)
);

create table material(
    `id` varchar(50) NOT NULL PRIMARY KEY,
    `type` int NOT NULL,
    `owner` varchar(50) NOT NULL,
    `visibility` int NOT NULL,
    `quality` int NOT NULL,
    `title` varchar(100),
    `filepath` varchar(200)
);

create table shelf(
    `id` varchar(50) NOT NULL PRIMARY KEY,
    `user` varchar(50) NOT NULL,
    `mid` varchar(50) NOT NULL,
    INDEX(user)
);