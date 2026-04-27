CREATE TABLE supplier (
    SNO TEXT PRIMARY , 
    SNAME TEXT , 
    STATUS INTEGER , 
    CIY TEXT , 
) ;
INSERT INTO supplier (SNO, SNAME , STATUS , CITY) VALUES 

( 's1' , 'smith' ,'20', 'london') , 
('s2' , 'jones' , '10' , 'paris') , 
( 's3' , 'blake' , '30' , 'paris') ,
('s4', 'clarke' , '20' , 'london') , 
('s5' , 'adamns' , '30' , 'athens') ;

SELECT * FROM supplier;


