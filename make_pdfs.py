import os
import subprocess
from pygments import highlight
from pygments.lexers import JavaLexer
from pygments.formatters import HtmlFormatter

CHROME_PATH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
BASE_DIR = r"C:\Users\pc\Desktop\se217-oop-lab"

pygments_style = HtmlFormatter(style='friendly', linenos=True, cssclass='syntax-highlight').get_style_defs('.syntax-highlight')

BASE_TEMPLATE = """<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>{title}</title>
<style>
@page {{
  size: A4;
  margin: 12mm 14mm 12mm 14mm;
}}
@media print {{
  body {{
    -webkit-print-color-adjust: exact;
    print-color-adjust: exact;
  }}
  .page-break {{
    page-break-before: always;
  }}
  .avoid-break {{
    page-break-inside: avoid;
  }}
}}
body {{
  font-family: 'Segoe UI', -apple-system, BlinkMacSystemFont, Roboto, Helvetica, Arial, sans-serif;
  color: #1e293b;
  line-height: 1.45;
  font-size: 9.5pt;
  margin: 0;
  padding: 0;
}}
.header {{
  border-bottom: 2.5px solid #0284c7;
  padding-bottom: 10px;
  margin-bottom: 12px;
}}
.univ-name {{
  font-size: 14pt;
  font-weight: 800;
  color: #0369a1;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  margin: 0;
}}
.dept-name {{
  font-size: 10pt;
  font-weight: 600;
  color: #0f172a;
  margin: 2px 0 0 0;
}}
.report-title {{
  font-size: 12pt;
  font-weight: 700;
  color: #0284c7;
  margin-top: 6px;
  margin-bottom: 0;
}}
.student-box {{
  background: #f8fafc;
  border: 1px solid #e2e8f0;
  border-left: 4px solid #0284c7;
  border-radius: 6px;
  padding: 8px 14px;
  margin-bottom: 12px;
}}
.student-table {{
  width: 100%;
  border-collapse: collapse;
  font-size: 9pt;
}}
.student-table td {{
  padding: 2.5px 6px;
}}
.student-table td.label {{
  font-weight: 700;
  color: #334155;
  width: 16%;
}}
.student-table td.val {{
  color: #0f172a;
}}
.student-table a {{
  color: #0284c7;
  text-decoration: none;
}}
.section-title {{
  font-size: 10.5pt;
  font-weight: 700;
  color: #0f172a;
  border-bottom: 1.5px solid #cbd5e1;
  padding-bottom: 3px;
  margin-top: 10px;
  margin-bottom: 6px;
}}
p.desc {{
  margin: 4px 0 8px 0;
  color: #334155;
  font-size: 9pt;
}}
.code-card {{
  border: 1px solid #cbd5e1;
  border-radius: 5px;
  overflow: hidden;
  margin-bottom: 10px;
  page-break-inside: avoid;
}}
.code-header {{
  background: #f1f5f9;
  padding: 5px 12px;
  font-family: 'Consolas', monospace;
  font-size: 8.5pt;
  font-weight: 700;
  color: #334155;
  border-bottom: 1px solid #cbd5e1;
  display: flex;
  justify-content: space-between;
}}
.syntax-highlight {{
  font-size: 8pt;
  line-height: 1.35;
  padding: 6px 8px;
  background: #ffffff;
  margin: 0;
  overflow-x: auto;
}}
.syntax-highlight pre {{
  margin: 0;
  font-family: 'Consolas', 'Courier New', monospace;
}}
.terminal {{
  background: #0f172a;
  border-radius: 6px;
  padding: 10px 14px;
  font-family: 'Consolas', 'Courier New', monospace;
  font-size: 8.5pt;
  line-height: 1.4;
  color: #f8fafc;
  margin-bottom: 10px;
  page-break-inside: avoid;
}}
.terminal-bar {{
  display: flex;
  align-items: center;
  gap: 5px;
  margin-bottom: 8px;
  padding-bottom: 5px;
  border-bottom: 1px solid #1e293b;
}}
.dot {{
  width: 9px;
  height: 9px;
  border-radius: 50%;
  display: inline-block;
}}
.dot-red {{ background: #ef4444; }}
.dot-yellow {{ background: #f59e0b; }}
.dot-green {{ background: #10b981; }}
.term-title {{
  font-size: 7.5pt;
  color: #94a3b8;
  margin-left: 8px;
}}
.cmd {{
  color: #38bdf8;
  font-weight: bold;
}}
.out {{
  color: #4ade80;
}}
.out-std {{
  color: #e2e8f0;
}}
.viva-box {{
  background: #eff6ff;
  border: 1px solid #bfdbfe;
  border-radius: 5px;
  padding: 8px 12px;
  margin-top: 8px;
  font-size: 8.5pt;
  color: #1e3a8a;
  page-break-inside: avoid;
}}
.viva-box b {{
  color: #1d4ed8;
}}
.footer {{
  border-top: 1px solid #e2e8f0;
  padding-top: 4px;
  margin-top: 10px;
  font-size: 7.5pt;
  color: #94a3b8;
  text-align: center;
}}
{pygments_css}
</style>
</head>
<body>
<div class="header">
  <div class="univ-name">Daffodil International University</div>
  <div class="dept-name">Department of Software Engineering &bull; Faculty of Science & Information Technology</div>
  <div class="report-title">{title}</div>
</div>

<div class="student-box">
  <table class="student-table">
    <tr>
      <td class="label">Student Name:</td>
      <td class="val"><strong>Faiaz ul Islam</strong></td>
      <td class="label">Student ID:</td>
      <td class="val"><strong>252-35-597</strong></td>
    </tr>
    <tr>
      <td class="label">Course Title:</td>
      <td class="val">SE 217 &ndash; Object Oriented Programming Lab</td>
      <td class="label">Section:</td>
      <td class="val"><strong>45-H2</strong></td>
    </tr>
    <tr>
      <td class="label">Semester:</td>
      <td class="val">Fall 2026</td>
      <td class="label">GitHub Repo:</td>
      <td class="val"><a href="https://github.com/FaiazEnd/se217-oop-lab">github.com/FaiazEnd/se217-oop-lab</a></td>
    </tr>
  </table>
</div>

{content}

<div class="footer">
  SE 217: Object Oriented Programming Lab &bull; Student ID: 252-35-597 &bull; Daffodil International University
</div>
</body>
</html>
"""

def highlight_java(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        code = f.read()
    formatter = HtmlFormatter(style='friendly', linenos=True, cssclass='syntax-highlight')
    return highlight(code, JavaLexer(), formatter)

def render_html_to_pdf(html_path, pdf_path):
    cmd = [
        CHROME_PATH,
        "--headless=new",
        "--disable-gpu",
        "--no-pdf-header-footer",
        f"--print-to-pdf={pdf_path}",
        html_path
    ]
    res = subprocess.run(cmd, capture_output=True, text=True)
    if os.path.exists(pdf_path):
        print(f"Successfully created: {pdf_path} ({os.path.getsize(pdf_path)} bytes)")
    else:
        print(f"Failed to create: {pdf_path}\nError: {res.stderr}")

def generate_week01():
    code1 = highlight_java(os.path.join(BASE_DIR, "Week01_597", "FoodItem.java"))
    code2 = highlight_java(os.path.join(BASE_DIR, "Week01_597", "FoodItemDemo.java"))
    
    content = f"""
<div class="section-title">1. Problem Scenario & Task Description</div>
<p class="desc">
  The campus canteen wants a Java program to track food items on the shelf. Each food item possesses a <code>name</code> (String), <code>price</code> (int, taka per piece), and <code>quantity</code> (int, pieces in stock).
  The goal is to model <code>FoodItem</code> with methods <code>stockValue()</code>, <code>printLine()</code>, and an optional <code>sell(int amount)</code> transaction method.
  <code>FoodItemDemo</code> creates three objects (Khichuri, Tea, Samosa), prints individual summaries, total stock valuation, and demonstrates inventory sales.
</p>

<div class="section-title">2. Source Code Listings</div>
<div class="code-card">
  <div class="code-header">
    <span>File: FoodItem.java</span>
    <span>Entity Class</span>
  </div>
  {code1}
</div>

<div class="code-card">
  <div class="code-header">
    <span>File: FoodItemDemo.java</span>
    <span>Driver Class</span>
  </div>
  {code2}
</div>

<div class="section-title">3. Execution Output & Verification</div>
<div class="terminal">
  <div class="terminal-bar">
    <span class="dot dot-red"></span>
    <span class="dot dot-yellow"></span>
    <span class="dot dot-green"></span>
    <span class="term-title">Terminal &mdash; bash &mdash; javac Week01_597/*.java &amp;&amp; java -cp Week01_597 FoodItemDemo</span>
  </div>
  <div class="cmd">$ javac FoodItem.java FoodItemDemo.java</div>
  <div class="cmd">$ java FoodItemDemo</div>
  <div class="out">Khichuri | Tk 90 | Qty 12 | Value 1080</div>
  <div class="out">Tea | Tk 15 | Qty 40 | Value 600</div>
  <div class="out">Samosa | Tk 10 | Qty 25 | Value 250</div>
  <div class="out-std">Total stock value: Tk 1930</div>
  <div class="out">Sold 5 Tea</div>
  <div class="out-std">Not enough Samosa in stock</div>
  <div class="out">Tea | Tk 15 | Qty 35 | Value 525</div>
</div>

<div class="viva-box">
  <b>Lab Assessment &amp; Viva Discussion:</b><br>
  &bull; <b>Object Instantiation:</b> <code>FoodItem khichuri = new FoodItem();</code> dynamically allocates state memory on the heap, with reference pointer <code>khichuri</code> stored on the thread stack.<br>
  &bull; <b>State Isolation:</b> Each object maintains independent copies of instance fields (e.g., <code>khichuri.price</code> vs <code>tea.price</code>).<br>
  &bull; <b>Calculation Delegation:</b> <code>stockValue()</code> encapsulates the arithmetic rule (<code>price * quantity</code>), reused by both <code>printLine()</code> and total value aggregation.
</div>
"""
    html = BASE_TEMPLATE.format(
        title="Lab Performance Task Report &mdash; Week 01: Canteen Stock Report",
        pygments_css=pygments_style,
        content=content
    )
    html_file = os.path.join(BASE_DIR, "week01_report.html")
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(html)
    
    # Save in root and in Week01_597 folder
    pdf_root = os.path.join(BASE_DIR, "Week01_252-35-597.pdf")
    pdf_week = os.path.join(BASE_DIR, "Week01_597", "Week01_252-35-597.pdf")
    render_html_to_pdf(html_file, pdf_root)
    render_html_to_pdf(html_file, pdf_week)
    os.remove(html_file)

def generate_week03():
    code1 = highlight_java(os.path.join(BASE_DIR, "week3", "BusTrip.java"))
    code2 = highlight_java(os.path.join(BASE_DIR, "week3", "BusCounter.java"))
    
    content = f"""
<div class="section-title">1. Problem Scenario & Task Description</div>
<p class="desc">
  The university transport office operates commuter bus routes connecting Dhaka city with Daffodil Smart City (DSC).
  This system models trips using <code>BusTrip</code> with private encapsulated attributes (<code>tripCode</code>, <code>route</code>, <code>fare</code>, <code>capacity</code>, <code>seatsLeft</code>) and a static trip counter generating codes (<code>BT-201</code>, <code>BT-202</code>...).
  <code>BusCounter</code> performs batch seat bookings, tests reference aliasing (<code>busy = trips[3]</code>), aggregates revenue, determines the trip with maximum vacancies, and includes the optional <code>findByRoute()</code> search query.
</p>

<div class="section-title">2. Source Code Listings</div>
<div class="code-card">
  <div class="code-header">
    <span>File: BusTrip.java</span>
    <span>Encapsulated Entity Class</span>
  </div>
  {code1}
</div>

<div class="code-card">
  <div class="code-header">
    <span>File: BusCounter.java</span>
    <span>Driver &amp; Booking Management Class</span>
  </div>
  {code2}
</div>

<div class="section-title">3. Execution Output & Verification</div>
<div class="terminal">
  <div class="terminal-bar">
    <span class="dot dot-red"></span>
    <span class="dot dot-yellow"></span>
    <span class="dot dot-green"></span>
    <span class="term-title">Terminal &mdash; bash &mdash; javac week3/*.java &amp;&amp; java -cp week3 BusCounter</span>
  </div>
  <div class="cmd">$ javac BusTrip.java BusCounter.java</div>
  <div class="cmd">$ java BusCounter</div>
  <div class="out-std">Trips created: 4</div>
  <div class="out-std">Booking failed for Uttara-DSC</div>
  <div class="out">BT-201  Mirpur-DSC   Tk  50  seats left: 18</div>
  <div class="out">BT-202  Uttara-DSC   Tk  40  seats left: 25</div>
  <div class="out">BT-203  Gabtoli-DSC  Tk  35  seats left: 32</div>
  <div class="out">BT-204  Savar-DSC    Tk  30  seats left:  0</div>
  <div class="out-std">Total revenue: Tk 1480</div>
  <div class="out-std">Most seats left: Gabtoli-DSC</div>
  <div class="out-std">trips[3] seats left: 0</div>
  <div class="out">BT-202  Uttara-DSC   Tk  40  seats left: 25</div>
  <div class="out-std">No such route: Banani-DSC</div>
</div>

<div class="viva-box">
  <b>Lab Assessment &amp; Viva Discussion:</b><br>
  &bull; <b>Constructor Chaining:</b> <code>this(route, fare, 40);</code> routes two-argument instantiation to the canonical 3-argument constructor, ensuring zero code duplication and uniform code generation.<br>
  &bull; <b>Static Variables:</b> <code>tripCount</code> is allocated in class metadata space, shared across all instances to safely generate sequential trip codes (BT-201, BT-202, etc.).<br>
  &bull; <b>Reference Aliasing Step:</b> <code>BusTrip busy = trips[3];</code> copies the heap memory reference address. Mutating <code>busy.bookSeats(20)</code> directly mutates the state observable through <code>trips[3]</code>.
</div>
"""
    html = BASE_TEMPLATE.format(
        title="Lab Performance Task Report &mdash; Week 03: Campus Bus Booking",
        pygments_css=pygments_style,
        content=content
    )
    html_file = os.path.join(BASE_DIR, "week03_report.html")
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(html)
    
    pdf_root1 = os.path.join(BASE_DIR, "Week03_252-35-597.pdf")
    pdf_root2 = os.path.join(BASE_DIR, "Week3_252-35-597.pdf")
    pdf_week = os.path.join(BASE_DIR, "week3", "Week03_252-35-597.pdf")
    render_html_to_pdf(html_file, pdf_root1)
    render_html_to_pdf(html_file, pdf_root2)
    render_html_to_pdf(html_file, pdf_week)
    os.remove(html_file)

def generate_week04():
    code1 = highlight_java(os.path.join(BASE_DIR, "week4", "week4_597.java"))
    
    content = f"""
<div class="section-title">1. Problem Scenario & Task Description</div>
<p class="desc">
  A class teacher requires an automated console tool to collect and evaluate examination records for 5 students.
  The program models <code>Student</code> (with <code>id</code>, <code>name</code>, <code>marks</code>, and <code>display()</code>) and executes via driver class <code>week4_597</code>.
  It dynamically instantiates an array of 5 Student objects, captures interactive console input using <code>Scanner</code> (handling leftover newline tokens), displays the class roster, determines the top scorer, computes class average, identifies the lowest student, and counts students above average.
</p>

<div class="section-title">2. Source Code Listing</div>
<div class="code-card">
  <div class="code-header">
    <span>File: week4_597.java</span>
    <span>Entity &amp; Driver Implementation (Week4_YourID standard)</span>
  </div>
  {code1}
</div>

<div class="section-title">3. Execution Output & Verification</div>
<div class="terminal">
  <div class="terminal-bar">
    <span class="dot dot-red"></span>
    <span class="dot dot-yellow"></span>
    <span class="dot dot-green"></span>
    <span class="term-title">Terminal &mdash; bash &mdash; javac week4/week4_597.java &amp;&amp; java -cp week4 week4_597</span>
  </div>
  <div class="cmd">$ javac week4_597.java</div>
  <div class="cmd">$ java week4_597</div>
  <div class="out-std">Enter information for Student 1 &rarr; ID: 101, Name: Nila, Marks: 78.5</div>
  <div class="out-std">Enter information for Student 2 &rarr; ID: 102, Name: Rafi, Marks: 85.0</div>
  <div class="out-std">Enter information for Student 3 &rarr; ID: 103, Name: Mim, Marks: 92.5</div>
  <div class="out-std">Enter information for Student 4 &rarr; ID: 104, Name: Tanvir, Marks: 64.0</div>
  <div class="out-std">Enter information for Student 5 &rarr; ID: 105, Name: Sadia, Marks: 81.0</div>
  <br>
  <div class="out-std">===== Student Information =====</div>
  <div class="out">ID: 101, Name: Nila, Marks: 78.5</div>
  <div class="out">ID: 102, Name: Rafi, Marks: 85.0</div>
  <div class="out">ID: 103, Name: Mim, Marks: 92.5</div>
  <div class="out">ID: 104, Name: Tanvir, Marks: 64.0</div>
  <div class="out">ID: 105, Name: Sadia, Marks: 81.0</div>
  <br>
  <div class="out-std">===== Top Student =====</div>
  <div class="out">ID: 103, Name: Mim, Marks: 92.5</div>
  <br>
  <div class="out-std">Average Marks: 80.2</div>
  <br>
  <div class="out-std">===== Lowest Student (Optional) =====</div>
  <div class="out">ID: 104, Name: Tanvir, Marks: 64.0</div>
  <div class="out-std">Students above average: 3</div>
</div>

<div class="viva-box">
  <b>Lab Assessment &amp; Viva Discussion:</b><br>
  &bull; <b>Array Allocation vs Object Construction:</b> <code>new Student[5]</code> creates an array of 5 <code>null</code> reference slots. Each slot must be initialized with <code>new Student()</code> in a loop to avoid <code>NullPointerException</code>.<br>
  &bull; <b>Scanner Input Stream Buffer Clearing:</b> <code>scanner.nextInt()</code> reads the integer but leaves the trailing newline <code>\\n</code> in the buffer. Calling <code>scanner.nextLine()</code> flushes this residual newline so subsequent string reads are captured cleanly.<br>
  &bull; <b>Extrema Finding:</b> Initializes <code>topStudent = students[0]</code> and iterates through the array in $O(n)$ time to identify the peak score.
</div>
"""
    html = BASE_TEMPLATE.format(
        title="Lab Performance Task Report &mdash; Week 04: Result Manager",
        pygments_css=pygments_style,
        content=content
    )
    html_file = os.path.join(BASE_DIR, "week04_report.html")
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(html)
    
    pdf_root1 = os.path.join(BASE_DIR, "Week04_252-35-597.pdf")
    pdf_root2 = os.path.join(BASE_DIR, "Week4_252-35-597.pdf")
    pdf_week = os.path.join(BASE_DIR, "week4", "Week4_252-35-597.pdf")
    render_html_to_pdf(html_file, pdf_root1)
    render_html_to_pdf(html_file, pdf_root2)
    render_html_to_pdf(html_file, pdf_week)
    os.remove(html_file)

def generate_week05():
    code1 = highlight_java(os.path.join(BASE_DIR, "Week05", "Student.java"))
    code2 = highlight_java(os.path.join(BASE_DIR, "Week05", "StudentDemo.java"))
    
    content = f"""
<div class="section-title">1. Problem Scenario & Task Description</div>
<p class="desc">
  This module focuses on the fundamental Object-Oriented principle of <strong>Encapsulation</strong> and defensive programming.
  By declaring internal state variables as <code>private</code> and providing controlled access via public getters and setters with validation rules, the system ensures that objects cannot be manipulated into an invalid state.
  The <code>Student</code> class validates that marks are strictly within the range of <code>0</code> to <code>100</code>.
</p>

<div class="section-title">2. Source Code Listings</div>
<div class="code-card">
  <div class="code-header">
    <span>File: Student.java</span>
    <span>Encapsulated Entity with Validation Constraints</span>
  </div>
  {code1}
</div>

<div class="code-card">
  <div class="code-header">
    <span>File: StudentDemo.java</span>
    <span>Driver &amp; Validation Boundary Verification</span>
  </div>
  {code2}
</div>

<div class="section-title">3. Execution Output & Verification</div>
<div class="terminal">
  <div class="terminal-bar">
    <span class="dot dot-red"></span>
    <span class="dot dot-yellow"></span>
    <span class="dot dot-green"></span>
    <span class="term-title">Terminal &mdash; bash &mdash; javac Week05/*.java &amp;&amp; java -cp Week05 StudentDemo</span>
  </div>
  <div class="cmd">$ javac Student.java StudentDemo.java</div>
  <div class="cmd">$ java StudentDemo</div>
  <div class="out">Student ID: 597</div>
  <div class="out">Name: Faiaz ul Islam</div>
  <div class="out">Marks: 88.5</div>
  <br>
  <div class="out-std">--- Testing Validation ---</div>
  <div class="out-std" style="color: #f87171;">Invalid marks! Marks must be between 0 and 100.</div>
  <div class="out">Updated Marks: 95.0</div>
</div>

<div class="viva-box">
  <b>Lab Assessment &amp; Viva Discussion:</b><br>
  &bull; <b>Data Hiding &amp; Invariant Defense:</b> Declaring <code>private double marks;</code> prevents external code from directly executing invalid assignments such as <code>s.marks = 150</code> or <code>s.marks = -10</code>.<br>
  &bull; <b>Constructor Guarding:</b> Initializing marks inside constructor via <code>setMarks(marks)</code> guarantees that even initial object creation adheres to domain constraints.<br>
  &bull; <b>Getter/Setter Decoupling:</b> Public accessors provide a clean abstraction barrier, allowing internal representation changes without breaking client code.
</div>
"""
    html = BASE_TEMPLATE.format(
        title="Lab Performance Task Report &mdash; Week 05: Encapsulation &amp; Validation",
        pygments_css=pygments_style,
        content=content
    )
    html_file = os.path.join(BASE_DIR, "week05_report.html")
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(html)
    
    pdf_root1 = os.path.join(BASE_DIR, "Week05_252-35-597.pdf")
    pdf_root2 = os.path.join(BASE_DIR, "Week5_252-35-597.pdf")
    pdf_week = os.path.join(BASE_DIR, "Week05", "Week05_252-35-597.pdf")
    render_html_to_pdf(html_file, pdf_root1)
    render_html_to_pdf(html_file, pdf_root2)
    render_html_to_pdf(html_file, pdf_week)
    os.remove(html_file)

if __name__ == "__main__":
    print("Generating Week 01 PDF...")
    generate_week01()
    print("Generating Week 03 PDF...")
    generate_week03()
    print("Generating Week 04 PDF...")
    generate_week04()
    print("Generating Week 05 PDF...")
    generate_week05()
    print("All PDFs successfully generated!")
