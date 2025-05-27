# Write your MySQL query statement below
#SELECT DISTINCT L1.num AS  ConsecutiveNums 
#FROM Logs L1
#JOIN Logs L2 ON L1.id = L2.id -1
#JOIN Logs L3 ON L2.id = L3.id - 1
#WHERE L1.num = L2.num AND L2.num = L3.num;

SELECT DISTINCT i1.num AS ConsecutiveNums 
FROM logs i1, logs i2, logs i3
WHERE 
    i1.id = i2.id + 1 
    AND i2.id = i3.id + 1 
    AND i1.num = i2.num 
    AND i2.num = i3.num;