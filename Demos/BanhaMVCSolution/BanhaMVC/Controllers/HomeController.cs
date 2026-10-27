using System.Diagnostics;
using BanhaMVC.Models;
using Microsoft.AspNetCore.Mvc;

namespace BanhaMVC.Controllers
{
    public class HomeController : Controller
    {
        // Mapping / Routing : 
        // handle Req - Res
        // send to view 
        // .......

        // Controller factory : self
        // builder.Services.AddControllersWithViews();
        // /Home/Index 
        // create an object - Index -> Life cycle 

        // class act as controller(to be mapped/Routed) : 
        // 1- end with "Controller"
        // 2- Inherit from controller !!

        // function to be mapped / Routed ?
        // 1-public
        // 2-not overloaded
        // 3-not static 

        // /Home/Index
        public IActionResult Index()
        {
            return View("Index");
        }

        public IActionResult Privacy()
        {
            return View("Privacy");
        }

        // Our own Req : Hello world

        // /Home/ShowMsg
        public string ShowMsg()
        {
            return "Hello World !";
        }

        // Level 01 :
        // Function inside controller !!
        // handle req - Coordinate BL - send data to View
        // function : obj - int - string 

        // Special Function ...
        // Action(MVC) / EndPoint
        // standard of special data types + Protocols / standards 
        // ActionResult , IActionResult  > Generalization

        // View            ViewResult
        // NotFound        NotFoundResult
        // Unauthorized    UnauthorizedResult
        // Json            JsonResult
        // File            FileResult 
        // Content         ContentResult
        // ........................

        // /Home/ShowMsg02
        public ContentResult ShowMsg02()
        {
            // declare
            ContentResult result = new ContentResult();
            // initial 
            result.Content = "Hello World !";
            // return 
            return result;
        }

        // level 02 
        // /Home/ShowView
        public ViewResult ShowView()
        {
            // declare 
            ViewResult result = new ViewResult();
            // Initial 
            result.ViewName = "View01";
            // return 
            return result;
        }

        // level 03
        // 1- General Form : Actionresult / IActioResult
        // Abstraction(yes)  -  Concreteness : self
        // 2- DRY : MS : Helper method

        // Reusable Code : Function : 
        //public ViewResult View(string ViewName)
        //{
        //    // declare 
        //    ViewResult result = new ViewResult();
        //    // Initial 
        //    result.ViewName = ViewName;
        //    // return 
        //    return result;
        //}
        
        public IActionResult ShowMix(int id)
        {
            if(id % 2 == 1)
            {
                return Content("Hello World !");
            }
            else
            {
                return View("View01");
            }
        }


        // 2 Pages : Compete life cycles : 
        // retreival pages : 

        // 1- details of specific element(entity)
        // 2- Wide range of data

        // Steps : 
        // Life cycle of my sys Hr (get all depts): 
        // Life cycle of my sys Hr (get specific emp): 

        // SRS -> UI -> Classes Specs Document ->  Develop ?
        // Models :
        // 1- models (classes of business - BL on Classes)
        // 1-1 build models/entitis of business
        // 1-2 Map
        // 1-2-1 environment (packages)
        // 1-2-2 DbContext (Connection data)
        // 1-2-2 Configurations (tables)
        // 1-2-2 DbContext (Call Mapping - Practice)
        // 1-2-3 Execute mapping (small note - data(files) - Seed data)
        // static structure has been allocated ?!
        // AI-deriven Develop
        // 2- modelBL

        // 2- controllers 
        // get all deapertments -> on Dept -> DeptController
        // get emp -> on Emp -> EmpController
        // handle req - coordinate BL - provide response

        // 3- views
        // Table as element - h1(h2-h3-h4-h5-h6) - SEO - Bootstrap Classes

        // Explicit loading , lazy and eager loading
    }
}
