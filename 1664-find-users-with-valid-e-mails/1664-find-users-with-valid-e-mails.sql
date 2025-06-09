# Write your MySQL query statement below
-- Select users whose emails are valid
SELECT *
FROM Users
WHERE 
    -- Check if email ends with "@leetcode.com"
    mail LIKE '%@leetcode.com'
    
    -- Check if email starts with a valid character: a letter (uppercase or lowercase)
    AND mail REGEXP '^[a-zA-Z]'

    -- Check if email only contains valid characters before the @: letters, digits, '_', '.', '-'
    AND mail REGEXP '^[a-zA-Z][a-zA-Z0-9_.-]*@leetcode\\.com$'
