USE csci375team6_povCal;
delete from users;

INSERT INTO users (firstName, lastName) VALUES 
('john_doe', 'john@example.com'),
('jane_smith', 'jane@example.com');



INSERT INTO income (id, ownerId, amount, incomeType)  
VALUES (1, 1, 65000, 'Salary'), 
(2, 2, 2000, 'Business Revenue');


INSERT INTO assets(id, ownerId, assetType, assetValue, purchaseDate) VALUES 
(1,1 ,'House', '21000', '2013-01-01'),
(2,1 ,'Food Truck', '5000', '2013-01-01'),
(3,2 ,'Real Estate', '4500', '2013-01-01'),
(4,2 ,'Real Estate', '4600', '2013-01-01')

;



INSERT INTO liabilities(id, ownerId, liabilityType, amountOwed) VALUES
(1,1, 'credit card', 1200),
(2,2, 'Parking tickets', 140);
