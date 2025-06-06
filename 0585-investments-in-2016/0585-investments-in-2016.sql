-- Step 1: Define both CTEs in a single WITH clause
WITH 
pidtiv AS (
    -- Find tiv_2015 values that occur more than once
    SELECT tiv_2015
    FROM Insurance
    GROUP BY tiv_2015
    HAVING COUNT(*) > 1
),
nosamecity AS (
    -- Find (lat, lon) pairs that are unique
    SELECT lat, lon
    FROM Insurance
    GROUP BY lat, lon
    HAVING COUNT(*) = 1
)

-- Step 2: Use both CTEs to filter the Insurance table
SELECT ROUND(SUM(tiv_2016), 2) AS tiv_2016
FROM Insurance
WHERE tiv_2015 IN (SELECT tiv_2015 FROM pidtiv) -- Condition 1: shared tiv_2015
  AND (lat, lon) IN (SELECT lat, lon FROM nosamecity); -- Condition 2: unique location
