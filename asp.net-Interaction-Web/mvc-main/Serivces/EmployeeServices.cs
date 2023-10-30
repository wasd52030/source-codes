using MvcMain.Data;
using MvcMain.Models;
using Microsoft.EntityFrameworkCore;

public interface IEmployeeService
{
    Task<List<Employee>> getEmployees();
    Employee? getEmployeeById(int id);
    Task<bool> NewEmployee(Employee employee);
    Task<bool> UpdateEmployee(Employee employee);
    Task<bool> DeleteEmployee(int id);
}

public class EmployeeService : IEmployeeService
{
    private readonly ApplicationDBContext dbContext;
    public EmployeeService(ApplicationDBContext dbContext)
    {
        this.dbContext = dbContext;
    }

    public async Task<List<Employee>> getEmployees()
    {
        return await dbContext.Employees.ToListAsync();
    }

    public Employee? getEmployeeById(int id) => dbContext.Employees.FirstOrDefault(e => e.id == id);

    public async Task<bool> NewEmployee(Employee employee)
    {
        var emp = dbContext.Employees.Add(employee);
        Console.WriteLine(emp);
        await dbContext.SaveChangesAsync();
        return true;
    }

    public async Task<bool> UpdateEmployee(Employee employee)
    {
        dbContext.Employees.Update(employee);
        await dbContext.SaveChangesAsync();
        return true;
    }

    public async Task<bool> DeleteEmployee(int id)
    {
        var emp=getEmployeeById(id);
        dbContext.Employees.Remove(emp);
        await dbContext.SaveChangesAsync();
        return true;
    }
}