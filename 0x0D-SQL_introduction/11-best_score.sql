-- script that lists best records of the table second_table of the database

SELECT score, name
FROM second_table
WHERE score >= 10
ORDER By score DESC;
