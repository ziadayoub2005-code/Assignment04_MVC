using BanhaMVC.Data.DbContexts;
using BanhaMVC.Models;
using Microsoft.AspNetCore.Mvc;
using System.Diagnostics;
using System.Xml.Linq;

namespace BanhaMVC.Controllers
{
    // req handle 
    // BL Coordinate -> get all Depts
    // Provide res to view 

    // By default EF not load related entity !!

    // Explicit Loading ?! 
    // Include (EFCore)

    // Self : important
    // Eager Loading - Lazy Loading : self
    // EF befor core : Loading Options Vs after Core : self

    public class DepartmentController : Controller
    {
        DepBL depBL = new DepBL();

        // /Department/Index
        public IActionResult Index()
        {
            // decide data to be fetched / operatio on DB
            List<Department> Depts = depBL.GetAll();
            return View("Index", Depts); // model : List<Department>
        }

        // /Department/Add
        public IActionResult Add()
        {
            return View("Add"); // model : null
        }

        // /Department/SaveAdd?Name=media&Mgrname=Ali
        public IActionResult SaveAdd(Department Dept)
        {
            // validation to be right - BL ..
            if (Dept.Name != null)
            {
                // Save to DB
                // context -> BL -> Model 
                depBL.AddDept(Dept);
                // if Saved ?
                // /Department/Index
                return RedirectToAction(nameof(Index));
            }
            return View("Add", Dept); // model Department
        }

        // Operation on DB ...
        // /Dept/Add?Name=Hr&mgrname=ali
        // BE - ModelBinding ...

        // Add Dep Life Cycle : 
        // 1- UX .. add New Anchor ...
        // 2- Add action : open add page / form
        // 3- View/Form to add dep
        // 4- SavaAdd : Add to DB - Binding

    }
}
