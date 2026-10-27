using BanhaMVC.Data.DbContexts;
using Microsoft.EntityFrameworkCore;

namespace BanhaMVC.Models
{
   
    // Container operations on Employee
    public class EmployeeBL
    {
        MsaooDbContext context = new MsaooDbContext();

        // 1- 
        // Get emp details :
        // GetBy ? Unique -> Id -> PK -> 

        public Employee GetById(int id)
        {
            return context.Employees.Include(E => E.Dept).FirstOrDefault(E => E.Id == id);
        }

        // 2- BL -> get all :
        public List<Employee> GetAll()
        {
            return context.Employees.ToList();
        }

        // 3-1 Save in DB 
        public void SaveInDb()
        {
            context.SaveChanges();
        }

        // 3-2
        //public void Update(Employee Emp)
        //{
        //    // local
        //    context.Employees.Update(Emp); // Modified
        //    // DB
        //    context.SaveChanges();
        //    // Update statemnt 
        //}

        // 4- Delete 
        public void Delete(Employee Emp)
        {
            // delete form local 
            context.Employees.Remove(Emp);
            // delete from DB
            context.SaveChanges();
        }

    }
}
