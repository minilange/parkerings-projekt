IF OBJECT_ID(N'dbo.UserLicenseplates', N'U') IS NOT NULL  
	DROP TABLE UserLicenseplates;
	PRINT('Dropped UserLicensePlates')

IF OBJECT_ID(N'dbo.Parkings', N'U') IS NOT NULL  
	DROP TABLE Parkings;
	PRINT('Dropped Parkings')

IF OBJECT_ID(N'dbo.Users', N'U') IS NOT NULL  
	DROP TABLE Users;
	PRINT('Dropped Users')

IF OBJECT_ID(N'dbo.RegisteredLicenseplates', N'U') IS NOT NULL  
	DROP TABLE RegisteredLicenseplates;
	PRINT('Dropped UserLicensePlates')

IF OBJECT_ID(N'dbo.Areas', N'U') IS NOT NULL  
	DROP TABLE Areas;
	PRINT('Dropped Areas')

IF OBJECT_ID(N'dbo.Countries', N'U') IS NOT NULL  
	DROP TABLE Countries;
	PRINT('Dropped Countries')


PRINT('')
PRINT('------------------')
PRINT('')


CREATE TABLE Countries (
	countrycode NVARCHAR(3) PRIMARY KEY,
	phonecode INT,
	name NVARCHAR(255)
)
PRINT('Initiated Countries')

CREATE TABLE Areas (
	areaId INT IDENTITY(1,1) PRIMARY KEY,
	areaName NVARCHAR(255),
	address NVARCHAR(255),
	latitude FLOAT,
	longitude FLOAT
)
PRINT('Initiated Areas')

CREATE TABLE RegisteredLicenseplates (
	licenseplates NVARCHAR(7) PRIMARY KEY,
	brand NVARCHAR(255),
	model NVARCHAR(255),
	type NVARCHAR(100)
)
PRINT('Initiated RegisteredLicenseplates')

CREATE TABLE Users (
	userId INT IDENTITY(1,1) PRIMARY KEY,
	firstname NVARCHAR(255),
	lastname NVARCHAR(255),
	email NVARCHAR(255) UNIQUE,
	password NVARCHAR(255),
	phone NVARCHAR(15),
	countrycode NVARCHAR(3),
	FOREIGN KEY (countrycode) REFERENCES Countries(countrycode)
)
PRINT('Initiated Users')

CREATE TABLE Parkings (
	parkingId INT IDENTITY(1,1) PRIMARY KEY,
	licenseplates NVARCHAR(7),
	userId INT,
	areaId INT,
	minutes INT,
	price INT,
	state NVARCHAR(50),
	timestamp DATETIME2,
	FOREIGN KEY (licenseplates) REFERENCES RegisteredLicenseplates(licenseplates),
	FOREIGN KEY (userId) REFERENCES Users(userId),
	FOREIGN KEY (areaId) REFERENCES Areas(areaId)
)
PRINT('Initiated Parkings')

CREATE TABLE UserLicenseplates (
	userId INT,
	licenseplates NVARCHAR(7),
	FOREIGN KEY (userId) REFERENCES Users(userId),
	FOREIGN KEY (licenseplates) REFERENCES RegisteredLicenseplates(licenseplates)
)
PRINT('Initiated UserLicenseplates')

