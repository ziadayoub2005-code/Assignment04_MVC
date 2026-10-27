using BanhaMVC.Models;
using Microsoft.AspNetCore.Mvc;

namespace BanhaMVC.Controllers
{
    public class BindController : Controller
    {
        // Element : 
        // Collect Data ...

        // Binding : 
        // Req : keys and values ..
        // Keys is the same as parameters ...

        // Form : 
        // Controls : input - Select - .. 
        // submit .. -> Keys and values 
        // Keys : name attribute .. 
        // name attribute is the same as parameters name ... 

        // Data : 
        // 1- Req Body > FormData
        // 2- Route values
        // 3- Req Header > Querystring 
        // 4- Default values

        // Id : special Property : Routing ...

        // /Bind/Test?name=ali&age=34
        // /Bind/Test?name=ali&age=34&color=red
        // /Bind/Test?name=ali
        // /Bind/Test?name=ali&age=34&id=8
        // /Bind/Test/6?name=ali&age=34

        // /Bind/Test/4?name=ali&age=34&id=8
        
        public IActionResult Test(string Name,int Age,int id)
        {
            return View();
        }

        // refdister user .. 
        // add oppointment .. 
        // Add (name,time,type,name,address,....)

        // Bind not to primitive ..
        // Bind to model (domain - view - ...)

        // Bind to obj ..
        // Condition : 
        // Keys is the same as Properties of this obj ...

        // /Bind/TestComplex?Id=3&name=Pr&mgrname=Ismail
        public IActionResult TestComplex(Department Dept)
        {
            return View();
        }
    }
}
