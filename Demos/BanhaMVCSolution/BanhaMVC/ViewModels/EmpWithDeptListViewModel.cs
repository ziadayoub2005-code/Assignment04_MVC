using BanhaMVC.Models;

namespace BanhaMVC.ViewModels
{
    // Emp + List<Dep>
    public class EmpWithDeptListViewModel
    {
        // Emp
        public int Id { get; set; } 
        public string Name { get; set; } 
        public string Title { get; set; }
        public string Address { get; set; }
        public int Age { get; set; }
        public int? DeptId { get; set; }

        // List<dept>
        public List<Department> DeptList { get; set; }

    }
}
