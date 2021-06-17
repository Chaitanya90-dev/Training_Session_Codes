Create table LMS_MEMBERS

(

MEMBER_ID Varchar(10),

MEMBER_NAME Varchar(30) NOT NULL,

CITY Varchar(20),

DATE_REGISTER Date NOT NULL,

DATE_EXPIRE Date ,

MEMBERSHIP_STATUS Varchar(15)NOT NULL,

Constraint LMS_cts1 PRIMARY KEY(MEMBER_ID)

);



Insert into LMS_MEMBERS

Values('LM001', 'ADESH', 'NASHIK', '2020-02-12', '2021-02-11','Temporary');


Insert into LMS_MEMBERS

Values('LM002', 'RUSHIKESH', 'NASHIK', '2020-04-10', '2021-04-09','Temporary');


Insert into LMS_MEMBERS

Values('LM003', 'RAHUL', 'NAGPUR', '2020-05-13','2021-05-12', 'Permanent');


Insert into LMS_MEMBERS

Values('LM004', 'SWANAND', 'PUNE', '2020-04-22', '2021-04-21', 'Temporary');


Insert into LMS_MEMBERS

Values('LM005', 'SANKET', 'PUNE', '2020-03-30', '2021-05-16','Temporary');

Insert into LMS_MEMBERS

 
Values('LM006', 'HITANSHU', 'NAGPUR', '2020-04-12', '2021-05-16','Temporary');


select * from lms_members;





Create table LMS_SUPPLIERS_DETAILS

(

SUPPLIER_ID Varchar(3),

SUPPLIER_NAME Varchar(30) NOT NULL,

ADDRESS Varchar(50),

CONTACT bigint(10) NOT NULL,

EMAIL Varchar(15) NOT NULL,

Constraint LMS_cts2 PRIMARY KEY(SUPPLIER_ID)

);


Insert into LMS_SUPPLIERS_DETAILS 

Values ('S01','ABC STATIONARY', 'PUNE', 9894123555,'ABC@gmail.com');


Insert into LMS_SUPPLIERS_DETAILS 

Values ('S02','JK Stores', 'NASHIK', 9940123450 ,'jks@yahoo.com');

Insert into LMS_SUPPLIERS_DETAILS 

Values ('S03','RS AGARWAL BOOK STORE', 'MUMBAI', 9444411222,'rsag@gmail.com');

Insert into LMS_SUPPLIERS_DETAILS 

Values ('S04','PRAGATI BOOK STORE', 'DELHI', 8630001452,'pragati@redif.com');

Insert into LMS_SUPPLIERS_DETAILS 

Values ('S05','EINSTEN BOOK GALLARY', 'US', 9542000001,'eingal@aol.com');

Insert into LMS_SUPPLIERS_DETAILS 

Values ('S06','NAVNEET STORE', 'MUMBAI',7855623100 ,'navneet@aol.com');

select * from LMS_SUPPLIERS_DETAILS;





Create table LMS_BOOK_DETAILS

(

BOOK_CODE Varchar(10), 

BOOK_TITLE Varchar(50) NOT NULL,

CATEGORY Varchar(15) NOT NULL,

AUTHOR Varchar(30) NOT NULL,

PUBLICATION Varchar(30),

PUBLISH_DATE Date,

BOOK_EDITION int(2),

PRICE decimal(8,2) NOT NULL, 

RACK_NUM Varchar(3),

DATE_ARRIVAL Date NOT NULL,  

SUPPLIER_ID Varchar(3) NOT NULL,

Constraint LMS_cts4 PRIMARY KEY(BOOK_CODE), 

Constraint LMS_cts41 FOREIGN KEY(SUPPLIER_ID) References LMS_SUPPLIERS_DETAILS(SUPPLIER_ID)

);

Insert into LMS_BOOK_DETAILS

Values('BL000010', 'Java ForvDummies', 'JAVA', 'Paul J. Deitel', 'Prentice Hall', '1999-12-10', 6, 575.00, 'A1', '2011-05-10', 'S01');

Insert into LMS_BOOK_DETAILS

Values('BL000002', 'Java: The Complete Reference ', 'JAVA', 'Herbert Schildt', 'Tata Mcgraw Hill ', '2011-10-10', 5, 750.00, 'A1', '2011-05-10', 'S03');

Insert into LMS_BOOK_DETAILS 

Values('BL000003', 'Java How To Do Program', 'JAVA', 'Paul J. Deitel', 'Prentice Hall', '1999-05-10', 6, 600.00, 'A1', '2012-05-10', 'S01');

Insert into LMS_BOOK_DETAILS

Values('BL000004', 'Java: The Complete Reference ', 'JAVA', 'Herbert Schildt', 'Tata Mcgraw Hill ', '2011-10-10', 5, 750.00, 'A1', '2012-05-11', 'S01');

Insert into LMS_BOOK_DETAILS 

Values('BL000005', 'Java How To Do Program', 'JAVA', 'Paul J. Deitel', 'Prentice Hall', '1999-12-10', 6, 600.00, 'A1', '2012-05-11', 'S01');

Insert into LMS_BOOK_DETAILS

Values('BL000006', 'Java: The Complete Reference ', 'JAVA', 'Herbert Schildt', 'Tata Mcgraw Hill ', '2011-10-10', 5, 750.00, 'A1', '2012-05-12', 'S03');

Insert into LMS_BOOK_DETAILS 

Values('BL000007', 'Let Us C', 'C', 'Yashavant Kanetkar ', 'BPB Publications', '2010-12-11', 9, 500.00 , 'A3', '2010-11-03', 'S03');

Insert into LMS_BOOK_DETAILS 

Values('BL000008', 'Let Us C', 'C', 'Yashavant Kanetkar ','BPB Publications', '2010-05-12', 9, 500.00 , 'A3', '2011-08-09', 'S04');

Insert into LMS_BOOK_DETAILS 

Values('BL000009', 'Let Us C#', 'C', 'Yashavant Kanetkar ','BPB Publications', '2010-05-12', 9, 550.00 , 'A3', '2011-08-09', 'S04');

Insert into LMS_BOOK_DETAILS 

Values('BL000011', 'Let Us C++', 'C', 'Yashavant Kanetkar ','BPB Publications', '2010-05-12', 9, 650.00 , 'A3', '2011-08-09', 'S04');

select * from LMS_BOOK_DETAILS;





Create table LMS_BOOK_ISSUE

(

BOOK_ISSUE_NO int,

MEMBER_ID Varchar(10) NOT NULL,

BOOK_CODE Varchar(10) NOT NULL,

DATE_ISSUE Date NOT NULL,

DATE_RETURN Date NOT NULL,

DATE_RETURNED Date NULL,

Constraint LMS_cts5 PRIMARY KEY(BOOK_ISSUE_NO),

Constraint LMS_Mem FOREIGN KEY(MEMBER_ID) References LMS_MEMBERS(MEMBER_ID),

Constraint LMS_BookDetail FOREIGN KEY(BOOK_CODE) References LMS_BOOK_DETAILS(BOOK_CODE)
);


Insert into LMS_BOOK_ISSUE 

Values (001, 'LM001', 'BL000010', '2020-05-01', '2020-06-01', '2020-05-24');

Insert into LMS_BOOK_ISSUE 

Values (002, 'LM002', 'BL000002', '2020-05-01', '2020-06-15','2020-07-16');

Insert into LMS_BOOK_ISSUE

Values (003, 'LM003', 'BL000007', '2020.-04-01', '2020-05-16', '2020-05-20');

Insert into LMS_BOOK_ISSUE 

Values (004, 'LM004', 'BL000005', '2020-04-01', '2020-04-15','2012-05-10' );

Insert into LMS_BOOK_ISSUE 

Values (005, 'LM005', 'BL000008', '2020-03-30', '2020-04-29','2012-05-10' );

Insert into LMS_BOOK_ISSUE 

Values (006, 'LM005', 'BL000008', '2020-04-20', '2020-05-15','2020-08-15' );

Insert into LMS_BOOK_ISSUE 

Values (007, 'LM003', 'BL000007', '2020-04-22', '2020-05-28','2020-06-10');

select * from LMS_BOOK_ISSUE ;