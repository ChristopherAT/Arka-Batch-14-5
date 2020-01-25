SELECT tcash.name as cashier, tprod.name as product, tcate.name as category, price FROM product as tprod
JOIN cashier as tcash ON tcash.id = tprod.id_cashier
JOIN category AS tcate ON tcate.id = tprod.id_category;