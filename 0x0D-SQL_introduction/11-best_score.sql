-- lists all the records with a score >= 10 in second table of database
SELECT `score`, `name`
FROM second_table
WHERE `score` >= 10
ORDER BY `score` DESC;
