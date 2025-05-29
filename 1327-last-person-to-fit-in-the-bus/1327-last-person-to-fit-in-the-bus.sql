# Write your MySQL query statement below
WITH cte AS(                    #Ctreated a temporary table to calculate the total weight 
    SELECT person_name, turn, SUM(weight) OVER (ORDER BY turn) AS running_wt
    FROM Queue
)
SELECT person_name
FROM cte
WHERE running_wt <= 1000        #Board people only within weight limit
ORDER BY turn DESC              #To sort using turn on the table
LIMIT 1;                        #Last person                            

