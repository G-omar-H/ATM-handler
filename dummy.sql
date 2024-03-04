-- Insert data into Region table
INSERT INTO Region (regionId, regionName)
VALUES (1, 'East Coast'), (2, 'West Coast'), (3, 'Midwest');

-- Insert data into Branch table
INSERT INTO Branch (branchId, branchName, regionId)
VALUES (1, 'Main Branch', 1), (2, 'Downtown Branch', 1), (3, 'West Coast Headquarters', 2), (4, 'Chicago Office', 3), (5, 'University Branch', 2);

-- Insert data into Device table
INSERT INTO Device (deviceId, deviceName)
VALUES (1, 'ATM Controller'), (2, 'Cash Dispenser'), (3, 'Card Reader'), (4, 'Receipt Printer'), (5, 'Cash Deposit Module'), (6, 'Envelope Deposit Module'), (7, 'Touchscreen Display'), (8, 'Cash Cassette'), (9, 'Security Camera');

-- Insert data into AtmDevices table
INSERT INTO AtmDevice (atmId, deviceId, deviceStatus)
VALUES (1, 1, 'Operational'), (1, 2, 'Operational'), (1, 3, 'Operational'),
       (2, 1, 'Operational'), (2, 2, 'Operational'), (2, 3, 'Operational'),
       (3, 1, 'Operational'), (3, 2, 'Operational'), (3, 3, 'Operational'),
       (4, 1, 'Operational'), (4, 2, 'Operational'), (4, 3, 'Operational');

-- Insert data into ElectronicJournals table
INSERT INTO ElectronicJournal (ejId, ejData, atmId)
VALUES (1, 'Cash withdrawal completed successfully for user John Smith (USR-12345). Account: 123456, Amount: $40. Available balance: $440. Transaction time: 2024-03-05 10:15:00 AM. Card used: Debit card ending in XXXX-1234.', 1),
       (2, 'Deposit of $100 made for user Jane Doe (USR-54321) using cash. Account: 987654, New balance: $720. Transaction time: 2024-03-04 04:30:00 PM. Teller ID: 1001.', 2),
       (3, 'Balance inquiry for user Michael Brown (USR-98765). Account: 876543, Available balance: $1250. Transaction time: 2024-03-04 02:00:00 PM. Card used: Credit card ending in XXXX-5678.', 3),
       (4, 'PIN change successful for user David Lee (USR-24680). Transaction time: 2024-03-05 12:30:00 PM. Card used: Debit card ending in XXXX-9012.', 4),
       (5, 'Transfer of $200 initiated from account 123456 (John Smith) to account 789012 (Sarah Jones). Transaction time: 2024-03-04 08:00:00 AM. Confirmation required.', 1),
       (6, 'Failed login attempt for user (USR-99999). Incorrect PIN entered. Transaction time: 2024-03-05 03:15:00 AM. Card used: Debit card ending in XXXX-3456.', 2),
       (7, 'Card dispensed for user Michael Brown (USR-98765). Account: 876543. Transaction time: 2024-03-04 09:00:00 AM. Card used: Debit card ending in XXXX-5678.', 3),
       (8, 'Cash dispenser malfunction detected. Transaction aborted. Transaction time: 2024-03-05 01:00:00 PM. ATM: Corner Store ATM (123 Main St.).', 4);

-- Insert data into Event table
INSERT INTO Event (eventId, eventType, ejId)
VALUES (1, 'Cash Withdrawal', 1),
       (2, 'Balance Inquiry', 2),
       (3, 'Deposit', 3),
       (4, 'PIN Change', 4),
       (5, 'Transfer Initiation', 5),
       (6, 'Failed Login', 6),
       (7, 'Card Dispense', 7),
       (8, 'Dispenser Malfunction', 8);

-- Insert data into Groups table
INSERT INTO Group (groupId, groupName, groupDescription, groupType, regionId)
VALUES (1, 'Main Branch ATMs', 'ATMs located within the main branch building. These ATMs cater to a high volume of transactions and offer extended operating hours.', 'Branch', 1),
       (2, 'Downtown Branch ATMs', 'ATMs located in the downtown branch, serving a primarily business clientele. These ATMs offer enhanced security features.', 'Branch', 1),
       (3, 'East City Branch ATMs', 'ATMs located in the East City branch, serving a diverse residential and commercial community.', 'Branch', 2),
       (4, 'Convenience Store ATMs', 'ATMs located in partner convenience stores across the city, providing 24/7 access for customers on the go.', 'Off-site', 1),
       (5, 'University Campus ATMs', 'ATMs located on university campuses, serving students and staff. These ATMs offer features like bill payment and mobile top-up.', 'Off-site', 2);

-- Insert data into Transaction table
INSERT INTO Transaction (transactionId, transactionType, transactionDetail, ejId)
VALUES (1, 'Withdrawal', 'Withdrawal of $200 from account 123456 at ATM XYZ (Branch: Main Branch, Group: Main Branch ATMs)', 1),
       (2, 'Balance Inquiry', 'Balance inquiry for account 54321 at ATM ABC (Branch: Downtown Branch, Group: Off-site ATMs)', 2),
       (3, 'Deposit', 'Deposit of $500 to account 987654 using envelope at ATM DEF (Branch: West Coast Headquarters, Group: Convenience Store ATMs)', 3),
       (4, 'Transfer', 'Transfer of $100 from account 123456 to account 54321 at ATM GHI (Branch: Chicago Office, Group: University Campus ATMs)', 4),
       (5, 'Card Payment', 'Card payment of $25.99 for merchant ABC at ATM JKL (Branch: Main Branch, Group: Main Branch ATMs)', 5);

-- Insert data into ATM table (assuming atmName is not used)
INSERT INTO ATM (atmId, networkAddress, latitude, longitude, timezone, subnet, branchId, groupId)
VALUES (1, '192.168.1.101', 33.7550, -84.3900, 'EST', '255.255.255.0', 1, 1),
       (2, '192.168.1.102', 33.7625, -84.3881, 'EST', '255.255.255.0', 2, 2),
       (3, '192.168.2.101', 37.7749, -122.4194, 'PST', '255.255.255.0', 3, 3),
       (4, '192.168.3.101', 41.8819, -87.6231, 'CST', '255.255.255.0', 4, 4);