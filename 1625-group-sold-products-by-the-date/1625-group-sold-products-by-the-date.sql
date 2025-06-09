# Write your MySQL query statement below
-- Select sell date, count of unique products, and comma-separated product list
SELECT 
    sell_date,
    COUNT(DISTINCT product) AS num_sold,  -- Count of different products sold on that date
    GROUP_CONCAT(DISTINCT product ORDER BY product ASC SEPARATOR ',') AS products  -- Sorted product names
FROM Activities
GROUP BY sell_date  -- Group by date
ORDER BY sell_date; -- Return in date order
