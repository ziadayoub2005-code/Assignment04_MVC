using BanhaMVC.Data.DbContexts;
using Microsoft.EntityFrameworkCore;

namespace BanhaMVC.Models
{
    // Container : BL/operations/Fetching - Dept
    public class DepBL
    {
        MsaooDbContext context = new MsaooDbContext();

        private static readonly List<Department> _mockDepts = new List<Department>
        {
            new Department { Id = 1, Name = "Software Development", Mgrname = "Eng. Abdelrahman Elwakeel" },
            new Department { Id = 2, Name = "Open Source & Web", Mgrname = "Dr. Mohamed Ali" },
            new Department { Id = 3, Name = "AI & Data Science", Mgrname = "Eng. Sara Ahmed" },
            new Department { Id = 4, Name = "Cloud Computing & DevOps", Mgrname = "Eng. Mahmoud Hassan" }
        };

        // 1- Get all Depts : 
        public List<Department> GetAll()
        {
            try
            {
                var list = context.Departments.Include(D => D.Employees).ToList();
                if (list != null && list.Count > 0)
                    return list;
            }
            catch
            {
                // Fallback if DB is not connected locally
            }
            return _mockDepts;
        }

        // 2- Add Dept 
        public void AddDept(Department Dept)
        {
            try
            {
                context.Add(Dept);
                context.SaveChanges();
            }
            catch
            {
                Dept.Id = _mockDepts.Count > 0 ? _mockDepts.Max(d => d.Id) + 1 : 1;
                _mockDepts.Add(Dept);
            }
        }
    }
}
