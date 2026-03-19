
CREATE TABLE Gemeente
(
  gemeente_ID   INT         NOT NULL AUTO_INCREMENT,
  gemeente_naam VARCHAR(50) NOT NULL,
  postcode      VARCHAR(15) NOT NULL,
  land_Code     VARCHAR(3)  NOT NULL,
  PRIMARY KEY (gemeente_ID)
);

CREATE TABLE Klant
(
  klant_ID      INT         NOT NULL AUTO_INCREMENT,
  klant_Vnaam   VARCHAR(30) NOT NULL,
  klant_Naam    VARCHAR(60) NOT NULL,
  telefoon      VARCHAR(20) NULL    ,
  geboorteDatum DATE        NOT NULL,
  email         VARCHAR(50) NOT NULL,
  gemeente_ID   INT         NOT NULL,
  PRIMARY KEY (klant_ID)
);

CREATE TABLE Ploeg
(
  ploeg_ID    INT         NOT NULL AUTO_INCREMENT,
  ploeg_Naam  VARCHAR(30) NOT NULL,
  gemeente_ID INT         NOT NULL,
  stadion_ID  INT         NOT NULL,
  PRIMARY KEY (ploeg_ID)
);

CREATE TABLE Stadion
(
  stadion_ID    INT         NOT NULL AUTO_INCREMENT,
  stadion_Naam  VARCHAR(30) NOT NULL,
  aantal_zetels INT         NOT NULL,
  PRIMARY KEY (stadion_ID)
);

CREATE TABLE Ticket
(
  ticket_ID INT   NOT NULL AUTO_INCREMENT,
  prijs     FLOAT NOT NULL,
  klant_ID  INT   NOT NULL,
  match_ID  INT   NOT NULL,
  PRIMARY KEY (ticket_ID)
);

CREATE TABLE Wedstrijd
(
  wedstrd_ID     INT      NOT NULL AUTO_INCREMENT,
  beginUur       DATETIME NOT NULL,
  eindUur        DATETIME NOT NULL,
  thuis          INT      NOT NULL,
  bezoekers      INT      NOT NULL,
  stadion_ID     INT      NOT NULL,
  score_Thuis    INT      NULL    ,
  score_Bezoeker INT      NULL    ,
  PRIMARY KEY (wedstrd_ID)
);

ALTER TABLE Klant
  ADD CONSTRAINT FK_Gemeente_TO_Klant
    FOREIGN KEY (gemeente_ID)
    REFERENCES Gemeente (gemeente_ID);

ALTER TABLE Ticket
  ADD CONSTRAINT FK_Klant_TO_Ticket
    FOREIGN KEY (klant_ID)
    REFERENCES Klant (klant_ID);

ALTER TABLE Ploeg
  ADD CONSTRAINT FK_Gemeente_TO_Ploeg
    FOREIGN KEY (gemeente_ID)
    REFERENCES Gemeente (gemeente_ID);

ALTER TABLE Ploeg
  ADD CONSTRAINT FK_Stadion_TO_Ploeg
    FOREIGN KEY (stadion_ID)
    REFERENCES Stadion (stadion_ID);

ALTER TABLE Wedstrijd
  ADD CONSTRAINT FK_Ploeg_TO_Wedstrijd
    FOREIGN KEY (thuis)
    REFERENCES Ploeg (ploeg_ID);

ALTER TABLE Wedstrijd
  ADD CONSTRAINT FK_Ploeg_TO_Wedstrijd1
    FOREIGN KEY (bezoekers)
    REFERENCES Ploeg (ploeg_ID);

ALTER TABLE Wedstrijd
  ADD CONSTRAINT FK_Stadion_TO_Wedstrijd
    FOREIGN KEY (stadion_ID)
    REFERENCES Stadion (stadion_ID);

ALTER TABLE Ticket
  ADD CONSTRAINT FK_Wedstrijd_TO_Ticket
    FOREIGN KEY (match_ID)
    REFERENCES Wedstrijd (wedstrd_ID);
