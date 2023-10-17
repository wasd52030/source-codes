using Microsoft.AspNetCore.Mvc;

namespace _20231016.Controllers
{
    [Route("[controller]")]
    public class HelloWorldController : Controller
    {
        private readonly ILogger<HelloWorldController> _logger;

        public HelloWorldController(ILogger<HelloWorldController> logger)
        {
            _logger = logger;
        }

        public IActionResult Index()
        {
            return Ok("Hello, World！");
        }

        [Route("[action]/{name}/{n}")]
        public IActionResult Welcome(string name, int n)
        {
            ViewData["message"] = $"Hello {name}";
            ViewData["n"] = n;
            return View();
            // return Ok(string.Join('\n', Enumerable.Repeat($"Hello {name}", n)));
        }

        [Route("[action]")]
        [ResponseCache(Duration = 0, Location = ResponseCacheLocation.None, NoStore = true)]
        public IActionResult Error()
        {
            return View("Error!");
        }
    }
}