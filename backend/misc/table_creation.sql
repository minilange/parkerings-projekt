
IF (OBJECT_ID('dbo.Admins', 'U') IS NOT NULL)
BEGIN
	DROP TABLE dbo.Admins;
	PRINT('DROPPED Admins')
END

IF (OBJECT_ID('dbo.UserLicenseplates', 'U') IS NOT NULL)
BEGIN
	DROP TABLE dbo.UserLicenseplates;
	PRINT('DROPPED UserLicenseplates')
END

IF (OBJECT_ID('dbo.Parkings','U') IS NOT NULL)
BEGIN
	DROP TABLE dbo.Parkings;
	PRINT('DROPPED Parkings')
END

IF (OBJECT_ID('dbo.RegisteredLicenseplates', 'U') IS NOT NULL) 
BEGIN
	DROP TABLE dbo.RegisteredLicenseplates;
	PRINT('DROPPED RegisteredLicenseplates')
END

IF (OBJECT_ID('dbo.Users', 'U') IS NOT NULL)  
BEGIN
	DROP TABLE dbo.Users;
	PRINT('DROPPED Users')
END

IF (OBJECT_ID('dbo.Areas', 'U') IS NOT NULL)
BEGIN
	DROP TABLE dbo.Areas;
	PRINT('DROPPED Areas')
END
	   
PRINT('')
PRINT('------------------')
PRINT('')


CREATE TABLE Areas (
	[areaId] INT IDENTITY(1,1) PRIMARY KEY,
	[areaName] NVARCHAR(255),
	[address] NVARCHAR(255),
	[latitude] FLOAT,
	[longitude] FLOAT
)
PRINT('Initiated Areas')

CREATE TABLE RegisteredLicenseplates (
	[licenseplate] NVARCHAR(7) PRIMARY KEY,
	[brand] NVARCHAR(255),
	[model] NVARCHAR(255),
	[type] NVARCHAR(100)
)
PRINT('Initiated RegisteredLicenseplates')

CREATE TABLE Users (
	[userId] INT IDENTITY(1,1) PRIMARY KEY,
	[firstname] NVARCHAR(255),
	[lastname] NVARCHAR(255),
	[email] NVARCHAR(255) UNIQUE,
	[password] NVARCHAR(255),
	[phone] NVARCHAR(15),
	[ccCode] NVARCHAR(5)
)
PRINT('Initiated Users')

CREATE TABLE Parkings (
	[parkingId] INT IDENTITY(1,1) PRIMARY KEY,
	[licenseplate] NVARCHAR(7),
	[userId] INT,
	[areaId] INT,
	[minutes] INT,
	[price] INT,
	[state] NVARCHAR(50),
	[timestamp] DATETIME2,
	FOREIGN KEY (licenseplate) REFERENCES dbo.RegisteredLicenseplates(licenseplate),
	FOREIGN KEY (userId) REFERENCES dbo.Users(userId),
	FOREIGN KEY (areaId) REFERENCES dbo.Areas(areaId)
)
PRINT('Initiated Parkings')

CREATE TABLE UserLicenseplates (
	[userId] INT,
	[licenseplate] NVARCHAR(7),
	FOREIGN KEY (userId) REFERENCES Users(userId),
	FOREIGN KEY (licenseplate) REFERENCES RegisteredLicenseplates(licenseplate)
)
PRINT('Initiated UserLicenseplates')

CREATE TABLE Admins (
	userId INT,
	[level] INT
	FOREIGN KEY (userId) REFERENCES dbo.Users(userId)
)
PRINT('Initiated Admins')
