# Write your MySQL query statement below
SELECT p.product_id,
       COALESCE(p1.new_price, 10) AS price           #Checks if new_price is NULL, if yes assigns the 10 value
FROM (SELECT DISTINCT product_id FROM Products) p    #Unique Product IDs, Need All Products
LEFT JOIN (                                          #To preserve all product_ids
    SELECT product_id, new_price
    FROM Products
    WHERE change_date <= '2019-08-16'                # Interested in on or before that date
    AND (product_id, change_date ) IN (              #Inside IN, finds the latest price change date
      SELECT product_id, MAX(change_date)
      FROM Products
      WHERE change_date <= '2019-08-16'
      GROUP BY product_id
    )
) p1 ON p.product_id = p1.product_id;

