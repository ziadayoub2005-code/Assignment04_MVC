using BanhaMVC.Data.ConfigurationClasses;
using BanhaMVC.Models;
using Microsoft.EntityFrameworkCore;

namespace BanhaMVC.Data.DbContexts
{
    // open connection DB 
    // 1- act as connection (inherit from Dbcontext)
    // 2- Connection data ! 
    // .NET 8.0
    public class MsaooDbContext : DbContext
    {
        protected override void OnConfiguring(DbContextOptionsBuilder optionsBuilder)
        {
            optionsBuilder.UseSqlServer("Data Source=.;Initial Catalog=Msaoo;Integrated Security=True;Encrypt=False;Trust Server Certificate=True");
        }

        // Dbsets :
        public DbSet<Employee> Employees { get; set; }
        public DbSet<Department> Departments { get; set; }
        public DbSet<Student> Students { get; set; }

        protected override void OnModelCreating(ModelBuilder modelBuilder)
        {
            // on line : scan assembly for implemnet IEntityTypeConfiguration
            // GP 

            modelBuilder.ApplyConfiguration(new DepartmentConfigurations());
            modelBuilder.ApplyConfiguration(new EmployeeConfigurations());
            modelBuilder.ApplyConfiguration(new StudentConfigurations());
        }
    }


}
