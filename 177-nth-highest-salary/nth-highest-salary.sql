CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      # Write your MySQL query statement below.
      SELECT Salary as getNthHigehstSalary
      FROM (
            SELECT distinct Salary, DENSE_RANK() OVER ( ORDER BY Salary DESC) rnk
            FROM Employee
      ) t
      WHERE rnk = n
      
      
  );
END