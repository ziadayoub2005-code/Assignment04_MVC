namespace BanhaMVC.Models
{
    public class Department
    {
        public int Id { get; set; }
        public string Name { get; set; }
        public string? Mgrname { get; set; }

        // Rship with Emps
        public List<Employee>? Employees { get; set; }

        // Rship with Students
        public List<Student>? Students { get; set; }
    }
}
