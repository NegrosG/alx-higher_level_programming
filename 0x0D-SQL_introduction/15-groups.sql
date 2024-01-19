-- List the number of record of the same value in second_table
SELECT `score`, COUNT(*) as number
FROM `second_table`
GROUP BY `score`;
