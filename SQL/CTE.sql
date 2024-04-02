--example CTE as subquery

WITH orders_mini as (
    SELECT orderID, customer, datetime, ecom, shipto, state, tax
    FROM orders --where orders is a giant table, use a CTE to minimize bandwidth in the query
    WHERE datetime between '2023%' and '20250101'
)

SELECT *
FROM orders_mini
WHERE datetime = today()


