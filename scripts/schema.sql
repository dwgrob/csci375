USE csci375team6_povCal;

create table if not exists users (
    id int PRIMARY KEY AUTO_INCREMENT,
    firstName varchar(20),
    lastName varchar(20),
    contactInfo varchar(20)
);



create table if not exists advisors (
    id int PRIMARY KEY AUTO_INCREMENT,
    firstName varchar(20),
    lastName varchar(20),
    contactInfo varchar(20),
    authId varchar(20)
);



-- salary, full_time, part_time, rent, capital, other
create table if not exists income (
    id int PRIMARY KEY AUTO_INCREMENT,
    ownerId INT,
    amount int,
    incomeType varchar(20),
    FOREIGN KEY (ownerId) REFERENCES users(id) on DELETE cascade
    

);


-- property, vehicle, cash, investment, art, 
create table if not exists assets (
    id int PRIMARY KEY AUTO_INCREMENT,
    ownerId int,
    assetType varchar(50),
    assetValue int,
    purchaseDate DATE,
    FOREIGN KEY (ownerId) REFERENCES users(id) on DELETE cascade
);

create table if not exists liabilities (
    id int PRIMARY KEY AUTO_INCREMENT,
    ownerId int,
    liabilityType varchar(50),
    amountOwed int
);


create table if not exists blogs (
    blogId int PRIMARY KEY AUTO_INCREMENT,
    authorId INT,
    title varchar(100),
    tag varchar(100),
    FOREIGN KEY (authorId) REFERENCES users(id) ON DELETE CASCADE,
    text varchar(1000) 
);


create table if not exists  comments (
    commentId int PRIMARY KEY AUTO_INCREMENT,
    blogId int,
    FOREIGN KEY (blogId) REFERENCES blogs(blogId) ON DELETE CASCADE,
    authorId int,
    FOREIGN KEY (authorId) REFERENCES advisors(id) ON DELETE CASCADE, 
    text varchar(500)
)


