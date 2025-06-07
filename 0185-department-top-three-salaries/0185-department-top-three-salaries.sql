WITH RankedSalaries AS (
    SELECT 
        e.id,
        e.name,
        e.salary,
        e.departmentId,
        DENSE_RANK() OVER (PARTITION BY departmentId ORDER BY salary DESC) AS salary_rank
    FROM Employee e
)

SELECT 
    d.name AS Department,
    r.name AS Employee,
    r.salary AS Salary
FROM RankedSalaries r
JOIN Department d ON r.departmentId = d.id
WHERE r.salary_rank <= 3
ORDER BY d.name, r.salary DESC;
