select*from ticket

INSERT into ticket(`ticket_ID`,`prijs`,`klant_ID`,`match_ID`)VALUES(3,30,2,2)

UPDATE ticket set `ticket_ID`=1,`prijs`=50,`klant_ID`=1, `match_ID`=1 WHERE `ticket_ID`=1

INSERT into ticket(`ticket_ID`,`prijs`, `klant_ID`,`match_ID`)VALUES(1,50,1,1)

DELETE from ticket WHERE `ticket_ID`=1

select*from stadion

select*from ploeg

SELECT stadion.stadion_ID,stadion.stadion_Naam,stadion.aantal_Zetels,stadion.stadion_Img,ploeg.logo_Img FROM stadion INNER JOIN ploeg ON stadion.stadion_ID = ploeg.stadion_ID;