using _20231016.Data;
using _20231016.Models;
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore.Storage;

namespace _20231016.Controllers
{
    [Route("[controller]")]
    public class EmployeeController : Controller
    {
        private readonly ILogger<EmployeeController> _logger;
        private readonly IEmployeeService employeeService;

        public EmployeeController(ILogger<EmployeeController> logger, IEmployeeService employeeService)
        {
            _logger = logger;
            this.employeeService = employeeService;
        }

        public IActionResult Index()
        {
            return View();
        }


        // add view by model
        // dotnet aspnet-codegenerator view ActionName [Empty|Create|Edit|Delete|Details|List] -outdir Views/ControllerName
        // example -> dotnet aspnet-codegenerator view Employees List -m Employee -outDir Views/Employee
        [Route("[action]")]
        public async Task<IActionResult> Employees()
        {
            return View(await employeeService.getEmployees());
        }

        [Route("[action]")]
        public IActionResult Create()
        {
            return View();
        }

        [Route("[action]")]
        [HttpPost]
        public async Task<IActionResult> Create(Employee employee)
        {
            Console.WriteLine(employee);
            if (ModelState.IsValid)
            {
                await employeeService.NewEmployee(employee);
                return RedirectToAction(nameof(Employees));
            }
            return View(employee);
        }
        [Route("[action]")]
        public IActionResult Update(int id)
        {
            Console.WriteLine(id);
            var emp = employeeService.getEmployeeById(id);
            return View(emp);
        }

        [Route("[action]")]
        [HttpPost]
        public async Task<IActionResult> UpdateEmployee(Employee employee)
        {
            Console.WriteLine(employee);
            if (ModelState.IsValid)
            {
                await employeeService.UpdateEmployee(employee);
                return RedirectToAction(nameof(Employees));
            }
            return View(employee);
        }

        [Route("[action]")]
        public async Task<IActionResult> Delete(int id)
        {
            Console.WriteLine(id);
            await employeeService.DeleteEmployee(id);
            return RedirectToAction(nameof(Employees));
        }

        [Route("[action]")]
        [ResponseCache(Duration = 0, Location = ResponseCacheLocation.None, NoStore = true)]
        public IActionResult Error()
        {
            return View("Error!");
        }
    }
}