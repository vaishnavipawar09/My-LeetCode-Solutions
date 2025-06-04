-- First, summarize total amount per day (in case of multiple customers)
WITH daily AS (                                         --	Pre-sums amount per date, so multiple transactions on a day are combined
    SELECT visited_on, SUM(amount) AS daily_total
    FROM Customer
    GROUP BY visited_on
)

-- Now, compute the 7-day rolling sum and average
SELECT 
    d1.visited_on,
    SUM(d2.daily_total) AS amount,                        -- sum of last 7 days
    ROUND(AVG(d2.daily_total), 2) AS average_amount       -- avg over 7 days, rounded to 2 decimal places
FROM daily d1
JOIN daily d2 
  ON d2.visited_on BETWEEN DATE_SUB(d1.visited_on, INTERVAL 6 DAY) AND d1.visited_on 
  #DATE-SUB Gets the date 6 days before the current day, so the window is 7 days (current + past 6)
GROUP BY d1.visited_on
HAVING COUNT(*) = 7                                        -- ensure full 7-day window
ORDER BY d1.visited_on ASC;
