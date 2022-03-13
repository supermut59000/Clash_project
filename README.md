# Clash_project

A project to track u and your friend on Clash Royal.





# Commande

## Table size

SELECT table_name AS "Table", ROUND(((data_length + index_length) / 1024), 2) AS "Size (kB)" FROM information_schema.TABLES WHERE table_schema = 'database_1' ORDER BY (data_length + index_length) DESC;

