using BanhaMVC.Data.DbContexts;
using Microsoft.EntityFrameworkCore;

namespace BanhaMVC.Models
{
    // Business Logic Container for Student Operations
    public class StudentBL
    {
        private readonly MsaooDbContext context = new MsaooDbContext();

        // Mock data fallback if database server is offline or unreachable
        private static readonly List<Student> _mockStudents = new List<Student>
        {
            new Student { Id = 1, Name = "Zeyad Mohamed", Age = 23, Address = "Banha", DeptId = 1, Department = new Department { Id = 1, Name = "Software Development" } },
            new Student { Id = 2, Name = "Ahmed Ali", Age = 22, Address = "Cairo", DeptId = 1, Department = new Department { Id = 1, Name = "Software Development" } },
            new Student { Id = 3, Name = "Sara Hassan", Age = 24, Address = "Giza", DeptId = 2, Department = new Department { Id = 2, Name = "Open Source & Web" } },
            new Student { Id = 4, Name = "Mahmoud Ibrahim", Age = 23, Address = "Alexandria", DeptId = 3, Department = new Department { Id = 3, Name = "AI & Data Science" } },
            new Student { Id = 5, Name = "Mona Youssef", Age = 22, Address = "Mansoura", DeptId = 2, Department = new Department { Id = 2, Name = "Open Source & Web" } },
            new Student { Id = 6, Name = "Omar Khaled", Age = 25, Address = "Tanta", DeptId = 4, Department = new Department { Id = 4, Name = "Cloud Computing & DevOps" } },
            new Student { Id = 7, Name = "Nour El-Din", Age = 21, Address = "Banha", DeptId = 1, Department = new Department { Id = 1, Name = "Software Development" } },
            new Student { Id = 8, Name = "Fatma Tarek", Age = 23, Address = "Cairo", DeptId = 3, Department = new Department { Id = 3, Name = "AI & Data Science" } }
        };

        // 1- Get all students (Eager Loading with Department)
        public List<Student> GetAll()
        {
            try
            {
                var list = context.Students.Include(s => s.Department).ToList();
                if (list != null && list.Count > 0)
                    return list;
            }
            catch
            {
                // Fallback to in-memory data
            }
            return _mockStudents;
        }

        // 2- Filtered & Paginated search
        public List<Student> GetFiltered(string? search, int? deptId, int page, int pageSize, out int totalCount)
        {
            try
            {
                var query = context.Students.Include(s => s.Department).AsQueryable();

                // Search by student name
                if (!string.IsNullOrWhiteSpace(search))
                {
                    search = search.Trim();
                    query = query.Where(s => s.Name.Contains(search));
                }

                // Filter by department
                if (deptId.HasValue && deptId.Value > 0)
                {
                    query = query.Where(s => s.DeptId == deptId.Value);
                }

                totalCount = query.Count();

                return query
                    .OrderBy(s => s.Id)
                    .Skip((page - 1) * pageSize)
                    .Take(pageSize)
                    .ToList();
            }
            catch
            {
                // Fallback logic for mock data
                var query = _mockStudents.AsQueryable();

                if (!string.IsNullOrWhiteSpace(search))
                {
                    search = search.Trim();
                    query = query.Where(s => s.Name.Contains(search, StringComparison.OrdinalIgnoreCase));
                }

                if (deptId.HasValue && deptId.Value > 0)
                {
                    query = query.Where(s => s.DeptId == deptId.Value);
                }

                totalCount = query.Count();

                return query
                    .OrderBy(s => s.Id)
                    .Skip((page - 1) * pageSize)
                    .Take(pageSize)
                    .ToList();
            }
        }

        // 3- Get student by ID
        public Student? GetById(int id)
        {
            try
            {
                var student = context.Students.Include(s => s.Department).FirstOrDefault(s => s.Id == id);
                if (student != null)
                    return student;
            }
            catch
            {
                // Fallback
            }
            return _mockStudents.FirstOrDefault(s => s.Id == id);
        }

        // 4- Add new student
        public void Add(Student student)
        {
            try
            {
                context.Students.Add(student);
                context.SaveChanges();
            }
            catch
            {
                student.Id = _mockStudents.Count > 0 ? _mockStudents.Max(s => s.Id) + 1 : 1;
                if (student.DeptId.HasValue)
                {
                    var depBL = new DepBL();
                    student.Department = depBL.GetAll().FirstOrDefault(d => d.Id == student.DeptId.Value);
                }
                _mockStudents.Add(student);
            }
        }

        // 5- Update student
        public void Update(int id, Student updatedStudent)
        {
            try
            {
                var existing = context.Students.FirstOrDefault(s => s.Id == id);
                if (existing != null)
                {
                    existing.Name = updatedStudent.Name;
                    existing.Age = updatedStudent.Age;
                    existing.Address = updatedStudent.Address;
                    existing.DeptId = updatedStudent.DeptId;
                    context.SaveChanges();
                    return;
                }
            }
            catch
            {
                // Fallback
            }

            var mock = _mockStudents.FirstOrDefault(s => s.Id == id);
            if (mock != null)
            {
                mock.Name = updatedStudent.Name;
                mock.Age = updatedStudent.Age;
                mock.Address = updatedStudent.Address;
                mock.DeptId = updatedStudent.DeptId;
                if (mock.DeptId.HasValue)
                {
                    var depBL = new DepBL();
                    mock.Department = depBL.GetAll().FirstOrDefault(d => d.Id == mock.DeptId.Value);
                }
            }
        }

        // 6- Delete student
        public void Delete(int id)
        {
            try
            {
                var student = context.Students.FirstOrDefault(s => s.Id == id);
                if (student != null)
                {
                    context.Students.Remove(student);
                    context.SaveChanges();
                    return;
                }
            }
            catch
            {
                // Fallback
            }

            var mock = _mockStudents.FirstOrDefault(s => s.Id == id);
            if (mock != null)
            {
                _mockStudents.Remove(mock);
            }
        }
    }
}
