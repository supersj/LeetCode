select
(SELECT distinct(Salary) FROM Employee
UNION
SELECT NULL
ORDER BY Salary DESC LIMIT 1,1)
as SecondHighestSalary
