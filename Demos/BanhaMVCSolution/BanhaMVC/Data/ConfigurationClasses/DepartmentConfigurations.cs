using BanhaMVC.Models;
using Microsoft.EntityFrameworkCore;
using Microsoft.EntityFrameworkCore.Metadata.Builders;

namespace BanhaMVC.Data.ConfigurationClasses
{
    // act as configuration calss
    public class DepartmentConfigurations : IEntityTypeConfiguration<Department>
    {
        public void Configure(EntityTypeBuilder<Department> builder)
        {
            // to DB objects
            // tabel - view - schema - ... 
            builder.ToTable("departments");

            // Key
            builder.HasKey(D => D.Id);

            // Property
            builder.Property(d => d.Name)
                .HasMaxLength(100);

            // relationship
            // relation ship with Emp (in Emp Configuration)
        }
    }
}
