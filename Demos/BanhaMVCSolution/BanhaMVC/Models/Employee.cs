using System.ComponentModel.DataAnnotations.Schema;

namespace BanhaMVC.Models
{
    // Clean - expressive - get business !
    // 1- FK represent as code !
    // 2- EF + 6.0
    public class Employee
    {
        public int Id { get; set; } // not null
        public string Name { get; set; } // not null 
        public string Title { get; set; }
        public string Address { get; set; }
        public int Age { get; set; }

        // FK 
        /// <summary>
        /// FK for (Dept)
        /// </summary>
        public int? DeptId { get; set; }

        // rship with Dept 
        public Department? Dept { get; set; }
    }
}
