CREATE TABLE user(
    user_id     BIGINT          NOT NULL AUTO_INCREMENT,
    email       VARCHAR(50)     UNIQUE NOT NULL,
    password    VARCHAR(100)    NOT NULL,
    role        VARCHAR(50)     NULL ,
    PRIMARY KEY (user_id)
);