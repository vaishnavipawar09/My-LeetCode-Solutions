# Write your MySQL query statement below
#BOth are friends
SELECT user_id AS id, COUNT(*) AS num              -- Count friends for each user
FROM (
    SELECT requester_id AS user_id FROM RequestAccepted  -- Get requesters
    UNION ALL
    SELECT accepter_id AS user_id FROM RequestAccepted   -- Get accepters
) AS all_friends
GROUP BY user_id                                  -- Group by user
ORDER BY num DESC                                 -- Most friends first
LIMIT 1;                                          -- Get top user only

