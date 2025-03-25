USE csci375team6_povertycalculator;

create table if not exists users (
    id int PRIMARY KEY AUTO_INCREMENT,
    firstName varchar(20),
    lastName varchar(20),
    contactInfo varchar(20),
    type varchar(10)
);

create table if not exists income (
    id int PRIMARY KEY AUTO_INCREMENT,
    ownerId INT,
    income int ,
    salary int,
    rentalIncome int,
    businessIncome int,
    investments int,
    otherSources int,
    liabilities int,
    obligations int,
    FOREIGN KEY (ownerId) REFERENCES users(id) on DELETE cascade
);

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
    amountOwed DECIMAL(12,6),
    apr DECIMAL(2,2)
   
);


create table if not exists blogs (
    id int PRIMARY KEY AUTO_INCREMENT,
    authorId INT,
    FOREIGN KEY (authorId) REFERENCES users(id) ON DELETE CASCADE,
    text varchar(1000) 
);


