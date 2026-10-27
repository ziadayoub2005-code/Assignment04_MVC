using BanhaMVC.Models;
using Microsoft.EntityFrameworkCore;
using Microsoft.EntityFrameworkCore.Metadata.Builders;

namespace BanhaMVC.Data.ConfigurationClasses
{
    public class EmployeeConfigurations : IEntityTypeConfiguration<Employee>
    {
        public void Configure(EntityTypeBuilder<Employee> builder)
        {
            // Db objects
            builder.ToTable("Employees");
            // key
            builder.HasKey(E => E.Id);
            // Prop
            builder.Property(E => E.Name)
                .HasMaxLength(100);
            // relationship
            // relationship with Department (here)
            builder.HasOne(E => E.Dept)
                .WithMany(D => D.Employees)
                .HasForeignKey(E => E.DeptId)
                .OnDelete(DeleteBehavior.Restrict);
        }
    }
}
