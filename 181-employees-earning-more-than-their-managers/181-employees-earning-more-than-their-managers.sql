# Write your MySQL query statement below

select e.name as employee
from Employee e inner join  Employee m
on e.salary > m.salary and e.managerid = m.id