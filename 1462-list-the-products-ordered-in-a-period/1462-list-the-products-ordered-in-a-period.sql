# Write your MySQL query statement below
-- Select product name and total units for products ordered at least 100 times in Feb 2020
SELECT 
    p.product_name,
    SUM(o.unit) AS unit  -- Total units ordered
FROM 
    Orders o
JOIN 
    Products p ON o.product_id = p.product_id  -- Join orders with product info
WHERE 
    o.order_date BETWEEN '2020-02-01' AND '2020-02-29'  -- Only Feb 2020 orders
GROUP BY 
    o.product_id
HAVING 
    SUM(o.unit) >= 100  -- Only include products with 100 or more units
