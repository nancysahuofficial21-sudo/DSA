# Write your MySQL query statement below
SELECT e.name AS name
FROM Employee e join Employee emp
ON e.id=emp.managerId
GROUP BY e.id, e.name
HAVING COUNT(emp.managerId)>=5;