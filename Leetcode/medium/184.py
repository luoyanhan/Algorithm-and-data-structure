select Department.Name as `Department`, Employee.Name as `Employee`, Employee.Salary from Employee join Department on Employee.DepartmentId = Department.Id and (Employee.Salary, Employee.DepartmentId) in
(select max(Salary), DepartmentId from Employee group by DepartmentId);


select Department.Name as `Department`, aa.Name as `Employee`, aa.Salary from (select a.Name, a.Salary, a.DepartmentId from Employee a join (select DepartmentId, max(Salary) as max_s from Employee group by DepartmentId) b on a.DepartmentId=b.DepartmentId and a.Salary=b.max_s) aa join Department on aa.DepartmentId=Department.Id;