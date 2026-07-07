# Write your MySQL query statement below
WITH ranked_salary AS (
    SELECT d.name AS Department, e.name AS Employee, e.salary AS Salary, 
        DENSE_RANK() OVER (PARTITION BY e.departmentId ORDER BY e.salary DESC) AS `rank`
    FROM Employee e
    JOIN Department d ON d.id = e.departmentId
)
SELECT Department, Employee, Salary
FROM ranked_salary
WHERE `rank` <=3;
