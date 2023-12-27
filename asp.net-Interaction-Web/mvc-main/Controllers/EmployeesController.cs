using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.Rendering;
using Microsoft.EntityFrameworkCore;
using MvcMain.Attributes;
using MvcMain.Models;

namespace mvc_main.Controllers
{
    [AutoInject]
    public partial class EmployeesController : Controller
    {
        [AutoInject]
        private readonly NorthwindContext Context;

        // public EmployeesController(NorthwindContext context)
        // {
        //     Context = context;
        // }

        // GET: Employees
        public async Task<IActionResult> Index()
        {
            Console.WriteLine(Context == null);
            var northwindContext = Context.Employees.Include(e => e.ReportsToNavigation);
            var el = await northwindContext.ToListAsync();
            return View(el);
        }

        // GET: Employees/Details/5
        public async Task<IActionResult> Details(long? id)
        {
            if (id == null || Context.Employees == null)
            {
                return NotFound();
            }

            var employee = await Context.Employees
                .Include(e => e.ReportsToNavigation)
                .FirstOrDefaultAsync(m => m.EmployeeId == id);
            if (employee == null)
            {
                return NotFound();
            }

            return View(employee);
        }

        // GET: Employees/Create
        public IActionResult Create()
        {
            ViewData["ReportsTo"] = new SelectList(Context.Employees, "EmployeeId", "EmployeeId");
            return View();
        }

        // POST: Employees/Create
        // To protect from overposting attacks, enable the specific properties you want to bind to.
        // For more details, see http://go.microsoft.com/fwlink/?LinkId=317598.
        [HttpPost]
        [ValidateAntiForgeryToken]
        public async Task<IActionResult> Create([Bind("EmployeeId,LastName,FirstName,Title,TitleOfCourtesy,BirthDate,HireDate,Address,City,Region,PostalCode,Country,HomePhone,Extension,ReportsTo,Notes")] Employee employee)
        {
            if (ModelState.IsValid)
            {
                Context.Add(employee);
                await Context.SaveChangesAsync();
                return RedirectToAction(nameof(Index));
            }
            ViewData["ReportsTo"] = new SelectList(Context.Employees, "EmployeeId", "EmployeeId", employee.ReportsTo);
            return View(employee);
        }

        // GET: Employees/Edit/5
        public async Task<IActionResult> Edit(long? id)
        {
            if (id == null || Context.Employees == null)
            {
                return NotFound();
            }

            var employee = await Context.Employees.FindAsync(id);
            if (employee == null)
            {
                return NotFound();
            }
            ViewData["ReportsTo"] = new SelectList(Context.Employees, "EmployeeId", "EmployeeId", employee.ReportsTo);
            return View(employee);
        }

        // POST: Employees/Edit/5
        // To protect from overposting attacks, enable the specific properties you want to bind to.
        // For more details, see http://go.microsoft.com/fwlink/?LinkId=317598.
        [HttpPost]
        [ValidateAntiForgeryToken]
        public async Task<IActionResult> Edit(long id, [Bind("EmployeeId,LastName,FirstName,Title,TitleOfCourtesy,BirthDate,HireDate,Address,City,Region,PostalCode,Country,HomePhone,Extension,Notes,ReportsTo")] Employee employee)
        {
            var e = Context.Employees.FirstOrDefault(e => e.EmployeeId == id);
            if (id != employee.EmployeeId && e == null)
            {
                return NotFound();
            }

            if (ModelState.IsValid)
            {
                try
                {
                    Context.Entry(e!).CurrentValues.SetValues(employee);
                    // Context.Update(employee);
                    await Context.SaveChangesAsync();
                }
                catch (DbUpdateConcurrencyException)
                {
                    if (!EmployeeExists(employee.EmployeeId))
                    {
                        return NotFound();
                    }
                    else
                    {
                        throw;
                    }
                }
                return RedirectToAction(nameof(Index));
            }
            ViewData["ReportsTo"] = new SelectList(Context.Employees, "EmployeeId", "EmployeeId", employee.ReportsTo);
            return View(employee);
        }

        // GET: Employees/Delete/5
        public async Task<IActionResult> Delete(long? id)
        {
            if (id == null || Context.Employees == null)
            {
                return NotFound();
            }

            var employee = await Context.Employees
                .Include(e => e.ReportsToNavigation)
                .FirstOrDefaultAsync(m => m.EmployeeId == id);
            if (employee == null)
            {
                return NotFound();
            }

            return View(employee);
        }

        // POST: Employees/Delete/5
        [HttpPost, ActionName("Delete")]
        [ValidateAntiForgeryToken]
        public async Task<IActionResult> DeleteConfirmed(long id)
        {
            if (Context.Employees == null)
            {
                return Problem("Entity set 'NorthwindContext.Employees'  is null.");
            }
            var employee = await Context.Employees.FindAsync(id);
            if (employee != null)
            {
                Context.Employees.Remove(employee);
            }

            await Context.SaveChangesAsync();
            return RedirectToAction(nameof(Index));
        }

        private bool EmployeeExists(long id)
        {
            return (Context.Employees?.Any(e => e.EmployeeId == id)).GetValueOrDefault();
        }
    }
}
