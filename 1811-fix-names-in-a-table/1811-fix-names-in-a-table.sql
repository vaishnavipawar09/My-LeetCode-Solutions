# Write your MySQL query statement below 
SELECT                      #Select user_id and formatted name
    user_id, 
    -- Make first character uppercase and rest lowercase
    CONCAT(UPPER(LEFT(name, 1)), LOWER(SUBSTRING(name, 2))) AS name
FROM Users
ORDER BY user_id;  -- Sort results by user_id
