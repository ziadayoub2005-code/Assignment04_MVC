# 🎓 Assignment 04 — ASP.NET Core MVC & EF Core 8.0
### Full Student Controller Lifecycle, Advanced ViewModels, Async/Await & Self-Study

---

## 📌 معلومات الطالب والتكليف (Student & Assignment Info)
* **اسم الطالب (Student Name):** زياد محمد إمام محمود (Zeyad Mohamed Emam Mahmoud)
* **المحاضر (Instructor):** المهندس / عبدالرحمن شعبان الوكيل (Eng. Abdelrahman Shaaban Elwakeel)
* **المجموعة (Course Group):** DotNet With Elwakeel • Banha Group
* **بيئة العمل (Tech Stack):** .NET 8.0, ASP.NET Core MVC, EF Core 8.0, C# 12, Bootstrap 5

---

## 🚀 محتويات التكليف والحل الهندسي (Assignment Overview)

### 1️⃣ دورة حياة الـ Student Controller الكاملة (Task 1: Full Lifecycle)
تم تطبيق دورة حياة الأعمال الكاملة للـ `StudentController` اعتماداً على نموذج الفئات السابق تصميمه:
* **`GetAll()` / `Index`:**
  * ✅ **التقسيم لصفحات (Pagination):** أزرار ترقيم وتصفح ديناميكية مع الحفاظ على معايير البحث والفلترة.
  * ✅ **البحث بالاسم (Search by Name):** حقل بحث نصي للبحث الفوري عن الطلاب.
  * ✅ **الفلترة بالقسم (Filter by Department):** قائمة منسدلة لتصفية الطلاب بحسب القسم التابعين له.
* **`GetById()` / `Details`:**
  * ✅ عرض تفاصيل الطالب وقسمه التابع له عبر الـ Eager Loading، مع معالجة حالة `NotFound()`.
* **`Add` & `SaveAdd`:**
  * ✅ شاشة إضافة متوافقة مع الـ UX مع عرض **كافة الأقسام (All Departments)** داخل Dropdown للاختيار منها عبر `StudentWithDeptListViewModel`.
* **`Edit` & `SaveEdit`:**
  * ✅ شاشة تعديل متكاملة مع تحميل البيانات الأصلية وعرض كل الأقسام مع تحديد القسم الحالي تلقائياً.
* **`Delete` & `ConfirmDelete`:**
  * ✅ **Warning View:** عند الضغط على حذف، يتم التوجيه إجبارياً لشاشة تحذيرية حمراء واضحة تعرض بيانات الطالب وتطلب تأكيد الحذف منعاً للحذف الخطأ، ثم التنفيذ الفعلي عند التأكيد.
* **مرونة التشغيل (Offline Resiliency):**
  * ✅ طبقة `StudentBL` متصلة بـ `MsaooDbContext`، وفي حالة عدم توفر خادم SQL Server محلياً تعتمد على بيانات تجريبية (Mock Repository) لتظل كل الوظائف والشاشات تعمل بنسبة 100%.

---

### 2️⃣ حل الأسئلة المقالية والتقرير التخصصي (PDF Report)
تم حل وتوثيق جميع الأسئلة النظرية والمقالية داخل ملف **PDF هندسي متكامل (13 صفحة)**:
* 📄 **مسار الملف في المشروع:** [`Assignment/Assignment4_Answers.pdf`](./Assignment/Assignment4_Answers.pdf) أو في المسار الرئيسي [`Assignment4_Answers.pdf`](./Assignment4_Answers.pdf).

#### المحاور التي يغطيها ملف الـ PDF:
1. **Task 2: مقال لينكد إن التخصصي (LinkedIn Article):**
   * مقارنة شاملة وعملية بين **AutoMapper** و **Manual Mapping** ومكتبة **Mapster**.
   * ميزة الـ **Flattening** التلقائية، واستخدام `ProjectTo<T>()` مع EF Core لتحسين أداء استعلامات الـ SQL.
   * **Bonus Topic:** ثقافة استخدام الـ **HTTP Response Status Codes** (200, 201 Created, 204 NoContent, 400 BadRequest, 401 Unauthorized, 403 Forbidden, 404 NotFound, 500 InternalServerError).
   * نص البوست كامل وجاهز للنشر على LinkedIn.
2. **Task 3: الغرض والمعمارية العميقة لـ async و await:**
   * حل أزمة **مجاعة الخيوط (Thread Pool Starvation)** في تطبيقات الويب ذات الكثافة العالية.
   * مفهوم الـ **Non-blocking Asynchronous I/O** والـ IOCP/epoll على مستوى نظام التشغيل وكرت الشبكة.
   * المعمارية الداخلية لمترجم C# Roslyn Compiler وبناء الـ **State Machine** (`IAsyncStateMachine`).
   * القواعد الذهبية وأشهر الأخطاء الشائعة (تجنب `async void` والـ Deadlocks).
3. **Task 4: تقرير الدراسة الذاتية الشامل (Self-Study Report):**
   * **استراتيجيات تحميل البيانات في EF Core مقابل EF 6:** Eager Loading مع `AsSplitQuery()`، Explicit Loading، ومخاطر Lazy Loading والـ N+1 Query Problem ولماذا ألغت مايكروسوفت تفعيله افتراضياً في EF Core.
   * **نمط التصميم Builder Design Pattern:** فلسفة `WebApplication.CreateBuilder`، وفصل التكوين عن التشغيل، ومبدأ التجميد وثبات الحالة (Immutability).
   * **معمارية الـ Controller Factory:** كيف يتعرف الـ Framework على الكنترولر عبر `IControllerFactory` و `DefaultControllerFactory` و `IControllerActivator` ودورة حياة الكنترولر الكاملة.
   * **التجريد مقابل التخصيص:** المقارنة بين `IActionResult` و `ActionResult<T>`.

---

## 💻 طريقة تشغيل المشروع (How to Run)

1. فتح المشروع في **Visual Studio 2022** أو **VS Code**.
2. التحقق من مسار الاتصال في `MsaooDbContext.cs` (أو تشغيله مباشرة وسيتولى الـ Fallback توفير البيانات تلقائياً إن لم تكن قاعدة البيانات متصلة).
3. تشغيل المشروع عبر `Ctrl + F5` أو:
   ```bash
   cd Demos/BanhaMVCSolution/BanhaMVC
   dotnet run
   ```
4. التوجه في المتصفح إلى:
   * صفحة الطلاب: `https://localhost:XXXX/Student/GetAll`
   * أو الضغط على رابط **Students** في شريط التنقل العلوي (Navbar).
