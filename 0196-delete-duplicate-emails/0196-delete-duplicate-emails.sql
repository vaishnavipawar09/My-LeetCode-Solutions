DELETE p
FROM Person p
JOIN (
    SELECT email, MIN(id) AS min_id
    FROM Person
    GROUP BY email
) keep
ON p.email = keep.email AND p.id != keep.min_id;
