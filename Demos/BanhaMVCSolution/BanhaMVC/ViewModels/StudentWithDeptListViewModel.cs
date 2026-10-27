using BanhaMVC.Models;

namespace BanhaMVC.ViewModels
{
    // ViewModel combining Student data with the list of all Departments for Add/Edit dropdown
    public class StudentWithDeptListViewModel
    {
        public int Id { get; set; }
        public string Name { get; set; } = string.Empty;
        public int Age { get; set; }
        public string? Address { get; set; }
        public int? DeptId { get; set; }

        // List of all departments for user selection
        public List<Department> DeptList { get; set; } = new List<Department>();
    }
}
