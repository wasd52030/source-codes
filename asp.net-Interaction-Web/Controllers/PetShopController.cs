using Microsoft.AspNetCore.Mvc;

namespace _20231016.Controllers
{
    [Route("[controller]")]
    public class PetShopController : Controller
    {
        private readonly ILogger<PetShopController> _logger;

        public PetShopController(ILogger<PetShopController> logger)
        {
            _logger = logger;
        }

        public IActionResult Index()
        {
            ViewData["company"]="汪興仁寵物店";
            ViewData["address"]="高雄市楠梓區右昌一巷500號";

            var pets= new List<string>
            {
                "狗",
                "貓",
                "魚",
                "鼠",
                "變色龍"
            };
            ViewData.Model=pets;
            return View();
        }

        [Route("[action]")]
        [ResponseCache(Duration = 0, Location = ResponseCacheLocation.None, NoStore = true)]
        public IActionResult Error()
        {
            return View("Error!");
        }
    }
}