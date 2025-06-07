-- Step 1: Rank each employee's salary within their department
WITH RankedSalaries AS (
    SELECT 
        e.id,
        e.name,
        e.salary,
        e.departmentId,
        -- Assign rank by salary per department (highest gets rank 1)
        DENSE_RANK() OVER (PARTITION BY departmentId ORDER BY salary DESC) AS salary_rank
    FROM Employee e
)

-- Step 2: Select employees with top 3 unique salaries per department
SELECT 
    d.name AS Department,      -- Department name
    r.name AS Employee,        -- Employee name
    r.salary AS Salary         -- Salary
FROM RankedSalaries r
JOIN Department d ON r.departmentId = d.id  -- Join to get department name
WHERE r.salary_rank <= 3                    -- Keep only top 3 salaries per department
ORDER BY d.name, r.salary DESC;            -- Sort by department and salary (highest first)
