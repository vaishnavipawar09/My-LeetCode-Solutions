# Write your MySQL query statement below
WITH cte AS(
    SELECT person_name, turn, SUM(weight) OVER (ORDER BY turn) AS running_wt
    FROM Queue
)
SELECT person_name
FROM cte
WHERE running_wt <= 1000
ORDER BY turn DESC 
LIMIT 1;                            #To sort using turn on the table

