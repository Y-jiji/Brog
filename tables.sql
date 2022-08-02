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