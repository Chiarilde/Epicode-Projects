SELECT distinct Citta from AEROPORTO where NumPiste is NULL;
SELECT TipoAereo from VOLO where CittaPart = 'Torino';
SELECT CittaPart from VOLO where CittaArr = 'Bologna';
SELECT CittaArr, CittaPart from VOLO where IdVolo = 'AZ274';
SELECT TipoAereo, GiornoSett, OraPart from VOLO where CittaPart LIKE 'B%o%' and CittaArr LIKE '%e%a';
