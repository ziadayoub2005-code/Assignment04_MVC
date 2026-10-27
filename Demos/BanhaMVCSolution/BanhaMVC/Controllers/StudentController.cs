using BanhaMVC.Models;
using BanhaMVC.ViewModels;
using Microsoft.AspNetCore.Mvc;

namespace BanhaMVC.Controllers
{
    // Full business life Cycle of Student Controller
    // 1- GetAll (with Pagination, Search by name, Filter by Department)
    // 2- GetById (Student details)
    // 3- Add (show all Departments in dropdown)
    // 4- Edit (show all Departments in dropdown)
    // 5- Delete (direct to warning View, then ConfirmDelete)
    public class StudentController : Controller
    {
        private readonly StudentBL studentBL = new StudentBL();
        private readonly DepBL depBL = new DepBL();

        // =========================================================
        // 1- GetAll Life Cycle (Pagination + Search + Filter)
        // URL: /Student/GetAll?search=ali&deptId=1&page=1
        // =========================================================
        public IActionResult GetAll(string? search, int? deptId, int page = 1, int pageSize = 4)
        {
            if (page < 1) page = 1;
            if (pageSize < 1) pageSize = 4;

            int totalCount;
            var students = studentBL.GetFiltered(search, deptId, page, pageSize, out totalCount);
            var depts = depBL.GetAll();

            var totalPages = (int)Math.Ceiling((double)totalCount / pageSize);
            if (totalPages < 1) totalPages = 1;

            var viewModel = new StudentIndexViewModel
            {
                Students = students,
                DeptList = depts,
                Search = search,
                SelectedDeptId = deptId,
                CurrentPage = page,
                PageSize = pageSize,
                TotalCount = totalCount,
                TotalPages = totalPages
            };

            return View("GetAll", viewModel);
        }

        // Default Index action redirects to GetAll
        public IActionResult Index(string? search, int? deptId, int page = 1, int pageSize = 4)
        {
            return GetAll(search, deptId, page, pageSize);
        }

        // =========================================================
        // 2- GetById Life Cycle (Details)
        // URL: /Student/GetById/1
        // =========================================================
        public IActionResult GetById(int id)
        {
            var student = studentBL.GetById(id);
            if (student == null)
            {
                return NotFound();
            }

            return View("Details", student);
        }

        // Details alias
        public IActionResult Details(int id)
        {
            return GetById(id);
        }

        // =========================================================
        // 3- Add Life Cycle
        // Step 1: Open Add Form with all Departments in dropdown
        // URL: /Student/Add
        // =========================================================
        [HttpGet]
        public IActionResult Add()
        {
            var viewModel = new StudentWithDeptListViewModel
            {
                DeptList = depBL.GetAll()
            };

            return View("Add", viewModel);
        }

        // Step 2: Handle Add submission & Model Binding
        // URL: /Student/SaveAdd (POST)
        [HttpPost]
        public IActionResult SaveAdd(Student student)
        {
            // Simple validation
            if (!string.IsNullOrWhiteSpace(student.Name))
            {
                studentBL.Add(student);
                return RedirectToAction(nameof(GetAll));
            }

            // If invalid, reload form with department list
            var viewModel = new StudentWithDeptListViewModel
            {
                Name = student.Name,
                Age = student.Age,
                Address = student.Address,
                DeptId = student.DeptId,
                DeptList = depBL.GetAll()
            };

            return View("Add", viewModel);
        }

        // =========================================================
        // 4- Edit Life Cycle
        // Step 1: Open Edit Form with old record + Departments dropdown
        // URL: /Student/Edit/1
        // =========================================================
        [HttpGet]
        public IActionResult Edit(int id)
        {
            var student = studentBL.GetById(id);
            if (student == null)
            {
                return NotFound();
            }

            var viewModel = new StudentWithDeptListViewModel
            {
                Id = student.Id,
                Name = student.Name,
                Age = student.Age,
                Address = student.Address,
                DeptId = student.DeptId,
                DeptList = depBL.GetAll()
            };

            return View("Edit", viewModel);
        }

        // Step 2: Save Edited Student to DB
        // URL: /Student/SaveEdit/1 (POST)
        [HttpPost]
        public IActionResult SaveEdit(Student student, int id)
        {
            if (!string.IsNullOrWhiteSpace(student.Name))
            {
                studentBL.Update(id, student);
                return RedirectToAction(nameof(GetAll));
            }

            // If invalid, reload form
            var viewModel = new StudentWithDeptListViewModel
            {
                Id = id,
                Name = student.Name,
                Age = student.Age,
                Address = student.Address,
                DeptId = student.DeptId,
                DeptList = depBL.GetAll()
            };

            return View("Edit", viewModel);
        }

        // =========================================================
        // 5- Delete Life Cycle (Safe UX)
        // Step 1: Direct to Warning View before deletion
        // URL: /Student/Delete/1
        // =========================================================
        [HttpGet]
        public IActionResult Delete(int id)
        {
            var student = studentBL.GetById(id);
            if (student == null)
            {
                return NotFound();
            }

            // Opens warning page asking for confirmation
            return View("Delete", student);
        }

        // Step 2: Confirm Delete from DB
        // URL: /Student/ConfirmDelete/1 (POST)
        [HttpPost]
        public IActionResult ConfirmDelete(int id)
        {
            var student = studentBL.GetById(id);
            if (student != null)
            {
                studentBL.Delete(id);
                return RedirectToAction(nameof(GetAll));
            }

            return NotFound();
        }
    }
}
