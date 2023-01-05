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
	Countrycode NVARCHAR(3) PRIMARY KEY,
	Phonecode INT,
	Name NVARCHAR(255)
)
PRINT('Initiated Countries')

CREATE TABLE Areas (
	AreaID INT IDENTITY(1,1) PRIMARY KEY,
	AreaName NVARCHAR(255),
	Address NVARCHAR(255),
	Latitude FLOAT,
	Longitude FLOAT
)
PRINT('Initiated Areas')

CREATE TABLE RegisteredLicenseplates (
	Licenseplates NVARCHAR(7) PRIMARY KEY,
	Brand NVARCHAR(255),
	Model NVARCHAR(255),
	Type NVARCHAR(100)
)
PRINT('Initiated RegisteredLicenseplates')

CREATE TABLE Users (
	UserId INT IDENTITY(1,1) PRIMARY KEY,
	Firstname NVARCHAR(255),
	Lastname NVARCHAR(255),
	Email NVARCHAR(255) UNIQUE,
	Password NVARCHAR(255),
	Phone NVARCHAR(15),
	Countrycode NVARCHAR(3),
	FOREIGN KEY (Countrycode) REFERENCES Countries(Countrycode)
)
PRINT('Initiated Users')

CREATE TABLE Parkings (
	ParkingId INT IDENTITY(1,1) PRIMARY KEY,
	Licenseplates NVARCHAR(7),
	UserId INT,
	AreaId INT,
	Minutes INT,
	Price INT,
	State NVARCHAR(50),
	Timestamp DATETIME2,
	FOREIGN KEY (Licenseplates) REFERENCES RegisteredLicenseplates(Licenseplates),
	FOREIGN KEY (UserId) REFERENCES Users(UserId),
	FOREIGN KEY (AreaId) REFERENCES Areas(AreaId)
)
PRINT('Initiated Parkings')

CREATE TABLE UserLicenseplates (
	UserId INT,
	Licenseplates NVARCHAR(7),
	FOREIGN KEY (UserId) REFERENCES Users(UserId),
	FOREIGN KEY (Licenseplates) REFERENCES RegisteredLicenseplates(Licenseplates)
)
PRINT('Initiated UserLicenseplates')

