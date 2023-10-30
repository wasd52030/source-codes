using MvcMain.Models;
using Microsoft.AspNetCore.Mvc;
using MvcMain.Attributes;

namespace MvcMain.Controllers
{
    [AutoInject] 
    [Route("[controller]")]
    public partial class EmployeeController : Controller
    {
        [AutoInject]
        private readonly ILogger<EmployeeController> Logger;
        [AutoInject]
        private readonly IEmployeeService EmployeeService;

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
            return View(await EmployeeService.getEmployees());
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
                await EmployeeService.NewEmployee(employee);
                return RedirectToAction(nameof(Employees));
            }
            return View(employee);
        }
        [Route("[action]")]
        public IActionResult Update(int id)
        {
            Console.WriteLine(id);
            var emp = EmployeeService.getEmployeeById(id);
            return View(emp);
        }

        [Route("[action]")]
        [HttpPost]
        public async Task<IActionResult> UpdateEmployee(Employee employee)
        {
            Console.WriteLine(employee);
            if (ModelState.IsValid)
            {
                await EmployeeService.UpdateEmployee(employee);
                return RedirectToAction(nameof(Employees));
            }
            return View(employee);
        }

        [Route("[action]")]
        public async Task<IActionResult> Delete(int id)
        {
            Console.WriteLine(id);
            await EmployeeService.DeleteEmployee(id);
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