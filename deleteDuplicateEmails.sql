DELETE c1 FROM Person c1  
INNER JOIN Person c2   
WHERE  
    c1.Id > c2.Id AND  
    c1.Email = c2.Email; 
