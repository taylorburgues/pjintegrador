create table Amostras (
ID int auto_increment,
MP10 int(10) NOT NULL,
MP25 int(10) NOT NULL,
O3 int(10) NOT NULL,
CO int(10) NOT NULL,
NO2 int(10) NOT NULL,
SO2 int(10) NOT NULL,
primary key(ID)
) DEFAULT CHARSET=utf8;
drop table amostras;
select*from amostras;

SET @count = 0;
UPDATE `amostras` SET `id` = @count:= @count + 1;

insert into amostras values
(DEFAULT,1, 2, 3, 4, 5, 6),
(DEFAULT,2, 3, 4, 5, 6, 7),
(DEFAULT,2, 2, 6, 2, 8, 5),
(DEFAULT,3, 5, 7, 9, 5, 6),
(DEFAULT,6, 4, 2, 8, 0, 10);

select avg(MP10), avg(MP25), avg(O3), avg(CO), avg(NO2), avg(SO2) from amostras;