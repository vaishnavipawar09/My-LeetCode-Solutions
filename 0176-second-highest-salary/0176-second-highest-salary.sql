# Write your MySQL query statement below
-- Select the second highest salary from the Employee table
SELECT 
    (
        -- Subquery to select the second highest distinct salary
        SELECT DISTINCT salary
        FROM Employee
        ORDER BY salary DESC  -- Sort salaries in descending order
        LIMIT 1 OFFSET 1      -- Skip the highest salary (OFFSET 1), take the next one
    ) AS SecondHighestSalary;
