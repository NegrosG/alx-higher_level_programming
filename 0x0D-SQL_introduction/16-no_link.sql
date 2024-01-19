-- Script should list all the records of the second_table
-- Don't list rows without name value and record should be descending order
SELECT `score`, `name`
FROM `second_table`
WHERE `name` != ""
ORDER BY `score` DESC;
