namespace BanhaMVC.Models
{
    public class Student
    {
        public int Id { get; set; }
        public string Name { get; set; } = string.Empty;
        public int Age { get; set; }
        public string? Address { get; set; }

        // Foreign Key for Department
        public int? DeptId { get; set; }

        // Navigation property
        public Department? Department { get; set; }
    }
}
