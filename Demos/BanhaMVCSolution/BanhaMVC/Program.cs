namespace BanhaMVC
{
    public class Program
    {
        // Contatainer Main method ?
        // entry Point !!
        // Console app : CLR execute (inside main)
        // Win Forms : start from this from
        // Web app : build web app with some configs

        // builder desugn Pattern : self
        public static void Main(string[] args)
        {
            var builder = WebApplication.CreateBuilder(args);

            // Add services to the container.
            builder.Services.AddControllersWithViews();

            var app = builder.Build();

            // Configure the HTTP request pipeline.
            if (!app.Environment.IsDevelopment())
            {
                app.UseExceptionHandler("/Home/Error");
            }
            app.UseStaticFiles();

            app.UseRouting();

            app.UseAuthorization();

            app.MapControllerRoute(
                name: "default",
                pattern: "{controller}/{action}/{id?}");

            app.Run();
        }
    }
}
