using BanhaMVC.Models;

namespace BanhaMVC.ViewModels
{
    // ViewModel for GetAll/Index page supporting Search, Filter by Department, and Pagination
    public class StudentIndexViewModel
    {
        public List<Student> Students { get; set; } = new List<Student>();
        public List<Department> DeptList { get; set; } = new List<Department>();

        // Query criteria
        public string? Search { get; set; }
        public int? SelectedDeptId { get; set; }

        // Pagination metadata
        public int CurrentPage { get; set; } = 1;
        public int PageSize { get; set; } = 4;
        public int TotalPages { get; set; } = 1;
        public int TotalCount { get; set; } = 0;

        public bool HasPreviousPage => CurrentPage > 1;
        public bool HasNextPage => CurrentPage < TotalPages;
    }
}
