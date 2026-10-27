# -*- coding: utf-8 -*-
import subprocess
import os
import shutil

HTML_CONTENT = r'''<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
<meta charset="utf-8">
<title>حل تكليف المحاضرة الرابعة: ASP.NET Core MVC &amp; EF Core 8.0</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;800;900&family=JetBrains+Mono:wght@400;500;600;700&family=Readex+Pro:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>
  :root {
    --primary: #0f172a;
    --primary-blue: #1e40af;
    --accent: #2563eb;
    --accent-light: #3b82f6;
    --accent-gold: #d97706;
    --text-dark: #0f172a;
    --text-muted: #475569;
    --bg-light: #f8fafc;
    --card-bg: #ffffff;
    --border: #cbd5e1;
    --border-light: #e2e8f0;
    --code-bg: #0b1329;
    --code-fg: #f1f5f9;
    --c-kw: #c084fc;
    --c-str: #86efac;
    --c-type: #38bdf8;
    --c-num: #fbbf24;
    --c-com: #94a3b8;
    --c-fn: #60a5fa;
    --success: #16a34a;
    --danger: #dc2626;
    --warning: #d97706;
  }

  @page {
    size: A4 portrait;
    margin: 12mm 14mm 14mm 14mm;
    @bottom-center {
      content: "DotNet With Elwakeel • Banha Group — Assignment 04 Solutions & Engineering Report";
      font-family: 'Cairo', sans-serif;
      font-size: 8pt;
      color: #94a3b8;
    }
    @bottom-left {
      content: counter(page);
      font-family: 'Cairo', sans-serif;
      font-size: 8pt;
      color: #1e40af;
      font-weight: bold;
    }
  }

  @page :first {
    margin: 0;
    @bottom-center { content: normal; }
    @bottom-left { content: normal; }
  }

  * { box-sizing: border-box; }
  body {
    margin: 0;
    padding: 0;
    font-family: 'Cairo', sans-serif;
    color: var(--text-dark);
    background: #ffffff;
    font-size: 10.2pt;
    line-height: 1.68;
    direction: rtl;
    text-align: right;
  }

  /* Cover Page */
  .cover {
    height: 100vh;
    padding: 60px 45px;
    background: linear-gradient(135deg, #090e1a 0%, #172554 50%, #1e1b4b 100%);
    color: #ffffff;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    page-break-after: always;
  }

  .cover-top {
    border-bottom: 2px solid rgba(255, 255, 255, 0.15);
    padding-bottom: 25px;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }

  .cover-badge {
    display: inline-block;
    padding: 6px 14px;
    background: rgba(37, 99, 235, 0.35);
    border: 1px solid rgba(147, 197, 253, 0.3);
    border-radius: 999px;
    font-size: 9pt;
    letter-spacing: 0.5px;
    color: #93c5fd;
    font-family: 'Readex Pro', sans-serif;
  }

  .cover-inst {
    font-size: 9.5pt;
    color: #cbd5e1;
  }

  .cover-title {
    font-family: 'Readex Pro', sans-serif;
    font-size: 26pt;
    font-weight: 700;
    line-height: 1.3;
    margin: 30px 0 15px;
    color: #ffffff;
  }

  .cover-subtitle {
    font-size: 13.5pt;
    color: #93c5fd;
    line-height: 1.6;
    max-width: 90%;
    margin-bottom: 30px;
  }

  .cover-meta {
    background: rgba(15, 23, 42, 0.65);
    border: 1px solid rgba(255, 255, 255, 0.15);
    border-radius: 12px;
    padding: 22px 26px;
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 16px;
  }

  .meta-item {
    display: flex;
    flex-direction: column;
  }

  .meta-label {
    font-size: 8.5pt;
    color: #94a3b8;
    margin-bottom: 3px;
  }

  .meta-val {
    font-size: 11pt;
    font-weight: 700;
    color: #ffffff;
  }

  /* Table of Contents */
  .toc-box {
    background: var(--bg-light);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 24px 28px;
    margin: 25px 0 35px;
    page-break-after: always;
  }

  .toc-title {
    font-family: 'Readex Pro', sans-serif;
    font-size: 16pt;
    font-weight: 700;
    color: var(--primary-blue);
    margin-bottom: 18px;
    border-bottom: 2px solid var(--accent);
    padding-bottom: 8px;
  }

  .toc-list {
    list-style: none;
    padding: 0;
    margin: 0;
  }

  .toc-item {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 10px 0;
    border-bottom: 1px dashed var(--border-light);
    font-size: 10pt;
  }

  .toc-num {
    background: var(--accent);
    color: white;
    width: 26px;
    height: 26px;
    border-radius: 50%;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    font-size: 9pt;
    font-weight: bold;
    margin-left: 12px;
    font-family: 'JetBrains Mono', monospace;
  }

  /* Chapter Headers */
  .chapter {
    page-break-before: always;
    margin-top: 10px;
  }

  .chapter-header {
    background: linear-gradient(90deg, #1e3a8a 0%, #2563eb 100%);
    color: white;
    padding: 14px 20px;
    border-radius: 8px;
    font-family: 'Readex Pro', sans-serif;
    font-size: 14pt;
    font-weight: 700;
    margin-bottom: 18px;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }

  .chapter-tag {
    background: rgba(255, 255, 255, 0.2);
    font-size: 8.5pt;
    padding: 3px 10px;
    border-radius: 6px;
    font-family: 'JetBrains Mono', monospace;
  }

  .sub-title {
    font-family: 'Readex Pro', sans-serif;
    font-size: 12pt;
    font-weight: 700;
    color: #1e3a8a;
    margin: 22px 0 10px;
    border-right: 4px solid var(--accent);
    padding-right: 10px;
  }

  .h3-title {
    font-family: 'Readex Pro', sans-serif;
    font-size: 10.5pt;
    font-weight: 600;
    color: #334155;
    margin: 16px 0 8px;
  }

  p {
    margin: 0 0 12px;
    text-align: justify;
  }

  /* Cards & Callouts */
  .callout {
    background: #f0fdf4;
    border-right: 4px solid var(--success);
    border-radius: 6px;
    padding: 12px 16px;
    margin: 14px 0;
    font-size: 9.8pt;
  }

  .callout-warn {
    background: #fffbeb;
    border-right: 4px solid var(--warning);
    border-radius: 6px;
    padding: 12px 16px;
    margin: 14px 0;
    font-size: 9.8pt;
  }

  .callout-info {
    background: #eff6ff;
    border-right: 4px solid var(--accent);
    border-radius: 6px;
    padding: 12px 16px;
    margin: 14px 0;
    font-size: 9.8pt;
  }

  .callout-danger {
    background: #fef2f2;
    border-right: 4px solid var(--danger);
    border-radius: 6px;
    padding: 12px 16px;
    margin: 14px 0;
    font-size: 9.8pt;
  }

  /* Tables */
  .data-table {
    width: 100%;
    border-collapse: collapse;
    margin: 16px 0;
    font-size: 9.2pt;
  }

  .data-table th {
    background: #1e293b;
    color: white;
    padding: 9px 12px;
    text-align: right;
    font-weight: 600;
    border: 1px solid #334155;
  }

  .data-table td {
    padding: 8px 12px;
    border: 1px solid var(--border);
    vertical-align: middle;
  }

  .data-table tr:nth-child(even) {
    background: #f8fafc;
  }

  /* Code Blocks */
  .code-container {
    background: var(--code-bg);
    border-radius: 8px;
    margin: 14px 0;
    overflow: hidden;
    border: 1px solid #1e293b;
    direction: ltr;
    text-align: left;
  }

  .code-title {
    background: #1e293b;
    color: #94a3b8;
    padding: 6px 14px;
    font-family: 'JetBrains Mono', monospace;
    font-size: 8pt;
    border-bottom: 1px solid #334155;
    display: flex;
    justify-content: space-between;
  }

  pre.code {
    margin: 0;
    padding: 12px 14px;
    font-family: 'JetBrains Mono', monospace;
    font-size: 8.4pt;
    line-height: 1.6;
    color: var(--code-fg);
    overflow-x: auto;
    white-space: pre-wrap;
    word-break: break-word;
  }

  .kw { color: var(--c-kw); font-weight: bold; }
  .tp { color: var(--c-type); font-weight: 600; }
  .str { color: var(--c-str); }
  .cm { color: var(--c-com); font-style: italic; }
  .num { color: var(--c-num); }
  .fn { color: var(--c-fn); }

  /* Badges */
  .badge {
    display: inline-block;
    padding: 2px 8px;
    border-radius: 4px;
    font-size: 8pt;
    font-weight: 600;
    font-family: 'JetBrains Mono', monospace;
  }

  .badge-primary { background: #dbeafe; color: #1e40af; }
  .badge-success { background: #dcfce7; color: #15803d; }
  .badge-warn { background: #fef3c7; color: #b45309; }
  .badge-danger { background: #fee2e2; color: #b91c1c; }
  .badge-dark { background: #e2e8f0; color: #334155; }

  /* Grid layout for cards */
  .grid2 {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 14px;
    margin: 14px 0;
  }

  .feature-card {
    background: #ffffff;
    border: 1px solid var(--border);
    border-radius: 8px;
    padding: 14px;
    box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05);
  }

  .feature-card h4 {
    margin: 0 0 6px;
    color: var(--primary-blue);
    font-size: 10.5pt;
  }

  .feature-card p {
    margin: 0;
    font-size: 9.2pt;
    color: var(--text-muted);
  }

  .inline-code {
    background: #f1f5f9;
    color: #0f172a;
    padding: 1px 5px;
    border-radius: 4px;
    font-family: 'JetBrains Mono', monospace;
    font-size: 8.5pt;
    direction: ltr;
    display: inline-block;
  }
</style>
</head>
<body>

<!-- ==================== COVER PAGE ==================== -->
<div class="cover">
  <div class="cover-top">
    <div class="cover-badge">Assignment 04 • ASP.NET Core MVC 8.0</div>
    <div class="cover-inst">Instructor: Eng. Abdelrahman Shaaban Elwakeel</div>
  </div>

  <div>
    <div class="cover-title">
      دليل الحل الهندسي والتطبيقي المتكامل<br>
      لتكليف المحاضرة الرابعة: Student Controller Lifecycle
    </div>
    <div class="cover-subtitle">
      تطبيق معمارية دورة الحياة الكاملة (CRUD)، البحث، الفلترة، التقسيم (Pagination)، ومقال لينكد إن التخصصي (AutoMapper &amp; HTTP Status Codes)، مع التحليل الهندسي المعمق للـ async/await وتقرير الـ Self-Study الشامل.
    </div>
  </div>

  <div class="cover-meta">
    <div class="meta-item">
      <span class="meta-label">اسم الطالب (Student Name):</span>
      <span class="meta-val">زياد محمد إمام محمود (Zeyad Mohamed Emam)</span>
    </div>
    <div class="meta-item">
      <span class="meta-label">المجموعة الدراسية (Course Group):</span>
      <span class="meta-val">DotNet With Elwakeel • Banha Group</span>
    </div>
    <div class="meta-item">
      <span class="meta-label">بيئة العمل والتطوير (Tech Stack):</span>
      <span class="meta-val">.NET 8.0 • EF Core 8.0 • C# 12 • Bootstrap 5</span>
    </div>
    <div class="meta-item">
      <span class="meta-label">تاريخ التسليم (Submission Date):</span>
      <span class="meta-val">أكتوبر 2026</span>
    </div>
  </div>
</div>

<!-- ==================== TABLE OF CONTENTS ==================== -->
<div class="toc-box">
  <div class="toc-title">فهرس المحتويات والمحاور الهندسية (Table of Contents)</div>
  <ul class="toc-list">
    <li class="toc-item">
      <span><strong>المحور الأول:</strong> دورة حياة الـ Student Controller الكاملة (Task 1: Full Business Lifecycle)</span>
      <span class="toc-num">1</span>
    </li>
    <li class="toc-item">
      <span><strong>المحور الثاني:</strong> مقال لينكد إن التخصصي (Task 2: LinkedIn Article: AutoMapper &amp; HTTP Status Codes)</span>
      <span class="toc-num">2</span>
    </li>
    <li class="toc-item">
      <span><strong>المحور الثالث:</strong> المعمارية العميقة للكلمات المفتاحية async و await (Task 3: Purpose of async/await)</span>
      <span class="toc-num">3</span>
    </li>
    <li class="toc-item">
      <span><strong>المحور الرابع:</strong> تقرير الدراسة الذاتية الشامل (Task 4: Self-Study Report - 4 Comprehensive Topics)</span>
      <span class="toc-num">4</span>
    </li>
    <li class="toc-item">
      <span><strong>المحور الخامس:</strong> استعراض الشفرة المصدرية وصفحات الـ Razor (Source Code &amp; Views Implementation)</span>
      <span class="toc-num">5</span>
    </li>
  </ul>
</div>

<!-- ==================== CHAPTER 1 ==================== -->
<div class="chapter">
  <div class="chapter-header">
    <span>1 — دورة حياة الـ Student Controller الكاملة (Task 1: Full Lifecycle)</span>
    <span class="chapter-tag">Task 1: Student Controller</span>
  </div>

  <p>
    المطلوب في التاسك الأول بناء دورة حياة الأعمال الكاملة <strong>(Full Business Life Cycle)</strong> للـ <strong>Student Controller</strong> معتمداً على نموذج الفئات السابق تصميمه، ومحققاً المتطلبات الهندسية الخمسة:
  </p>
  <ul>
    <li>توفير الأفعال الأساسية: <code>GetAll()</code>, <code>GetById()</code>, <code>Add</code>, <code>Edit</code>, <code>Delete</code>.</li>
    <li>عند إضافة أو تعديل طالب (Add / Edit) يلزم عرض كافة الأقسام <strong>(All Departments)</strong> داخل قائمة منسدلة <code>&lt;select&gt;</code> ليختار المستخدم منها بكل سهولة.</li>
    <li>عند طلب الحذف (Delete)، يتم التوجيه إجبارياً إلى صفحة تحذيرية <strong>(Warning View)</strong> تطلب التأكيد الصريح قبل المسح من قاعدة البيانات (لحماية تجربة المستخدم ومنع الحذف الخطأ).</li>
    <li>في صفحة العرض العام <code>GetAll</code>، تطبيق ثلاث خواص متقدمة: <strong>التقسيم لصفحات (Pagination)</strong>، <strong>البحث باسم الطالب (Search by name)</strong>، و<strong>الفلترة بحسب القسم (Filter by Department)</strong>.</li>
  </ul>

  <div class="sub-title">1.1 المعمارية الهندسية واستخدام الـ ViewModels</div>
  <p>
    من أهم القواعد البرمجية النظيفة التي تعلمناها مع البشمهندس عبدالرحمن الوكيل: <strong>عدم تمرير الـ Domain Entity مباشرة إلى الـ View عندما تحتاج الصفحة بيانات مركبة من أكثر من مصدر</strong>.
  </p>

  <div class="grid2">
    <div class="feature-card">
      <h4>1. StudentWithDeptListViewModel</h4>
      <p>
        يُستخدم في عمليتي <strong>Add</strong> و <strong>Edit</strong>. يحمل بيانات الطالب المطلوب إضافته أو تعديله (Name, Age, Address, DeptId) بالإضافة إلى قائمة <code>List&lt;Department&gt; DeptList</code> لتغذية عنصر الـ Dropdown.
      </p>
    </div>
    <div class="feature-card">
      <h4>2. StudentIndexViewModel</h4>
      <p>
        يُستخدم في عملية <strong>GetAll</strong>. يدمج قائمة الطلاب في الصفحة الحالية، وقائمة الأقسام، ومعايير الفلترة (Search, SelectedDeptId)، وبيانات ترقيم الصفحات (CurrentPage, TotalPages, TotalCount).
      </p>
    </div>
  </div>

  <div class="sub-title">1.2 جدول مسارات وأفعال الـ Student Controller ودورات الحياة</div>
  <table class="data-table">
    <thead>
      <tr>
        <th>Action Name</th>
        <th>HTTP Method</th>
        <th>المدخلات (Parameters)</th>
        <th>المسؤولية ودورة الحياة (Lifecycle Role)</th>
        <th>نوع النتيجة / View</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><code>GetAll / Index</code></td>
        <td><span class="badge badge-primary">GET</span></td>
        <td><code>search, deptId, page, pageSize</code></td>
        <td>استقبال معايير البحث والفلترة وتطبيق معادلة الـ Pagination، وإرجاع الـ ViewModel.</td>
        <td><code>View("GetAll", VM)</code></td>
      </tr>
      <tr>
        <td><code>GetById / Details</code></td>
        <td><span class="badge badge-primary">GET</span></td>
        <td><code>int id</code></td>
        <td>جلب بيانات الطالب بالـ ID مع بيانات قسمه (Eager Loading)، أو إرجاع <code>NotFound()</code>.</td>
        <td><code>View("Details", Student)</code></td>
      </tr>
      <tr>
        <td><code>Add</code></td>
        <td><span class="badge badge-primary">GET</span></td>
        <td>—</td>
        <td>الخطوة 1 للإضافة: فتح شاشة الإدخال فارغة ومحملة بكل الأقسام في القائمة المنسدلة.</td>
        <td><code>View("Add", VM)</code></td>
      </tr>
      <tr>
        <td><code>SaveAdd</code></td>
        <td><span class="badge badge-success">POST</span></td>
        <td><code>Student student</code></td>
        <td>الخطوة 2 للإضافة: استقبال البيانات عبر Model Binding، حفظها بقاعدة البيانات، ثم Redirect.</td>
        <td><code>RedirectToAction("GetAll")</code></td>
      </tr>
      <tr>
        <td><code>Edit</code></td>
        <td><span class="badge badge-primary">GET</span></td>
        <td><code>int id</code></td>
        <td>الخطوة 1 للتعديل: جلب السجل القديم وتعبئة الـ Dropdown مع تحديد قسم الطالب الحالي.</td>
        <td><code>View("Edit", VM)</code></td>
      </tr>
      <tr>
        <td><code>SaveEdit</code></td>
        <td><span class="badge badge-success">POST</span></td>
        <td><code>Student student, int id</code></td>
        <td>الخطوة 2 للتعديل: تحديث الحقول في الـ Context وحفظ التغييرات، ثم Redirect.</td>
        <td><code>RedirectToAction("GetAll")</code></td>
      </tr>
      <tr>
        <td><code>Delete</code></td>
        <td><span class="badge badge-warn">GET</span></td>
        <td><code>int id</code></td>
        <td><strong>Warning View:</strong> عرض كارت أحمر تحذيري ببيانات الطالب وسؤال المستخدم: هل أنت متأكد؟</td>
        <td><code>View("Delete", Student)</code></td>
      </tr>
      <tr>
        <td><code>ConfirmDelete</code></td>
        <td><span class="badge badge-danger">POST</span></td>
        <td><code>int id</code></td>
        <td>التنفيذ الفعلي: مسح الكيان من الـ DbSet ثم حفظ الـ Context، وإعادة التوجيه لـ GetAll.</td>
        <td><code>RedirectToAction("GetAll")</code></td>
      </tr>
    </tbody>
  </table>

  <div class="callout-info">
    <strong>ملاحظة هندسية حول الـ Resiliency (مرونة النظام):</strong> تم بناء طبقة <code>StudentBL</code> بحيث تحاول تنفيذ العمليات على قاعدة البيانات عبر <code>MsaooDbContext</code>، وفي حالة عدم توفر خادم SQL Server محلياً (كما هو الحال في بعض بيئات الاختبار أو الماك)، تعتمد تلقائياً على <strong>In-Memory Mock Repository</strong> لتظل الشاشات والوظائف تعمل بنسبة 100% بدون أي Crash.
  </div>
</div>

<!-- ==================== CHAPTER 2 ==================== -->
<div class="chapter">
  <div class="chapter-header">
    <span>2 — مقال لينكد إن التخصصي (Task 2: AutoMapper &amp; HTTP Status Codes)</span>
    <span class="chapter-tag">Task 2: LinkedIn Article</span>
  </div>

  <p>
    المطلوب في التاسك الثاني صياغة مقال تخصصي موجه لمجتمع المطورين على <strong>LinkedIn</strong> يناقش مكتبة <strong>AutoMapper</strong> وأهميتها في تسريع عملية التحويل بين الكيانات، مع تغطية القيمة المضافة <strong>(Bonus Plus)</strong> لأهمية ضبط واستخدام الـ <strong>HTTP Response Status Codes</strong> في بناء تطبيقات الويب والـ APIs الحديثة.
  </p>

  <div class="sub-title">2.1 نص المقال الجاهز للنشر المباشر على LinkedIn (باللغة العربية والإنجليزية المهنية)</div>

  <div class="callout">
    <strong>عنوان البوست المقترح:</strong> 🚀 رحلة المهندس بين Manual Mapping و AutoMapper.. ولماذا يجب أن تتوقف عن إرجاع 200 OK لكل شيء؟! 💡
  </div>

  <div class="code-container">
    <div class="code-title">LinkedIn Post Content (Ready to Copy &amp; Publish)</div>
    <pre class="code">عمرك عديت كم سطر كود كتبته في حياتك مجرد:
dto.Name = model.Name;
dto.Age = model.Age;
dto.Address = model.Address; ؟ 😅

في مشاريع الـ ASP.NET Core MVC و الـ Web APIs، دايماً بنفصل بين طبقة الـ Database (Domain Models) وبين البيانات اللي رايحة للـ Frontend (ViewModels أو DTOs) لحماية النظام (Security) ولتقليل استهلاك الـ Network.
لكن التحدي الأكبر اللي بيقابل المطور يومياً هو: إزاي ننقل البيانات بين الكائنين بأقل مجهود وبأعلى كفاءة؟

خلال تدريبنا العملي في كورس الـ MVC مع البشمهندس Abdelrahman Shaaban Elwakeel، ناقشنا بعمق موضوعين من أهم مهارات مهندس الـ Backend:

1️⃣ الحل السحري: AutoMapper vs Manual Mapping
📌 الـ Manual Mapping ميزته إنه Type-safe وسريع جداً في الـ Execution وواضح في الـ Debugging، لكن عيبه الأكبر إنه بيتحول لـ Boilerplate Code ممل ومستهلك للوقت، وممكن تنسى تعيّن خاصية جديدة ضفتها للـ Model!
📌 هنا بيجي دور AutoMapper:
بسطر واحد بنعرف الـ Mapping Profile، وبسطر واحد داخل الـ Controller أو الـ Service بنقول:
var studentVM = _mapper.Map&lt;StudentDetailsVM&gt;(student);

والأجمل من كده ميزة الـ Flattening:
لو عندك جوه الطالب Student.Department.Name، الـ AutoMapper ذكي كفاية إنه يربطها تلقائياً بـ Property اسمها DepartmentName داخل الـ ViewModel بدون أي Configuration إضافي!
💡 Pro Tip: مع EF Core استخدم دايماً `ProjectTo&lt;T&gt;()` علشان الـ SQL Query يتولد فيه فقط الأعمدة المطلوبة للـ DTO (SQL Projection) وماتسحبش كل أعمدة الجدول في الميموري!

2️⃣ القيمة المضافة (Bonus Plus): ثقافة الـ HTTP Response Status Codes 🚦
من أكبر الأخطاء الشائعة اللي بتفصل بين المطور المبتدئ والمحترف: إن الـ API يرجع دايماً Status 200 OK حتى لو حصل خطأ أو المورد مش موجود! 🤦‍♂️

الـ HTTP Status Codes هي لغة التفاهم العالمية بين السيرفر والمتصفح/الموبايل:
✅ 200 OK: لعمليات القراءة والتحديث الناجحة.
✅ 201 Created: لما تضيف مورد جديد (Add Student). الأصول الهندسية تقتضي إنك ترجع معاه Header اسمه Location فيه رابط المورد الجديد `CreatedAtAction`.
✅ 204 No Content: لما تنفذ عملية Delete أو Update ومش محتاج ترجع Data في الـ Body.
⚠️ 400 Bad Request: لما تكون المدخلات غير صحيحة أو الـ Model Validation يفشل.
🔒 401 Unauthorized: المستخدم مش عامل Login أصلاً (Missing Identity).
🚫 403 Forbidden: المستخدم مسجل لكن معندوش Role يسمحله بالحذف (Forbidden Access).
🔍 404 Not Found: الـ ID اللي طالبه مش موجود في قاعدة البيانات.
💥 500 Internal Server Error: حصل Exception غير متوقع في السيرفر.

استخدامك للـ Status Codes الصحيحة بيسهل حياة مهندسي الـ Frontend، بيخلي تطبيقك RESTful بامتياز، وبيخلي الـ Monitoring و الـ Logging Tools تشتغل بدقة متناهية.

سؤالي للمهندسين الزملاء:
في مشاريعك الحالية، بتفضل AutoMapper ولا Manual Mapping (أو مكتبات تانية زي Mapster)؟ وهل بتعتمد على Status Codes بدقة في مشاريعك؟ شاركوني تجاربكم في التعليقات! 👇

#DotNet #CSharp #ASPNETCore #MVC #WebAPI #CleanCode #AutoMapper #SoftwareEngineering #BackendDevelopment #Architecture</pre>
  </div>

  <div class="sub-title">2.2 جدول المقارنة الفنية: AutoMapper مقابل Manual Mapping مقابل Mapster</div>
  <table class="data-table">
    <thead>
      <tr>
        <th>المعيار الهيكلي</th>
        <th>Manual Mapping</th>
        <th>AutoMapper</th>
        <th>Mapster (البديل الحديث)</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>سرعة التنفيذ (Execution Speed)</strong></td>
        <td><span class="badge badge-success">الأسرع مطلقاً (0 overhead)</span></td>
        <td>سريع (يعتمد على IL Emitting بعد الـ Warmup)</td>
        <td><span class="badge badge-success">فائق السرعة (يقارب الـ Manual)</span></td>
      </tr>
      <tr>
        <td><strong>جهد الصيانة والـ Boilerplate</strong></td>
        <td><span class="badge badge-danger">مرتفع جداً (كتابة يدوية لكل حقل)</span></td>
        <td><span class="badge badge-success">منخفض جداً (سطر واحد)</span></td>
        <td><span class="badge badge-success">منخفض جداً</span></td>
      </tr>
      <tr>
        <td><strong>Compile-Time Safety</strong></td>
        <td><span class="badge badge-success">آمن 100% في وقت الترجمة</span></td>
        <td>يحتاج اختبارات <code>AssertConfigurationIsValid</code></td>
        <td>آمن عبر Code Generation</td>
      </tr>
      <tr>
        <td><strong>تكامل EF Core Projection</strong></td>
        <td>يدوي عبر <code>.Select(s =&gt; new ...)</code></td>
        <td><span class="badge badge-primary"><code>.ProjectTo&lt;VM&gt;()</code></span></td>
        <td><span class="badge badge-primary"><code>.ProjectToType&lt;VM&gt;()</code></span></td>
      </tr>
    </tbody>
  </table>
</div>

<!-- ==================== CHAPTER 3 ==================== -->
<div class="chapter">
  <div class="chapter-header">
    <span>3 — الغرض والمعمارية العميقة لـ async و await (Task 3: Async/Await Purpose)</span>
    <span class="chapter-tag">Task 3: Concurrency &amp; Async</span>
  </div>

  <p>
    المطلوب في التاسك الثالث الإجابة التفصيلية عن الغرض من الكلمات المفتاحية <strong><code>async</code></strong> و <strong><code>await</code></strong> في منصة .NET، وكيف تؤثر جذرياً على أداء وقابلية التوسع <strong>(Scalability)</strong> لتطبيقات الويب.
  </p>

  <div class="sub-title">3.1 الغرض الأساسي: حل أزمة مجاعة الخيوط (Thread Pool Starvation)</div>
  <p>
    في تطبيقات الـ Web التي تستقبل آلاف الطلبات المتزامنة (Concurrent Requests)، يخصص خادم الويب (مثل Kestrel أو IIS) خيط معالجة <strong>(Thread)</strong> من مخزن الخيوط <strong>(Thread Pool)</strong> لخدمة كل طلب قادم.
  </p>
  <p>
    إذا كان الكود تزامني <strong>Synchronous</strong>: عندما يستدعي التطبيق قاعدة البيانات لقراءة بيانات 1000 طالب عبر <code>_context.Students.ToList()</code>، فإن خيط المعالجة يدخل في حالة تجميد تام <strong>(Thread Blocked)</strong> لمدة 100-300 مللي ثانية في انتظار عودة الشبكة بالبيانات. خلال هذا الوقت، يستهلك الخيط ذاكرة (نحو 1 ميجابايت Stack Space) ولا يقدم أي فائدة حسابية للـ CPU!
  </p>

  <div class="callout-danger">
    <strong>سيناريو الانهيار (The Thread Pool Starvation Trap):</strong> إذا وصل 100 طلب متزامن وجميعها مجمدة في انتظار قواعد البيانات، تنفد خيوط الـ Thread Pool بالكامل. الطلبات الجديدة تبدأ بالتراكم في الطابور (Queue Delay)، مما يؤدي لارتفاع زمن الاستجابة (High Latency) وفي النهاية ظهور أخطاء <strong>HTTP 503 Service Unavailable</strong> وانهيار السيرفر.
  </div>

  <div class="sub-title">3.2 كيف تحل async و await هذه الكارثة؟ (Non-Blocking Asynchronous I/O)</div>
  <p>
    عند استخدام <code>await _context.Students.ToListAsync()</code>، يحدث ما يلي خطوة بخطوة:
  </p>
  <ol>
    <li>يرسل خيط المعالجة أمر القراءة إلى نظام التشغيل وكارت الشبكة عبر تقنية تسمى <strong>I/O Completion Ports (IOCP)</strong> في نظام Windows أو <strong>epoll</strong> في Linux.</li>
    <li>فور إرسال الأمر، <strong>يتحرر الخيط فوراً (Thread Released)</strong> ويعود إلى الـ Thread Pool ليخدم مستخدمين آخرين! لا يوجد أي خيط مجمد في الذاكرة.</li>
    <li>عندما تنتهي قاعدة البيانات وترسل حزم البيانات عبر الشبكة، يصدر كارت الشبكة إشارة مقاطعة للأجهزة (Hardware Interrupt)، ويقوم الـ OS بتنبيه مكتبة الـ Task Runtime.</li>
    <li>يقوم الـ Thread Pool باستدعاء أي خيط متاح لاستكمال بقية الكود (Continuation) من النقطة التي توقف عندها بعد الـ <code>await</code>!</li>
  </ol>

  <div class="sub-title">3.3 السحر الداخلي لمترجم C# (Under the Hood: The State Machine)</div>
  <p>
    الكلمات <code>async</code> و <code>await</code> ليست مجرد سكر تركيبي (Syntactic Sugar)، بل هي تعليمة مباشرة لمترجم <strong>Roslyn Compiler</strong> لإعادة تشكيل الدالة بالكامل!
  </p>
  <p>
    يقوم المترجم بإنشاء هيكل خفي <strong>(Hidden Struct / Class)</strong> يطبق الواجهة <code>IAsyncStateMachine</code>، ويقسم الدالة الأصلية إلى حالات مرقمة (State 0, State 1, State -1). عند الوصول لأمر <code>await</code>:
  </p>
  <ul>
    <li>إذا كانت المهمة مكتملة بالفعل، يكمل الكود سيره دون مغادرة الخيط (Fast Path).</li>
    <li>إذا كانت المهمة غير مكتملة، يسجل الكود دالة الإكمال (Awaiter Callback)، ويغير رقم الحالة (State)، ثم يخرج فوراً مفسحاً المجال للخيط!</li>
  </ul>

  <div class="code-container">
    <div class="code-title">C# Async/Await vs Compiler State Machine Representation</div>
    <pre class="code"><span class="cm">// الكود المكتوب بواسطة المطور:</span>
<span class="kw">public async</span> <span class="tp">Task</span>&lt;<span class="tp">IActionResult</span>&gt; <span class="fn">GetAll</span>()
{
    <span class="kw">var</span> data = <span class="kw">await</span> _studentBL.<span class="fn">GetAllAsync</span>();
    <span class="kw">return</span> <span class="fn">View</span>(data);
}

<span class="cm">// ما يولده المترجم تحت الغطاء (مفهوم مبسط للـ State Machine):</span>
[<span class="tp">CompilerGenerated</span>]
<span class="kw">struct</span> <span class="tp">&lt;GetAll&gt;d__0</span> : <span class="tp">IAsyncStateMachine</span>
{
    <span class="kw">public int</span> &lt;&gt;1__state;
    <span class="kw">public</span> <span class="tp">AsyncTaskMethodBuilder</span>&lt;<span class="tp">IActionResult</span>&gt; &lt;&gt;t__builder;
    <span class="kw">private</span> <span class="tp">TaskAwaiter</span>&lt;<span class="tp">List</span>&lt;<span class="tp">Student</span>&gt;&gt; &lt;&gt;u__1;

    <span class="kw">public void</span> <span class="fn">MoveNext</span>()
    {
        <span class="cm">// التبديل بين الحالات وإدارة دورة حياة الـ Task</span>
    }
}</pre>
  </div>

  <div class="sub-title">3.4 القواعد الذهبية وأشهر الأخطاء الشائعة (Golden Rules &amp; Anti-Patterns)</div>
  <table class="data-table">
    <thead>
      <tr>
        <th>الممارسة الخاطئة (Anti-Pattern)</th>
        <th>الممارسة الصحيحة (Best Practice)</th>
        <th>السبب الهندسي</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><code>public async void DoWork()</code></td>
        <td><code>public async Task DoWorkAsync()</code></td>
        <td>دوال <code>async void</code> تمنع التقاط الـ Exceptions وتؤدي لانهيار العملية (Crash). تُستخدم فقط في UI Events.</td>
      </tr>
      <tr>
        <td>استخدام <code>task.Result</code> أو <code>task.Wait()</code></td>
        <td>استخدام <code>await task</code> دائماً</td>
        <td>خلط الـ Sync مع الـ Async يسبب تجميد خيوط المعالجة وحدوث <strong>Deadlocks</strong> خطيرة.</td>
      </tr>
      <tr>
        <td>تطبيق <code>Task.Run()</code> لعمليات DB I/O</td>
        <td>استخدام دوال I/O الأصلية كـ <code>ToListAsync()</code></td>
        <td><code>Task.Run()</code> يحجز خيطاً إضافياً من الـ Pool بلا داعٍ لعملية I/O لا تحتاج معالجة حسابية.</td>
      </tr>
      <tr>
        <td>إهمال الـ <code>CancellationToken</code></td>
        <td>تمرير <code>cancellationToken</code> لجميع دوال EF</td>
        <td>لو أغلق المستخدم المتصفح، يتم إلغاء كويري قاعدة البيانات فوراً وتوفير موارد السيرفر.</td>
      </tr>
    </tbody>
  </table>
</div>

<!-- ==================== CHAPTER 4 ==================== -->
<div class="chapter">
  <div class="chapter-header">
    <span>4 — تقرير الدراسة الذاتية الشامل (Task 4: Self-Study Report)</span>
    <span class="chapter-tag">Task 4: Self Study</span>
  </div>

  <p>
    المطلوب في التاسك الرابع إعداد تقرير دراسة ذاتية <strong>(Self-Study Report)</strong> شامل يغطي أهم الموضوعات الهندسية التي طرحها البشمهندس عبدالرحمن الوكيل خلال المحاضرة وفي تعليقات الأكواد:
  </p>

  <div class="sub-title">4.1 استراتيجيات تحميل البيانات في EF Core مقابل EF 6 (Loading Strategies)</div>
  <p>
    في تطبيقات الـ ORM، تمثل إدارة العلاقات بين الجداول (مثل علاقة الطالب بالقسم) أحد أخطر عوامل تحديد أداء واستقرار النظام. توجد ثلاث استراتيجيات رئيسية:
  </p>

  <div class="grid2">
    <div class="feature-card">
      <h4>1. التحميل المسبق المباشر (Eager Loading)</h4>
      <p>
        جلب الكيان الأصلي والكيانات المرتبطة به في نفس استعلام الـ SQL أو عبر استعلامات متزامنة باستخدام دالتي <code>.Include()</code> و <code>.ThenInclude()</code>.
        <br><strong>الميزة:</strong> رحلة واحدة للشبكة وتفادي مشكلة الـ N+1 Queries.
        <br><strong>في EF Core:</strong> تدعم تقنية <code>AsSplitQuery()</code> لمنع انفجار البيانات الناتج عن الـ Cartesian Explosion في جداول الـ Many-to-Many!
      </p>
    </div>

    <div class="feature-card">
      <h4>2. التحميل الصريح المنضبط (Explicit Loading)</h4>
      <p>
        جلب الكيان الأصلي أولاً، ثم في مرحلة لاحقة وبأمر برمجي صريح من المطور يتم طلب تحميل العلاقة باستخدام <code>context.Entry(entity).Reference(...).Load()</code> للعلاقات الفردية أو <code>Collection(...).Load()</code> للمجموعات.
        <br><strong>الميزة:</strong> تحكم دقيق جداً في توقيت وحجم البيانات المحملة وفقاً لشروط منطق الأعمال.
      </p>
    </div>
  </div>

  <div class="feature-card" style="margin-top: 10px;">
    <h4>3. التحميل الكسول التلقائي (Lazy Loading): الفرق التاريخي بين EF 6 و EF Core</h4>
    <p>
      في <strong>EF 6 (قبل Core)</strong>، كان الـ Lazy Loading هو السلوك الافتراضي بمجرد وضع كلمة <code>virtual</code> على الـ Navigation Property. كان هذا السلوك يتسبب في كارثة الأداء الشهيرة <strong>(The N+1 Query Problem)</strong>: إذا قرأت 100 طالب في لوب وعرضت اسم قسم كل طالب، يرسل السيرفر استعلاماً واحداً لجلب الطلاب ثم 100 استعلام منفصل إضافي لجلب أقسامهم!
      <br>
      لذلك، في <strong>EF Core (بعد Core)</strong>، قرر مهندسو مايكروسوفت <strong>إلغاء تفعيل الـ Lazy Loading افتراضياً</strong>. وإذا أراد المطور تفعيله، يجب عليه تثبيت حزمة مستقلة <code>Microsoft.EntityFrameworkCore.Proxies</code> واستدعاء <code>UseLazyLoadingProxies()</code> صراحة، مما يجبر المهندس على التفكير الواعي في استراتيجية استعلاماته.
    </p>
  </div>

  <div class="sub-title">4.2 نمط التصميم Builder Design Pattern في معمارية .NET 8 الحديثة</div>
  <p>
    عند الانتقال من .NET Core القديم إلى .NET 6 و .NET 8، تساءل الجميع عن سر تبسيط كود الـ <code>Program.cs</code> واستخدام:
    <br><code class="inline-code">var builder = WebApplication.CreateBuilder(args);</code>
    <br><code class="inline-code">var app = builder.Build();</code>
  </p>
  <p>
    السبب هو التطبيق المباشر لنمط التصميم الشهير <strong>Builder Design Pattern</strong> (أحد أنماط الـ Creational Patterns من عصابة الـ GoF):
  </p>
  <ul>
    <li><strong>فصل مرحلة التكوين (Configuration) عن مرحلة التشغيل (Runtime Execution):</strong> يسمح الـ Builder بإضافة خدمات الـ Dependency Injection داخل <code>builder.Services</code>، وضبط إعدادات الـ Logging والـ Configuration بكل مرونة وبشكل تدريجي.</li>
    <li><strong>مبدأ التجميد وثبات الحالة (Immutability):</strong> بمجرد استدعاء دالة <code>builder.Build()</code>، يتم بناء حاوية الخدمات النهائية (Service Provider) وتجميدها تماماً. لا يمكن لأي كود لاحق إضافة أو حذف خدمات أثناء تشغيل الـ Web Application، مما يحمي النظام من أخطاء الـ Thread-Safety والـ Race Conditions.</li>
    <li><strong>بناء خط الأنابيب (Middleware Pipeline):</strong> كائن <code>app</code> الناتج يتولى فقط ضبط مسارات الطلبات وترتيب الـ Middlewares مثل <code>app.UseRouting()</code> و <code>app.UseAuthorization()</code> ثم بدء الاستماع للطلبات عبر <code>app.Run()</code>.</li>
  </ul>

  <div class="sub-title">4.3 معمارية الـ Controller Factory ودورة حياة الكنترولر في ASP.NET Core MVC</div>
  <p>
    عندما يطلب المتصفح مساراً مثل <code>/Student/GetAll</code>، كيف يفهم الـ Framework هذا الطلب وكيف يُنشئ كائن الـ Controller؟
  </p>
  <ol>
    <li><strong>Routing Middleware:</strong> يقوم بمطابقة الـ URL مع قوالب التوجيه المسجلة واستخراج اسم الـ Controller (وهو "Student") واسم الـ Action (وهو "GetAll").</li>
    <li><strong>مصنع الكنترولر (IControllerFactory):</strong> المكون الافتراضي المسجل في النظام هو <code>DefaultControllerFactory</code>. يقوم هذا المصنع بفحص الـ Assembly للعثور على الفئة المناسبة بناءً على الشروط القياسية: (أن تنتهي بكلمة Controller، ترث من Controller، وتكون فئة عامة Public وغير مجردة وغير Generic).</li>
    <li><strong>منشط الكنترولر (IControllerActivator):</strong> يقوم بإنشاء نسخة فعلية (Instance) من الكنترولر، وسحب كافة الـ Dependencies المطلوبة من حاوية الـ Dependency Injection وتمريرها في الـ Constructor (Constructor Injection).</li>
    <li><strong>تنفيذ الـ Action:</strong> يقوم الـ Model Binder باستخراج المدخلات، وتعمل الـ Action Filters، ثم يتم تنفيذ دالة الـ Action.</li>
    <li><strong>التخلص من الكائن (Disposal):</strong> عند اكتمال الـ Response، يقوم الـ Controller Factory باستدعاء <code>ReleaseController</code>، فإذا كان الكنترولر يطبق <code>IDisposable</code> أو <code>IAsyncDisposable</code>، يتم التخلص منه ومن موارده فوراً من الذاكرة لضمان عدم حدوث تسريب ذاكرة (Memory Leak).</li>
  </ol>

  <div class="sub-title">4.4 التجريد مقابل التخصيص: المقارنة بين IActionResult و ActionResult&lt;T&gt;</div>
  <p>
    في بدايات الـ MVC، كان المطور يعيد أنواعاً محددة (Concrete Types) مثل <code>ViewResult</code> أو <code>JsonResult</code>. ولكن في التطبيقات الحديثة:
  </p>
  <ul>
    <li><strong>واجهة IActionResult:</strong> تمثل أقصى درجات التجريد (Abstraction). تسمح للـ Action بإرجاع ردود مختلفة بحسب مسار منطق الأعمال (مثل إرجاع <code>View()</code> إذا وُجد الطالب، أو إرجاع <code>NotFound()</code> إذا كان الـ ID خطأ، أو إرجاع <code>Content()</code>).</li>
    <li><strong>النوع ActionResult&lt;T&gt;:</strong> تم تقديمه في ASP.NET Core 2.1 خصيصاً لخدمة الـ Web APIs و Swagger/OpenAPI. يسمح بتوفير مرونة الـ <code>IActionResult</code> مع الحفاظ على الـ Strong-Typing للنوع المرجع <code>T</code> ليتمكن الـ Documentation Generator والـ Frontend Client من معرفة شكل الـ Data Model بدقة.</li>
  </ul>
</div>

<!-- ==================== CHAPTER 5 ==================== -->
<div class="chapter">
  <div class="chapter-header">
    <span>5 — الشفرة المصدرية المطبقة وصفحات الـ Razor (Source Code Implementation)</span>
    <span class="chapter-tag">Implementation Showcase</span>
  </div>

  <p>
    تم تطبيق الحل الكامل داخل المشروع بمساراته النموذجية وفقاً لأحدث ممارسات ASP.NET Core 8.0:
  </p>

  <div class="sub-title">5.1 كود الـ Controller الأساسي (Controllers/StudentController.cs)</div>
  <div class="code-container">
    <div class="code-title">Controllers/StudentController.cs</div>
    <pre class="code"><span class="kw">public class</span> <span class="tp">StudentController</span> : <span class="tp">Controller</span>
{
    <span class="kw">private readonly</span> <span class="tp">StudentBL</span> studentBL = <span class="kw">new</span> <span class="tp">StudentBL</span>();
    <span class="kw">private readonly</span> <span class="tp">DepBL</span> depBL = <span class="kw">new</span> <span class="tp">DepBL</span>();

    <span class="cm">// 1- GetAll مع Pagination والبحث والفلترة</span>
    <span class="kw">public</span> <span class="tp">IActionResult</span> <span class="fn">GetAll</span>(<span class="kw">string</span>? search, <span class="kw">int</span>? deptId, <span class="kw">int</span> page = <span class="num">1</span>, <span class="kw">int</span> pageSize = <span class="num">4</span>)
    {
        <span class="kw">int</span> totalCount;
        <span class="kw">var</span> students = studentBL.<span class="fn">GetFiltered</span>(search, deptId, page, pageSize, <span class="kw">out</span> totalCount);
        <span class="kw">var</span> depts = depBL.<span class="fn">GetAll</span>();
        <span class="kw">var</span> totalPages = (<span class="kw">int</span>)<span class="tp">Math</span>.<span class="fn">Ceiling</span>((<span class="kw">double</span>)totalCount / pageSize);

        <span class="kw">var</span> viewModel = <span class="kw">new</span> <span class="tp">StudentIndexViewModel</span>
        {
            Students = students,
            DeptList = depts,
            Search = search,
            SelectedDeptId = deptId,
            CurrentPage = page,
            PageSize = pageSize,
            TotalCount = totalCount,
            TotalPages = totalPages &lt; <span class="num">1</span> ? <span class="num">1</span> : totalPages
        };
        <span class="kw">return</span> <span class="fn">View</span>(<span class="str">"GetAll"</span>, viewModel);
    }

    <span class="cm">// 2- GetById / Details</span>
    <span class="kw">public</span> <span class="tp">IActionResult</span> <span class="fn">GetById</span>(<span class="kw">int</span> id)
    {
        <span class="kw">var</span> student = studentBL.<span class="fn">GetById</span>(id);
        <span class="kw">if</span> (student == <span class="kw">null</span>) <span class="kw">return</span> <span class="fn">NotFound</span>();
        <span class="kw">return</span> <span class="fn">View</span>(<span class="str">"Details"</span>, student);
    }

    <span class="cm">// 3- Add: تحميل الأقسام للـ Dropdown</span>
    [<span class="tp">HttpGet</span>]
    <span class="kw">public</span> <span class="tp">IActionResult</span> <span class="fn">Add</span>()
    {
        <span class="kw">var</span> vm = <span class="kw">new</span> <span class="tp">StudentWithDeptListViewModel</span> { DeptList = depBL.<span class="fn">GetAll</span>() };
        <span class="kw">return</span> <span class="fn">View</span>(<span class="str">"Add"</span>, vm);
    }

    [<span class="tp">HttpPost</span>]
    <span class="kw">public</span> <span class="tp">IActionResult</span> <span class="fn">SaveAdd</span>(<span class="tp">Student</span> student)
    {
        <span class="kw">if</span> (!<span class="kw">string</span>.<span class="fn">IsNullOrWhiteSpace</span>(student.Name))
        {
            studentBL.<span class="fn">Add</span>(student);
            <span class="kw">return</span> <span class="fn">RedirectToAction</span>(<span class="kw">nameof</span>(GetAll));
        }
        <span class="kw">return</span> <span class="fn">View</span>(<span class="str">"Add"</span>, <span class="kw">new</span> <span class="tp">StudentWithDeptListViewModel</span> { DeptList = depBL.<span class="fn">GetAll</span>() });
    }

    <span class="cm">// 4- Edit: تحميل بيانات الطالب والأقسام</span>
    [<span class="tp">HttpGet</span>]
    <span class="kw">public</span> <span class="tp">IActionResult</span> <span class="fn">Edit</span>(<span class="kw">int</span> id)
    {
        <span class="kw">var</span> student = studentBL.<span class="fn">GetById</span>(id);
        <span class="kw">if</span> (student == <span class="kw">null</span>) <span class="kw">return</span> <span class="fn">NotFound</span>();
        <span class="kw">var</span> vm = <span class="kw">new</span> <span class="tp">StudentWithDeptListViewModel</span>
        {
            Id = student.Id, Name = student.Name, Age = student.Age,
            Address = student.Address, DeptId = student.DeptId, DeptList = depBL.<span class="fn">GetAll</span>()
        };
        <span class="kw">return</span> <span class="fn">View</span>(<span class="str">"Edit"</span>, vm);
    }

    [<span class="tp">HttpPost</span>]
    <span class="kw">public</span> <span class="tp">IActionResult</span> <span class="fn">SaveEdit</span>(<span class="tp">Student</span> student, <span class="kw">int</span> id)
    {
        <span class="kw">if</span> (!<span class="kw">string</span>.<span class="fn">IsNullOrWhiteSpace</span>(student.Name))
        {
            studentBL.<span class="fn">Update</span>(id, student);
            <span class="kw">return</span> <span class="fn">RedirectToAction</span>(<span class="kw">nameof</span>(GetAll));
        }
        <span class="kw">return</span> <span class="fn">View</span>(<span class="str">"Edit"</span>, student);
    }

    <span class="cm">// 5- Delete: التوجيه لصفحة التحذير ثم التأكيد</span>
    [<span class="tp">HttpGet</span>]
    <span class="kw">public</span> <span class="tp">IActionResult</span> <span class="fn">Delete</span>(<span class="kw">int</span> id)
    {
        <span class="kw">var</span> student = studentBL.<span class="fn">GetById</span>(id);
        <span class="kw">if</span> (student == <span class="kw">null</span>) <span class="kw">return</span> <span class="fn">NotFound</span>();
        <span class="kw">return</span> <span class="fn">View</span>(<span class="str">"Delete"</span>, student); <span class="cm">// Warning View</span>
    }

    [<span class="tp">HttpPost</span>]
    <span class="kw">public</span> <span class="tp">IActionResult</span> <span class="fn">ConfirmDelete</span>(<span class="kw">int</span> id)
    {
        studentBL.<span class="fn">Delete</span>(id);
        <span class="kw">return</span> <span class="fn">RedirectToAction</span>(<span class="kw">nameof</span>(GetAll));
    }
}</pre>
  </div>

  <div class="sub-title">5.2 كود صفحة العرض العام والفلترة (Views/Student/GetAll.cshtml)</div>
  <div class="code-container">
    <div class="code-title">Views/Student/GetAll.cshtml (Excerpt)</div>
    <pre class="code">@model StudentIndexViewModel

&lt;form method="get" action="/Student/GetAll" class="row g-3 align-items-end mb-4"&gt;
    &lt;!-- Search Input --&gt;
    &lt;div class="col-md-5"&gt;
        &lt;label class="form-label fw-bold"&gt;Search by Name&lt;/label&gt;
        &lt;input type="text" name="search" value="@Model.Search" class="form-control" placeholder="Search student name..." /&gt;
    &lt;/div&gt;

    &lt;!-- Department Filter Dropdown --&gt;
    &lt;div class="col-md-4"&gt;
        &lt;label class="form-label fw-bold"&gt;Filter by Department&lt;/label&gt;
        &lt;select name="deptId" class="form-select"&gt;
            &lt;option value=""&gt;-- All Departments --&lt;/option&gt;
            @foreach (var dept in Model.DeptList)
            {
                &lt;option value="@dept.Id" selected="@(dept.Id == Model.SelectedDeptId)"&gt;@dept.Name&lt;/option&gt;
            }
        &lt;/select&gt;
    &lt;/div&gt;

    &lt;div class="col-md-3 d-flex gap-2"&gt;
        &lt;button type="submit" class="btn btn-primary flex-grow-1"&gt;Filter&lt;/button&gt;
        &lt;a href="/Student/GetAll" class="btn btn-outline-secondary"&gt;Reset&lt;/a&gt;
    &lt;/div&gt;
&lt;/form&gt;

&lt;!-- Pagination Bar --&gt;
&lt;ul class="pagination"&gt;
    &lt;li class="page-item @(!Model.HasPreviousPage ? "disabled" : "")"&gt;
        &lt;a class="page-link" href="/Student/GetAll?search=@Model.Search&deptId=@Model.SelectedDeptId&page=@(Model.CurrentPage - 1)"&gt;Previous&lt;/a&gt;
    &lt;/li&gt;
    @for (int p = 1; p &lt;= Model.TotalPages; p++)
    {
        &lt;li class="page-item @(p == Model.CurrentPage ? "active" : "")"&gt;
            &lt;a class="page-link" href="/Student/GetAll?search=@Model.Search&deptId=@Model.SelectedDeptId&page=@p"&gt;@p&lt;/a&gt;
        &lt;/li&gt;
    }
    &lt;li class="page-item @(!Model.HasNextPage ? "disabled" : "")"&gt;
        &lt;a class="page-link" href="/Student/GetAll?search=@Model.Search&deptId=@Model.SelectedDeptId&page=@(Model.CurrentPage + 1)"&gt;Next&lt;/a&gt;
    &lt;/li&gt;
&lt;/ul&gt;</pre>
  </div>

  <div class="callout">
    <strong>خلاصة التقييم والتسليم:</strong> تم بحمد الله وتوفيقه استيفاء كافة متطلبات التكليف الرابع (Assignment 04) وفق أعلى المعايير الهندسية النظيفة، وتوثيق كافة الأسئلة المقالية والتقرير التخصصي داخل هذا المستند الشامل ليكون مرجعاً هندسياً متكاملاً.
  </div>
</div>

</body>
</html>
'''

def main():
    base_dir = "/Users/mac/Desktop/BanhaMVC04/Assignment"
    html_path = os.path.join(base_dir, "Assignment4_Answers.html")
    pdf_path = os.path.join(base_dir, "Assignment4_Answers.pdf")
    
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(HTML_CONTENT)
    print(f"HTML saved to {html_path}")
    
    chrome_cmd = [
        "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
        "--headless",
        "--disable-gpu",
        "--no-pdf-header-footer",
        f"--print-to-pdf={pdf_path}",
        f"file://{html_path}"
    ]
    
    print("Running Chrome to generate PDF...")
    result = subprocess.run(chrome_cmd, capture_output=True, text=True)
    print("Chrome return code:", result.returncode)
    if os.path.exists(pdf_path):
        size_kb = os.path.getsize(pdf_path) / 1024
        print(f"PDF generated successfully at {pdf_path} ({size_kb:.1f} KB)")
        
        # Also copy to root workspace so user sees it right away
        root_pdf_path = "/Users/mac/Desktop/BanhaMVC04/Assignment4_Answers.pdf"
        shutil.copyfile(pdf_path, root_pdf_path)
        print(f"Copied PDF to root: {root_pdf_path}")
    else:
        print("PDF generation failed! Stderr:", result.stderr)

if __name__ == "__main__":
    main()
