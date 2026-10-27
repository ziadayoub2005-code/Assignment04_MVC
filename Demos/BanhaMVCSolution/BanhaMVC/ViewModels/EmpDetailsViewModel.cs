namespace BanhaMVC.ViewModels
{
    // EmpName - DeptName - Grade - status - skills
    public class EmpDetailsViewModel
    {
        public string EmpName { get; set; }
        public string DeptName { get; set; }
        public string Status { get; set; }
        public int Grade { get; set; }
        public List<string> SkillSet { get; set; }
    }
}
