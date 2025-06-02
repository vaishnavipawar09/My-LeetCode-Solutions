# Write your MySQL query statement below
SELECT results
FROM (
     -- Subquery 1: Find user with most ratings
    SELECT name AS results
    FROM (
        SELECT u.name, COUNT(*) AS total_ratings
        FROM MovieRating r
        JOIN Users u ON r.user_id = u.user_id
        GROUP BY r.user_id
        ORDER BY total_ratings DESC, name ASC
        LIMIT 1
    ) AS top_user
    

    UNION ALL

    -- Subquery 2: Find top-rated movie in Feb 2020
    SELECT title AS results
    FROM (
        SELECT m.title, AVG(r.rating) AS avg_rating
        FROM MovieRating r
        JOIN Movies m ON r.movie_id = m.movie_id
        WHERE r.created_at BETWEEN '2020-02-01' AND '2020-02-29'        #requires month february
        GROUP BY r.movie_id
        ORDER BY avg_rating DESC, title ASC                      #tie, return lexicographically smaller movie name.
        LIMIT 1
    ) AS top_movie
    
) AS final_output;

