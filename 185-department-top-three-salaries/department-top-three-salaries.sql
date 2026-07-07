SELECT
    d.name AS Department,
    e.name AS Employee,
    e.salary
FROM (
    SELECT *,
           DENSE_RANK() OVER (
               PARTITION BY departmentId
               ORDER BY salary DESC
           ) rnk
    FROM Employee
) e
JOIN Department d
ON e.departmentId = d.id
WHERE rnk <=3 ;