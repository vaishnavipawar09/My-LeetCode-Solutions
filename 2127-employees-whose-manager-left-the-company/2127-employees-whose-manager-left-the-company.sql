# Write your MySQL query statement below
SELECT e1.employee_id
FROM Employees e1
LEFT JOIN Employees e2 ON e1.manager_id = e2.employee_id        #To check on null
#The below statement handle, when the manager left and also when they never had a manager
WHERE e1.salary < 30000 AND e1.manager_id IS NOT NULL AND e2.employee_id IS NULL
ORDER BY e1.employee_id;



