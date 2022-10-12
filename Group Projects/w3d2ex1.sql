SELECT NomeCantante from CANTANTE join ESECUZIONE on CodiceReg where NomeCantante LIKE 'D%';
SELECT TitoloAlbum from DISCO,ESECUZIONE join on DISCO.ANNO=ESECUZIONE.ANNO where Anno is NULL;




SELECT NomeCantante 
FROM CANTANTE JOIN ESECUZIONE ON                              
CANTANTE.CodiceReg=ESECUZIONE.CodiceReg                      
JOIN AUTORE ON ESECUZIONE.TitoloCanz=AUTORE.TitoloCanz     
WHERE Nome=NomeCantante AND Nome LIKE 'D%'; 


select TitoloAlbum from DISCO,ESECUZIONE on DISCO.ANNO=ESECUZIONE.ANNO where Anno is null;


SELECT TitoloAlbum
FROM DISCO JOIN CONTIENE ON
        DISCO.NroSerie = CONTIENE.NroSerieDisco
        JOIN ESECUZIONE ON CONTIENE.CodiceReg = ESECUZIONE.CodiceReg
WHERE ESECUZIONE.Anno IS NULL;

SELECT NomeCantante
FROM CANTANTE
WHERE NomeCantante NOT IN
                     (SELECT C1.NomeCantante
                      FROM CANTANTE AS C1
                      WHERE CodiceReg NOT IN
                                        (SELECT CodiceReg
                                         FROM CANTANTE AS C2)
                       WHERE C2.NomeCantante <> C1.NomeCantante);


SELECT NomeCantante
FROM CANTANTE
WHERE NomeCantante NOT IN
                     (SELECT C1.NomeCantante
                      FROM CANTANTE AS C1 JOIN ESECUZIONE ON
                      ESECUZIONE.CodiceReg = C1.CodiceReg
                      JOIN CANTANTE AS C2 ON
                           ESECUZIONE.CodiceReg = C2.CodiceReg)
                      WHERE C1.NomeCantante <> C2.NomeCantante);
