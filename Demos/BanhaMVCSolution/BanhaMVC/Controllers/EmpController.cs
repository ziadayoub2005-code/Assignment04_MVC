using BanhaMVC.Models;
using BanhaMVC.ViewModels;
using Microsoft.AspNetCore.Mvc;

namespace BanhaMVC.Controllers
{
    // send more than one info - set of values :
    // -> overload : helper method View ?  No 
    // -> Prop : holds more than info - set of values : 
    // Collections -> Prop -> more than info / set of values ..
    // 1- ViewData ... hold more than info - any info 
    // clean code .. no prior definition - fast look up 
    // Dictionary -> Key : string , value : object
    // ViewData["grade"] = grade;

    // 2- ViewBag : dynamic wrapper in same dictionary ... (dynamic)
    // ViewBag.grade = grade;

    // ViewData - ViewBag -> Dictionary : set of values - any value ?!
    // Business ? 
    // Not use -> Business
    // why ?! 
    // Specific details -> Views -> Page title(tab), alert ..

    // Domain Model -> classes of system
    // View Model -> classes from action to View
    // BE -> FE -> ViewModel

    // 3- custom class :
    // View Model : 
    // 3-1 Customization ?
    // select some prop of model >> light object -> quick response
    // merge more than one model -> shape needed data from different sources !
    // 3-2 Security .. (API) .. DTO
    // models -> Definitions -> Change them
    // 3-3 Separation of Concerns  
    // validations > data annotations > Clean design 

    // Action based on Domain model ...
    // Action based on View model ...

    // set in ViewData["grade"] >  read ViewBag.grade

    public class EmpController : Controller
    {
        EmployeeBL employeeBL = new EmployeeBL();
        DepBL depBL = new DepBL();

        // req handle
        // BL Coordinate 
        // Provide res

        // Action based on Domain model
        // /Emp/Details?id=1
        public IActionResult Details(int id)
        {
            // BL Container 
            // EmpBL 
            Employee Emp = employeeBL.GetById(id);

            int grade = 67;
            string Status = "B";
            List<string> skills = new List<string>() { "teamwork", "Communication" };

            ViewData["grade"] = grade;
            ViewData["Status"] = Status;
            ViewData["skills"] = skills;

            return View("Details", Emp); // model Employee
        }


        // Action based on ViewModel 
        // 1- ViewModel ...
        // EmpName - DeptName - Grade - status - skills

        // Manual Mapping : Sources - Destination - Mapping
        // Auto Mapper : Sources - Destoination (Auto)

        // /Emp/DetailsVM?id=2
        public IActionResult DetailsVM(int id)
        {
            //1-Sources .. 
            Employee Emp = employeeBL.GetById(id);
            int grade = 67;
            string Status = "B";
            List<string> skills = new List<string>() { "teamwork", "Communication" };
            //2-destination ..
            EmpDetailsViewModel EVM = new EmpDetailsViewModel();
            //3-Mapping ..
            EVM.EmpName = Emp.Name;
            EVM.DeptName = Emp?.Dept?.Name;
            EVM.Status = Status;
            EVM.Grade = grade;
            EVM.SkillSet = skills;

            return View("DetailsVM", EVM); // EmpDetailsViewModel
        }

        // /Emp/Index
        public IActionResult Index()
        {
            return View("Index", employeeBL.GetAll()); // model : list<Employee>
        }

        // /Emp/Edit/2
        public IActionResult Edit(int id)
        {
            // resources
            Employee Emp = employeeBL.GetById(id);
            List<Department> DeptList = depBL.GetAll();
            // Destination 
            EmpWithDeptListViewModel EDVM = new EmpWithDeptListViewModel();
            // Mapp 
            EDVM.Id = Emp.Id;
            EDVM.Name = Emp.Name;
            EDVM.Age = Emp.Age;
            EDVM.Address = Emp.Address;
            EDVM.Title = Emp.Title;
            EDVM.DeptId = Emp.DeptId;
            EDVM.DeptList = DeptList;

            return View("Edit", EDVM); //ViewModel EmpWithDeptListViewModel
        }

        // Id=2
        // name=Ismail,Age=30,....
        // /Emp/SaveEdit/2
        public IActionResult SaveEdit(Employee emp, int id)
        {
            if (emp.Name != null)
            {
                // Edit to Db
                // Edit philosophy : Old - New - Update ..

                Employee OldEmp = employeeBL.GetById(id);

                // approach01

                //// Update : local 
                OldEmp.Name = emp.Name;
                OldEmp.Address = emp.Address;
                OldEmp.Age = emp.Age;
                OldEmp.Title = emp.Title;
                OldEmp.DeptId = emp.DeptId;
                // Update DB : context -> BL ..
                employeeBL.SaveInDb();
                // if Saved -> new req ..

                // approach02 
                // Update entry (modified) .. 
                //employeeBL.Update(emp);

                // /Emp/Index
                return RedirectToAction(nameof(Index));
            }
            return View("Edit", emp);
        }

        // /Emp/Delete/2
        public IActionResult Delete(int id)
        {
            // catch delete obj(Emp)
            return View("delete", employeeBL.GetById(id)); // model employee
        }

        // /Emp/ConfirmDelete/3
        public IActionResult ConfirmDelete(int id)
        {
            // catch Deleted obj 
            Employee DeletedEmp=employeeBL.GetById(id);
            // sure ?
            if(DeletedEmp != null)
            {
                // delete fronm DB
                // context -> BL 
                employeeBL.Delete(DeletedEmp);
                // id deleted
                return RedirectToAction(nameof(Index));
            }
            return NotFound();
        }

        // Edit life cycle : 
        // 1- UX  -> Edit button - besides Element 
        // Index Page -> Index Lifecycle
        // 2- Edit action (Open edit Page With Old record)
        // 3- Edit Page/Form 
        // 4- Action : Edit on DB - Model Bind 

        // Dillema : UX : not clean - Exceptions ..
        // Departments -> User : Choose : Drop down list ...
        // BE(action) -> FE(View) -> Emp + List<Department> 
        // merge more than model : VD - VB : Page titles .. 
        // ViewModel(Used) : Emp - List<Departments>

        // UX : real option - Tag Helper (handle this)

        // Delete life cycle : 
        // 1- UX : Index -> Delete besides element 
        // 2- delete action -> delete from DB
        // -> alert Page -> open warning Page
        // 3- Warning Page
        // 4- ConfirmDelete action : delete from DB
    }
}
