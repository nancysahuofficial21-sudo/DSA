CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      # Write your MySQL query statement below.
      SELECT Salary as getNthHigehstSalary
      FROM (
            SELECT DISTINCT Salary, DENSE_RANK() OVER ( ORDER BY Salary DESC) rnk
            FROM Employee
      ) t
      WHERE rnk = n
      
  );
END