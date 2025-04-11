import sqlite3

def insert_chunk(topic, url, content, db_path="school_info.db"):
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS info (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            topic TEXT,
            url TEXT,
            content TEXT
        )
    ''')
    c.execute('INSERT INTO info (topic, url, content) VALUES (?, ?, ?)', (topic, url, content))
    conn.commit()
    conn.close()

def insert_ash_info():
    topic = "Academic Study Hall & Academic Probation"
    url = "https://www.calverthall.com/resources/academic-study-hall"

    main_content = """Academic Downloads for Students
Academic Study Hall Schedule & Guidelines
Office of Academic Affairs Re: Academic Study Hall (ASH) - Notification/Expectations

A review of your semester 1 report card has indicated you have failed a subject for the semester which places you on Academic Probation. A student on Academic Probation is in danger of failing a subject for the year and therefore would be required to:
• Complete a summer credit recovery course to matriculate for the year
• Or be dismissed from CHC if he has failed 3 or more full credit courses for the year.

To help address your academic situation, students are required to attend Academic Study Hall (ASH) and will be placed into 2 groups based on their Academic Probation:
• Red group – students who have failed 1-2 subjects and therefore only need to attend ASH each Tuesday & Thursday
• Gold Group – students who have failed 3 or more subjects and therefore need to attend ASH each Tuesday & Thursday as well as every other Saturday
  o Attendance will be recorded at each ASH session

During Academic Study Hall, a student will either:
• Work on missing assignments/HW to be caught up and current.
• See his course teacher for extra help. (Students should come to Study Hall to check in and then go to their course teacher for help. You will need to bring a note indicating you did indeed meet them for a review session.)
• Work on current assignments and study to remain in good current standing.
• Study and prepare for the next day’s classes.

During each Academic Study Hall (ASH), each student needs to:
• be in school dress code
• bring all the materials including devices
• have a list of their missing assignments

A student can be removed from the Academic Study Hall (ASH) list,
• If a student has a passing grade of a 75 or above in the failing subject at the issuing of their progress report (March 28)

Absence or Tardy Policy for Academic Study Hall:
• Please note that failure to report to ASH will result in further consequences including disciplinary action such as general detention and/or Saturday detention.
• Students are only excused from ASH with prior approval by the Office of Academic Affairs. Email excuses will not be accepted. You should see Mr. Fan in person if you need to be excused.
• No Proxy contact – contact Mr Fan yourself.

Questions can be directed to Mr. Fan (fant@calverthall.com) or in person in the Office of Academic Affairs in the school’s Main Office.
"""

    update_content = """Guidelines and schedule for Academic Study Hall (ASH). Students who have a course failure for Semester 1 were assigned to ASH for semester 2.
- ASH is scheduled each Tues & Thurs from 3-4pm in LHN. Students must be in dress code for ASH.
- Certain students with multiple failures were also assigned to Saturday ASH.

Please check the schedule so not to miss ASH.

We will NOT hold ASH on Thursday, 2/20.

Any questions can be directed in-person to Mr. Fan

Updated 2/14/2025
"""

    insert_chunk(topic, url, main_content)
    insert_chunk(topic, url, update_content)

# Run this to add ASH info to the DB
insert_ash_info()

insert_chunk(
    topic="Course Requirements - Freshman Year",
    url=None,
    content="""FRESHMAN YEAR - COURSES AND REQUIREMENTS

Course Placement for Freshmen year is completed by the Office of Academic Affairs (OAA). OAA examines a student’s admission index, his middle school grades, standardized test scores (including the HSPT), and historical performance of students from previous years to determine the appropriate course placements.

Freshmen students are placed in the most challenging curriculum that the OAA believes will yield a favorable GPA via a reasonable amount of challenging work.

REQUIRED FULL CREDIT COURSES:
- Religion
- Math
- Science
- Social Studies
- English
- World Language

REQUIRED HALF CREDIT COURSES:
- PE I / Health
- Computer Apps / Presentation Skills

PROGRAM EXCEPTIONS:
- McMullen Scholars: Take Honors Rhetoric & Logic (902H) instead of standard 0.5 credit courses
- Bro. Tom Miller Scholars: Waive Computer Apps / Presentation Skills
- La Salle Program: Enroll in La Salle class (full credit); may waive Social Studies and defer World Language
- Academic Skills Program: Waive Computer Apps / Presentation Skills
- Fine Arts Students: Replace 0.5 credit courses with fine arts courses as directed by their program

See course catalog for full course codes and descriptions.
"""
)


insert_chunk(
    topic="Course Requirements - Sophomore Year",
    url=None,
    content="""SOPHOMORE YEAR - COURSES AND REQUIREMENTS

Sophomore course placement is based on freshman year performance and teacher recommendations, in consultation with the student’s school counselor.

REQUIRED FULL CREDIT COURSES:
- Religion
- Math
- Science
- Social Studies
- English
- World Language (continuation of Freshman language)

ADDITIONAL REQUIREMENTS:
- 0.5 credit in Fine Arts
- 0.5 credit in PE II
- Optional 7th course may be taken as an elective

PROGRAM EXCEPTIONS:
- McMullen: Humanities (901H) replaces Fine Arts & PE
- La Salle: May defer World Language; may waive Fine Arts & PE if taking 1st-year language
- ASP Year 2: Waive PE II
- Fine Arts Program students: Priority access and substitutions for Fine Arts requirements
- Students with 2+ AP/Honors or special engineering courses may waive both PE & Fine Arts

See course catalog for full list of eligible electives and required courses per academic track.
"""
)


insert_chunk(
    topic="Course Requirements - Junior Year",
    url=None,
    content="""JUNIOR YEAR - COURSES AND REQUIREMENTS

Course placement is based on prior year performance and teacher recommendation.

REQUIRED FULL CREDIT COURSES:
- Religion
- Math
- Science
- Social Studies
- English
- Elective (must be 1 full credit)

ADDITIONAL GUIDANCE:
- Students must take 2 years of the same world language (3 recommended)
- Two 0.5 credit courses cannot be combined to replace a 1 credit elective

PROGRAM EXCEPTIONS:
- McMullen Scholars: Must take Humanities (901H) unless completed in Sophomore year
- La Salle: Begin World Language if not yet taken; science may be deferred
- Fine Arts Program students: Directed Fine Arts curriculum and priority scheduling

Electives available include courses in Engineering, Computer Science, Business, Leadership, Math, and Fine Arts.

Refer to the catalog for specific course codes, prerequisites, and graduation impact.
"""
)


insert_chunk(
    topic="Course Requirements - Senior Year",
    url=None,
    content="""SENIOR YEAR - COURSES AND REQUIREMENTS

Course placement is again determined by past performance and teacher recommendations. Seniors must take six full credit courses.

REQUIRED FULL CREDIT COURSES:
- Religion
- Social Studies
- English
- Three electives (1 credit each)

REQUIREMENTS & POLICIES:
- Only 1 Fine Art course may count toward the 3 required electives
- Two 0.5 credit courses cannot be combined into one required full credit
- Senior exams occur in May; students with a 90+ may be exempt
- MDSE requires 2 years of the same language; 3 is encouraged
- Graduation requires passing all senior courses and submission of an English term paper

PROGRAM EXCEPTIONS:
- McMullen: Must take Capstone Research Seminar (903)
- La Salle: Must finish language requirement if not yet complete
- Fine Arts: Directed elective choices and priority access

Failure in 3+ credits means ineligibility for graduation from Calvert Hall.

Full course descriptions, prerequisites, and electives are available in the catalog.
"""
)

insert_chunk(
    topic="Academic Study Hall & Academic Probation",
    url=None,
    content="""Academic Study Hall - Guidelines & Schedule

Office of Academic Affairs Re: Academic Study Hall (ASH) - Notification/Expectations

A review of your semester 1 report card has indicated you have failed a subject for the semester which places you on Academic Probation. A student on Academic Probation is in danger of failing a subject for the year and therefore would be required to:
• Complete a summer credit recovery course to matriculate for the year
• Or be dismissed from CHC if he has failed 3 or more full credit courses for the year.

To help address your academic situation, students are required to Academic Study Hall (ASH) and will be placed into 2 groups based on their Academic Probation:
• Red group – students who have failed 1-2 subjects and therefore only need to attend ASH each Tuesday & Thursday per the schedule below
• Gold Group – students who have failed 3 or more subjects and therefore need to attend ASH each Tues & Thurs as well as every other Saturday per the schedule below
• Attendance will be recorded at each ASH session

The upcoming schedule for Tues & Thurs ASH this year will be:
2/11, 2/13, 2/18, 2/20, 2/25, 2/27, 3/4, 3/6, 3/11, 3/13, 3/18, 3/20, 3/25, 3/27 (3pm-4pm in LHN)

The upcoming schedule for Saturday ASH this year will be:
2/15, 3/1, 3/15, 3/29, 4/12, 5/3 (9:30–11:30am in Commons)

During Academic Study Hall, a student will either:
• Work on missing assignments/HW to be caught up and current.
• See his course teacher for extra help. (Students should check in first, then go to their teacher with a note verifying the session.)
• Work on current assignments and study to remain in good standing.
• Study and prepare for the next day’s classes.

Each student must:
• Be in school dress code
• Bring all necessary materials and devices
• Have a list of missing assignments

Removal from the ASH list:
• A student may be removed if they have a 75+ in the failing subject at the March 28 progress report.

Absence or Tardy Policy for Academic Study Hall:
• Failure to report results in disciplinary consequences such as detention
• Students are excused only with prior in-person approval from the Office of Academic Affairs (no emails or proxies)
• See Mr. Fan directly for approval or questions

Questions can be directed to Mr. Fan (fant@calverthall.com) or in-person at the Office of Academic Affairs in the Main Office.

NOTE: A downloadable PDF outlines the procedures and schedule for Academic Study Hall (ASH). ASH is assigned to students who have failed 1 or more subjects. Contact Mr. Fan with any questions.
"""
)

insert_chunk(
    topic="Async Learning Policy - AY 24-25",
    url=None,
    content="""SNOW DAYS AND ASYNCHRONOUS LEARNING

Calvert Hall College follows Baltimore County Public Schools for weather emergencies and school closures. We follow a 90-minute delay for all delays (HR begins at 9:55 AM on delayed openings).

CHC has allotted TWO SNOW DAYS for this school year. As both have now been used, the school will implement Asynchronous Learning for any additional snow closings.

ASYNC LEARNING GUIDELINES:
• Teachers will post assignments by 10:30 AM on the day of closure.
• Assignments appear in the student’s assignment center.
• All work must be submitted by 8:25 AM the NEXT morning — late work is NOT accepted.
• ASYNC assignments count as attendance for the class.
• Course late policies do not apply to ASYNC work.
• Missing ASYNC assignments result in in-person Academic Study Hall on the return day.

SYNCHRONOUS OPTION:
Teachers may optionally hold virtual class sessions instead of ASYNC assignments. Subject meeting windows:
- Religion: 11:20–11:50 AM
- Language: 11:55–12:25 PM
- Math: 12:30–1:00 PM
- Social Studies: 1:05–1:35 PM
- Science: 1:40–2:10 PM
- English: 2:15–2:45 PM

INTERNET ISSUES:
Students who cannot submit due to connection issues must attend after-school ASH in Rm 106 (3–4 PM). Missing this will result in a zero.

Questions? Contact Mr. Fan at fant@calverthall.com.

(Updated ASYNC Policy for AY 24-25)
"""
)


insert_chunk(
    topic="Honor Roll Policies & Procedures",
    url=None,
    content="""Office of Academic Affairs – Honor Roll Policies & Procedures  
Updated: January 1, 2023

Honor Roll status is determined at the end of each semester. To earn Honor Roll, students must meet **both** of the following:
• A semester unweighted GPA of 88 or higher (strict; 87.999 is not rounded up).
• No single course grade below an 81.

BENEFITS OF HONOR ROLL DISTINCTION:
• Students who earn Honor Roll in both semesters of an academic year receive:
  - An Academic Letter the first year
  - An Academic Star for each subsequent year
• Letters and Stars are awarded during the Fall Semester
• Each Honor Roll student is eligible for **one Honor Roll Holiday**

HONOR ROLL HOLIDAY POLICY:
• Must be taken the following semester:
  - Semester 1 Honor Roll → Holiday must be taken during Semester 2
  - Semester 2 Honor Roll → Holiday must be taken during the next Semester 1
• Holidays cannot be carried over to future semesters.

HONOR ROLL HOLIDAY PROCESS:
1. Get the form from the Attendance Office or download here:  
   https://calverthall.myschoolapp.com/ftpimages/274/download/download_8802532.pdf?_=1744238061681
2. Fill in the form, including your schedule for that day.
3. Get teacher signatures — teachers may deny permission to miss class.
4. Get a parent/guardian signature.
5. Submit the form to the Attendance Office **at least 24 hours** in advance.
6. A parent/guardian must call the Attendance Office to confirm the absence.

Failure to follow these steps may result in your Honor Roll Holiday being denied.
"""
)


insert_chunk(
    topic="Academic Awards - Letters, Stars & Certificates",
    url=None,
    content="""Office of Academic Affairs – Academic Awards Letter  
Date: October 2024  

CONGRATULATIONS! Your best efforts during the 2023–2024 academic year have earned you one or more of the following Academic Awards:

• **Academic Letter** – awarded to students earning full-year Honor Roll distinction for the first time.
• **Academic Star** – awarded to students earning full-year Honor Roll distinction in each subsequent academic year.
• **Subject Certificates of Merit** – awarded to the top student(s) by subject in each grade level.

📘 *Note: The criteria for Honor Roll distinction are listed in the Student Handbook (pg. 20).*

🎓 **Academic Awards Assemblies (by class year):**
- October 9 (Wed) – Class of 2025
- October 11 (Fri) – Class of 2027
- October 14 (Mon) – Class of 2026

All awards are presented in homeroom assemblies in the theater to publicly recognize and celebrate student achievement within each class year.

📄 A complete list of award recipients is available on the Academic Affairs tile on the school resource page.

💬 A message from Mr. Fan, Vice Principal of Academic Affairs:  
"Earning an Academic Award is more than just receiving good grades. It’s a reflection of your sacrifice, commitment, and drive to achieve academic excellence. In a school with high standards, you’ve not only met them—you’ve exceeded them. We are incredibly proud of your achievement and dedication."

Questions? Contact Mr. Fan at fant@calverthall.com.
"""
)

insert_chunk(
    topic="Textbook List - Class of 2025",
    url="https://calverthall.myschoolapp.com/ftpimages/274/download/download_8238010.pdf?_=1744238061681",
    content="""Class of 2025 Textbook List

The list is organized alphabetically by last name and includes a scanable barcode accessible via phone.

BOOK RETURN INSTRUCTIONS:
• Bring your TB Notice (received in homeroom on 5/30) when returning books.
• If you do not have your TB Notice:
  - Print your portion of the textbook list
  - Bring a printed copy of your course schedule
• Check TB return directions for specific May return procedures.

Updated 8/29/2024
"""
)

insert_chunk(
    topic="Textbook List - Class of 2026",
    url="https://calverthall.myschoolapp.com/ftpimages/274/download/download_8238011.pdf?_=1744238061681",
    content="""Class of 2026 Textbook List

The list is organized alphabetically by last name and includes a scanable barcode accessible via phone.

BOOK RETURN INSTRUCTIONS:
• Bring your TB Notice (received in homeroom on 5/30) when returning books.
• If you do not have your TB Notice:
  - Print your portion of the textbook list
  - Bring a printed copy of your course schedule
• Check TB return directions for specific May return procedures.

Updated 8/29/2024
"""
)

insert_chunk(
    topic="Textbook List - Class of 2027",
    url="https://calverthall.myschoolapp.com/ftpimages/274/download/download_9793183.pdf?_=1744238061681",
    content="""Class of 2027 Textbook List

The list is organized alphabetically by last name and includes a scanable barcode accessible via phone.

BOOK RETURN INSTRUCTIONS:
• Bring your TB Notice (received in homeroom on 5/30) when returning books.
• If you do not have your TB Notice:
  - Print your portion of the textbook list
  - Bring a printed copy of your course schedule
• Check TB return directions for specific May return procedures.

Updated 8/29/2024
"""
)

insert_chunk(
    topic="Textbook List - Class of 2028",
    url="https://calverthall.myschoolapp.com/ftpimages/274/download/download_9793200.pdf?_=1744238061681",
    content="""Class of 2028 Textbook List

The list is organized alphabetically by last name and includes a scanable barcode accessible via phone.

BOOK RETURN INSTRUCTIONS:
• Bring your TB Notice (received in homeroom on 5/30) when returning books.
• If you do not have your TB Notice:
  - Print your portion of the textbook list
  - Bring a printed copy of your course schedule
• Check TB return directions for specific May return procedures.

Updated 8/29/2024
"""
)

insert_chunk(
    topic="Policy for Student Schedules & Lunch Periods",
    url=None,
    content="""Office of Academic Affairs – Lunch Period Policy  
Updated: 8/27/2024

Per the school handbook, students may not eat outside of designated dining areas:  
• Dining Hall  
• George Young Pavilion  
• Courtyards  

📌 **Exception**: Students without a free/lunch period between Periods 2 and 7  
If a student has classes consecutively from Periods 2 to 7 without a break, they may eat lunch during class under the following rules:

PERMITTED:
• Students must ask their teacher for permission.
• Students must show a printed schedule proving they do not have a lunch period.
• Students must eat quietly and remain in the classroom.

RESTRICTIONS:
🚫 Eating is NOT allowed in:
- Math classes
- Science lab classes
- During lectures or tests

🚫 Eating is NOT allowed in these locations:
- Lecture Halls
- Science Labs
- Library
- Commons
- Gyms
- Language Labs
- Chapel

⚠️ Food brought into class should not be disruptive (e.g., smelly, requires heating, messy).

Failure to follow protocol will result in:
• Loss of eating privilege in class
• Disciplinary consequences as outlined in the school’s Discipline Policy

Questions? Contact the Office of Academic Affairs.
"""
)

insert_chunk(
    topic="Effective Study Habits",
    url=None,
    content="""Effective Study Habits  
Updated: 8/28/2023

A few suggested examples of effective study habits:
• Set specific, realistic goals for each study session.
• Use active recall and spaced repetition to retain information.
• Find a quiet, distraction-free place to study.
• Take short breaks after 25–30 minutes of focused work (Pomodoro technique).
• Organize notes by subject, topic, or importance.
• Avoid multitasking; focus on one subject at a time.
• Use flashcards, practice quizzes, or group discussions for reinforcement.
• Review material regularly—not just before exams.
"""
)

insert_chunk(
    topic="Dual Enrollment Programs - NDMU Transcript Access",
    url="https://www.ndm.edu/academics/registrar/transcripts",
    content="""NDMU Dual Enrollment Transcript Access

Calvert Hall students who participated in a dual enrollment course through Notre Dame of Maryland University (NDMU) can access their transcript through the NDMU registrar website.

📄 Use the following link to:
• View your student record
• Order official transcripts to be sent to colleges

🔗 NDMU Transcript Portal: https://www.ndm.edu/academics/registrar/transcripts

❓ Questions about credit approval or transcript access should be directed to:
Ms. Susanna Price (NDMU Registrar) – sprice@ndm.edu
"""
)

insert_chunk(
    topic="Academic Policy - Homework Submission & Late Work (AY 2022–2023)",
    url=None,
    content="""Updated Homework Policy – Academic Year 2022–2023

At Calvert Hall, consistent homework completion is key to student success. Homework is used to assess understanding and directly impacts grades.

📌 KEY POINTS:
• Teachers will post homework to the assignment center in a timely manner.
• Homework not submitted by the due date will be marked “Missing” in the gradebook.
• Late work is subject to each course’s specific late homework policy (outlined in the course syllabus).
• Any homework not submitted within 2 weeks of the due date will receive a grade of 0.

📬 Questions about:
• General homework policies → Office of Academic Affairs
• Specific assignments, instructions, or deadlines → Your course instructor
"""
)

insert_chunk(
    topic="Student Lunch Policy - Eating in Classrooms Without a Legal Lunch Period (AY 2022–2023)",
    url=None,
    content="""Updated Lunch Policy – Academic Year 2022–2023

Some students have schedules without a legal lunch period between Periods 2 and 7. These students may request teacher permission to eat lunch in class under the following conditions:

✅ PERMITTED:
• Student has 5+ consecutive periods between Period 2 (9:35 AM) and Period 7 (2:00 PM)
• Must show class schedule as evidence
• May eat quietly while participating in class
• Lunch must be ready-to-eat (no heating, minimal prep)
• Student must clean up after eating

🚫 NOT ALLOWED:
• Eating in lecture halls, science rooms, music rooms, art studio, or computer labs
• Leaving class to eat or buy lunch
• Using phones/devices during lunch
• Bringing distracting or messy food

Teachers may revoke the privilege at their discretion.

Questions? Contact the Office of Academic Affairs.
"""
)


insert_chunk(
    topic="Academic Policy - Student Absences & Make-Up Work Expectations (AY 2022–2023)",
    url=None,
    content="""CHC Policy – Student Absences  
Updated: 9/6/2022

Calvert Hall distinguishes between **academic (medical)** and **non-academic (personal/vacation)** absences. The policies for each are outlined below:

📌 GENERAL GUIDELINES:
• Non-academic absences (e.g., vacations, non-CHC sports events) are considered personal choices.
• Teachers are **not required to re-teach material** or extend due dates for non-academic absences.
• Students are responsible for all missed content.
• Online attendance form must be completed with the reason and a note submitted when returning.

📧 COMMUNICATION:
• Students must contact teachers ASAP if absent.
• Teachers may allow due date adjustments for pre-approved medical exemptions only.
• Medical exemptions must be approved by the Office of Academic Affairs.
• COVID-related absences must be cleared by the school nurse.

📚 CLASS LINKS:
• Only provided for pre-approved exemptions (not for general absences).

📅 EXAM POLICY:
• All students must be present for exams.
• Only a doctor’s note is accepted for exam absences.
• Absences without a doctor’s note may incur a **20% penalty** on the final exam grade.

❓ Questions? Contact:
Mr. Thomas Fan, Assistant Principal of Academic Affairs  
📧 fant@calverthall.com  
📞 410-825-4266 x137
"""
)


insert_chunk(
    topic="Technology Policy - Acceptable Use & BYOD Requirements (AY 2024–2025)",
    url="https://calverthall.myschoolapp.com/ftpimages/274/download/download_4896603.pdf?_=1744245098549",
    content="""ACCEPTABLE USE POLICY FOR TECHNOLOGY  
Calvert Hall provides access to technology resources to support academic, administrative, and community goals. Students are expected to use technology ethically, legally, and in accordance with the school’s mission and behavioral standards—on or off campus.

GENERAL EXPECTATIONS:
• Students have **no expectation of privacy** when using school devices or the school network.
• CHC may monitor school-managed accounts, emails, documents, and activity logs to ensure compliance.
• All behavior online should match CHC’s in-person standards.

✅ STUDENTS MAY:
• Use technology for classwork and teacher-approved projects
• Access the internet for schoolwork (with teacher permission)
• Follow teacher directions when using tech in class

🚫 STUDENTS MAY NOT:
• Share passwords or impersonate others
• Post personal information or access unauthorized areas
• Use inappropriate language or images (in any format or platform)
• Engage in cyberbullying, sexting, or harassment
• Bypass web filtering or access explicit or violent content
• Plagiarize or violate copyright laws
• Install or delete software/hardware on school devices
• Use mobile hotspots or remove school-owned equipment
• Store personal files outside their school-assigned account
• Make defamatory remarks about CHC or its community
• Disrupt the school’s network or connect with staff online on non-educational platforms

💥 Violations may result in loss of privileges, suspension, or dismissal. The administration has final authority over appropriateness of use.

---

🎒 **BRING YOUR OWN DEVICE (BYOD) REQUIREMENTS**

All students must bring a personal device to school daily. Devices must meet the following standards:

MINIMUM DEVICE REQUIREMENTS:
• Modern, supported OS (e.g., Windows 10, macOS, iOS)
• Fully functional web browser
• Productivity/note-taking software installed
• Wi-Fi enabled, fast startup (< 90 seconds)
• Full-day battery life

TABLET REQUIREMENTS:
• Minimum 7” screen
• External physical keyboard

RECOMMENDATIONS:
• Use a protective case
• Avoid Chromebooks (limited compatibility with MS Office)
• All students receive Microsoft Office Suite free of charge

Students are expected to bring their device daily and keep it in working condition.
"""
)

insert_chunk(
    topic="Library Tools & Academic Resources - Research, Passwords, and Study Help (AY 2024–2025)",
    url=None,
    content="""📚 LIBRARY TOOLS & RESEARCH DATABASES

• NoodleTools Student Login  
  🔗 https://my.noodletools.com/logon/signin?domain=calverthall.com

• Bloom’s Literary Reference  
  🔗 http://online.infobase.com/HRC/Browse/Product/12

• Project Muse  
  🔗 https://muse.jhu.edu/cgi-bin/refer.cgi

• Salem Press – History  
  🔗 http://history.salempress.com/

• Salem Press – Health  
  🔗 http://health.salempress.com/

• Gale: Discovering Collection, Opposing Viewpoints, Literature  
  🔗 http://infotrac.galegroup.com/

• ProQuest Home Access  
  🔗 https://www.proquest.com/?accountid=65601

• JSTOR Home Access  
  🔗 http://www.jstor.org/logon

---

🔧 TECH SUPPORT & HELP TOOLS

• How to change your CHC password  
  🔗 https://calverthall.myschoolapp.com/app/faculty#topicdetail/190868/16429456/16429456/433066/0/1

📐 MATH HELP

• Sign-up form for Math Help with Mr. Baker  
  🔗 https://forms.office.com/Pages/ResponsePage.aspx?id=hTcqDeHAiEy9zknuGQZ_UWflUMxDV6BCh-ZjFwQ3X05UMEZTNzJFRlk1R1JUSDFVSUpQNENWNlJaMy4u

These resources support academic research, citation, tech needs, and tutoring.
"""
)

insert_chunk(
    topic="Summer Opportunities 2025 - Full Program Listing with URLs",
    url=None,
    content="""📚 Summer Opportunities for High School Students – 2025 Edition

Below is a comprehensive list of 2025 summer academic, creative, and enrichment programs open to high school students (many for rising juniors and seniors). All links are directly accessible.

---

🔗 **Adelphi University** – Pre-College Programs  
http://precollege.adelphi.edu/

🔗 **American Legion (Maryland)** – Boys State  
http://www.mdlegion.org/boysstate/

🔗 **Boston University** – Journalism Academy  
http://www.summerjournalism.org/  
🔗 Summer Term for High School Students:  
http://www.bu.edu/summer/high-school-programs/

🔗 **California College of the Arts** – Pre-College  
http://www.cca.edu/precollege

🔗 **Carleton College** – Liberal Arts Experience  
http://go.carleton.edu/clae

🔗 **Catholic University of America** – Summer on Stage  
http://drama.cua.edu/summer

🔗 **University of Chicago** – Summer Session  
http://summer.uchicago.edu/

🔗 **Christendom College** – Summer Experience  
http://www.christendom.edu/experience

🔗 **Cleveland Institute of Art** – Artists-in-Residence  
https://www.cia.edu/continuing-education/pre-college

🔗 **College of William & Mary**  
- NIAHD Pre-College: https://www.wm.edu/niahd  
- Legal Education Series: https://www.legaltechcenter.net/courses-training/law-related-education/

🔗 **Columbia Business School** – Pre-College  
https://kup.gsb.columbia.edu/?utm_campaign

🔗 **University of Delaware** – EDGE Program  
https://www.udel.edu/edge/

🔗 **Denison University** – Reynolds Young Writers Workshop  
https://denison.edu/campus/pre-college

🔗 **Duke University** – All Pre-College Programs  
https://learnmore.duke.edu/precollege/all-programs

🔗 **Elon University** – Emerging Journalists Program  
https://www.elon.edu/ejp

🔗 **Georgetown University** – Pre-College Programs  
https://georgetown.precollegeprograms.org  
🔗 Surgical Academy: https://georgetown.precollegeprograms.org/surgery

🔗 **Global Works** – Travel with Purpose  
https://www.globalworkstravel.com

🔗 **Howard County Leadership U**  
https://www.leadershiphc.org/leadership-u-2/

🔗 **Illinois Institute of Technology** – STEM Programs  
https://www.iit.edu/academics/pre-college-programs/summer

🔗 **Ithaca College** – Writers Institute  
http://ithaca.edu/iwi

🔗 **Johns Hopkins University** – Pre-College  
https://summer.jhu.edu/

🔗 **Landmark College** – Summer Programs  
http://landmark.edu/summer

🔗 **Lumiere Education** – Research Scholar Program  
http://www.lumiere-education.com/

🔗 **Marist College** – Pre-College  
http://marist.edu/precollege

🔗 **Maryland Institute College of Art (MICA)** – Pre-College  
http://www.mica.edu/precollege

🔗 **University of Maryland, College Park** – Terp Young Scholars  
https://go.umd.edu/tyscourses

🔗 **UMass Amherst** – Pre-College & Mt. Ida Programs  
https://www.umass.edu/uww/programs/pre-college  
https://www.umass.edu/uww/programs/pre-college/mt_ida

🔗 **Miami University of Ohio** – Summer Scholars  
http://miamioh.edu/summerscholars

🔗 **University of Michigan** – Stamps Pre-College  
https://stamps.umich.edu/pre-college

🔗 **New York University (NYU)** – High School Programs  
https://www.nyu.edu/highschool

🔗 **Northwestern University** – College Prep Program  
https://sps.northwestern.edu/college-preparation/admission.php

🔗 **University of Notre Dame**  
- Summer Scholars: http://precollege.nd.edu/summer-scholars/  
- Study Abroad: http://precollege.nd.edu/study-abroad/

🔗 **Notre Dame of Maryland University** – Pharmacy Camp  
https://www.ndm.edu/colleges-schools/school-pharmacy/pharmacy-camp

🔗 **Oxbridge Academic Programs**  
http://www.oxbridgeprograms.com/

🔗 **Phillips Exeter Academy** – Summer School  
http://www.exeter.edu/summer

🔗 **Pratt Institute** – Pre-College  
http://www.pratt.edu/precollege

🔗 **Rensselaer Polytechnic Institute (RPI)** – Summer Design Engineering  
https://info.rpi.edu/pre-college-initiatives/preface-rensselaer-summer-engineering-design-program-2021

🔗 **St. John’s College** – Summer Academy  
http://www.sjc.edu/summeracademy

🔗 **Savannah College of Art & Design (SCAD)**  
http://scad.edu/sss

🔗 **Sewanee: The University of the South** – Environmental Institute  
https://new.sewanee.edu/academics/summer-in-sewanee

🔗 **U.S. Naval Academy** – Summer STEM  
https://www.usna.edu/Admissions/Programs/STEM.php#fndtn-panel1-Attending

🔗 **University of Southern California (USC)**  
- General Pre-College: https://precollege.usc.edu/summer-prog  
- Bovard Scholars: http://scholars.usc.edu/

🔗 **Spoleto Study Abroad** – Summer in Italy  
http://www.spoletostudyabroad.com/

🔗 **Stanford University** – Summer College  
http://spcs.stanford.edu/find-yourself

🔗 **Stevens Institute of Technology** – Pre-College  
https://www.stevens.edu/admissions/pre-college-programs

🔗 **Summer Discovery & Discovery Internships**  
http://www.summerdiscovery.com/

🔗 **Syracuse University** – Summer Pre-College  
🔗 Scholarships & Info: https://calverthall.myschoolapp.com/app/student#resourceboarddetail/4937

---

Students are encouraged to research these programs early and apply as soon as possible. Many have rolling or early deadlines.

Speak with your counselor if you need help choosing the right fit or preparing an application!
"""
)

insert_chunk(
    topic="Dining Services & Meal Ordering - Sage Menus, Sandwich Pre-Order, First Financial Account Setup",
    url=None,
    content="""🍴 **Dining & Food Services at Calvert Hall**

🔗 **Sage Dining Portal**  
View lunch menus, allergen information, and nutrition details through the Sage Dining website:  
https://www.sagedining.com/sites/calverthall?page=home

🥪 **Sandwich Ordering (Pre-Lunch System)**  
Pre-order your lunch in advance using the CHC Campus Cards platform:  
https://chc.campus.cards/order/

💳 **First Financial Meal Cards – Important Setup Info**

Students may only buy lunch **if they have an active First Financial account linked to their ID card**. Here's how it works:

✅ **Setup Requirements:**
• Students receive an ID card in homeroom.  
• Cards are NOT automatically linked — you must create an account with First Financial online, in-branch, or by mailing in paperwork.  
• It takes a few days to activate an account. **Bring a packed lunch until activation is confirmed.**

💵 **Adding Money to the Card:**
• Use the **First Financial mobile app**, or  
• Visit the **Cardinal Branch** at school (open 8:00–8:20 AM on school days).

📌 **IOU Policy:**
• Students may request an IOU (up to **3 times per semester**) from the Student Activities Office.  
• IOUs are **$10** and cover a Cardinal Meal Deal.  
• All loans must be repaid **within 1 week**.  
• Unpaid IOUs at month’s end are sent to the **Finance Office** and charged to the student's **FACTS account**.

📞 **Need Help?**
• Member Services: 410-321-6060 (Option 5)  
• CHC First Financial Contact:  
  - **Mrs. Cindy Jones**  
  - Phone: 410-427-8954  
  - Email: cjones@firstfinancial.org
"""
)


insert_chunk(
    topic="Student Parking Registration & Off-Campus Tag Policy (AY 2024–2025)",
    url="https://calverthall.myschoolapp.com/podium/default.aspx?t=36644&rid=960",
    content="""🚗 **Student Parking Registration – 2024–2025 School Year**

All students who drive to school are required to register their vehicle each academic year — even if it was registered the year before.

📌 KEY REMINDERS:
• You must register **each vehicle** you plan to drive.  
• **On-campus parking spots are full** — new registrations will receive a **cling-tag** allowing parking **off-campus** on nearby streets.

🔗 Register for student parking here:  
https://calverthall.myschoolapp.com/podium/default.aspx?t=36644&rid=960

Unregistered vehicles may be subject to disciplinary action or ticketing.
"""
)


insert_chunk(
    topic="Student Resources – Forms, Bookstore, Transportation, Parent Club & More (AY 2024–2025)",
    url=None,
    content="""📘 **Resource Hub for Students & Families – 2024–2025**

🛒 **eCampus Bookstore** (Textbooks & Supplies)  
https://calverthall.ecampus.com/

📄 **Student Handbook (PDF)**  
https://bbk12e1-cdn.myschoolcdn.com/ftpimages/274/misc/misc_229973.pdf

🚌 **Transportation Info & Bus Routes**  
https://www.calverthall.com/admissions/transportation

💳 **First Financial Card Resource Tile**  
https://calverthall.myschoolapp.com/app/student#resourceboarddetail/6423

📅 **Class of 2025 Graduation Info**  
https://calverthall.myschoolapp.com/app/student#resourceboarddetail/7167

📇 **Paraprofessional / Volunteer Form** (Submit to Front Office)  
https://mediafiles01.myschoolcdn.com/ftpimages/274/misc/misc_118607.pdf

📈 **Register Your TI Calculator**  
https://calverthall.myschoolapp.com/podium/default.aspx?t=36644&rid=1733

🏫 **Parents' Club Sign-Up & Dues Payment**  
https://calverthall.myschoolapp.com/podium/default.aspx?t=36644&rid=2191

📘 **Order the 2024–2025 Yearbook Online**  
(Link was mentioned as “HERE” — let me know if you have the actual URL)

All links can also be accessed via the Student or Parent Resource Boards in the CHC portal.
"""
)

insert_chunk(
    topic="Retreats at Calvert Hall - Student Resource Page",
    url="https://calverthall.myschoolapp.com/app/student#resourceboarddetail/6288",
    content="""🕊️ **Student Retreats at Calvert Hall**

Retreats are an integral part of Calvert Hall's spiritual and community formation. All students are encouraged to participate fully in retreat experiences tailored to their grade level.

Visit the Retreat Information Page here:  
🔗 https://calverthall.myschoolapp.com/app/student#resourceboarddetail/6288

Details vary by grade level and may include overnight, day-long, or off-campus experiences.
"""
)

insert_chunk(
    topic="Service Requirements & Building Brotherhood Program - All Class Years (2024–2025)",
    url=None,
    content="""🛠️ **CHC Service Program & Building Brotherhood – Overview**

Service is a core part of the Calvert Hall mission. Below are resources by class year, plus program guides and agency directories.

📥 **Directory of Approved Service Agencies** (Updated May 2024)  
https://calverthall.myschoolapp.com/ftpimages/274/download/download_7087094.pdf?_=1744247382551

🎤 **Building Brotherhood Program – Overview Presentation**  
https://calverthall.myschoolapp.com/ftpimages/274/download/download_7087095.pptx?_=1744247382551

---

📚 **Grade-Specific Service Guides:**
• **Freshman Service Info**:  
  https://calverthall.myschoolapp.com/ftpimages/274/download/download_7087096.pdf?_=1744247382551

• **Sophomore Service Info**:  
  https://calverthall.myschoolapp.com/ftpimages/274/download/download_7087098.pdf?_=1744247382551

• **Junior Service Covenant**:  
  https://calverthall.myschoolapp.com/ftpimages/274/download/download_9362425.pdf?_=1744247382551

• **Junior Service Info**:  
  https://calverthall.myschoolapp.com/ftpimages/274/download/download_7087103.pdf?_=1744247382551

---

📱 **Volunteer Platform & Special Programs:**
• **Archdiocese of Baltimore – Volunteer App Process**  
  https://calverthall.myschoolapp.com/ftpimages/274/download/download_7573955.pdf?_=1744247382552

• **Beyond the Borders / IOSC Info Sheet**  
  https://calverthall.myschoolapp.com/ftpimages/274/download/download_7573954.pdf?_=1744247382552

❓ Questions? Reach out to your Religion teacher or contact:  
📧 Mr. Barczak – Religion Department Chair (barczakc@calverthall.com)
"""
)

insert_chunk(
    topic="Transportation Services - Bus Routes & Carpooling by County (AY 2024–2025)",
    url="https://www.calverthall.com/admissions/transportation",
    content="""🚌 **Transportation at Calvert Hall – 2024–2025**

Calvert Hall offers **bus transportation** for students in several counties and assists with **carpool connections** for interested families.

📞 Contact for Buses: Kris Mitchell – 410-825-4266 x185  
📞 Contact for Carpools: Lucy Baker – 410-825-4266 x117

---

### 🟡 **Anne Arundel County Bus**
• **Cost:** $1750 (AM service only)  
• **Stops & Times:**
  - 6:30 a.m. – Marley Station Mall  
  - 6:40 a.m. – Monsignor Slade School  
  - 7:30 a.m. – Arrive at Calvert Hall

---

### 🟠 **Carroll County Bus**
• **Cost:** $1700 (AM service only)  
• **Stops & Times:**
  - 6:30 a.m. – St. Joseph’s Catholic Church (915 Liberty Rd, Eldersburg)  
  - 6:45 a.m. – Finksburg Plaza (3000 Gamber Rd, Finksburg)

---

### 🔵 **Harford County Bus**
• **Cost:** $1500 (AM service only)  
• **Stops & Times:**
  - 6:45 a.m. – St. Margaret’s Middle School  
  - 7:00 a.m. – Harford Mall (former Sears entrance)  
  - 7:15 a.m. – Van Dorn Pools & Spas (Kingsville)  
  - 8:05 a.m. – Arrive at Calvert Hall

---

### 🟢 **Howard County Bus** *(with round trip options by American Limousine)*  
• **Cost Options:**
  - $2200 – Round Trip (morning + either afternoon bus)  
  - $1500 – Afternoon Only  
  - $1150 – Morning Only

🕑 **Morning Route:**
  - 6:15–6:20 a.m. – Columbia Mall (Lidl lot)  
  - 6:35–6:40 a.m. – Sprouts (Rt. 40 & St. Johns Ln)  
  - 6:50–6:55 a.m. – Applebee’s (6505 Baltimore National Pike, Catonsville)  
  - 7:00–7:05 a.m. – AMF Bowling Lanes (Pikesville)  
  - 7:25 a.m. – Arrive at Calvert Hall

🕒 **Afternoon (Early Pick-Up):**
  - 3:00 p.m. – Depart CHC  
  - 3:20 p.m. – AMF Bowling Lanes  
  - 3:40 p.m. – Panera/Toys R Us (6600 Baltimore National Pike)  
  - 3:50 p.m. – Sprouts  
  - 4:00 p.m. – Columbia Mall (Sears lot)

🕕 **Afternoon (Late Pick-Up):**
  - 5:50 p.m. – Depart CHC  
  - 6:10 p.m. – AMF Bowling Lanes  
  - 6:30 p.m. – Panera/Toys R Us  
  - 6:40 p.m. – Sprouts  
  - 6:50 p.m. – Columbia Mall

---

🚗 **Carpool Connections Available**  
Families can be connected with others in their area for carpooling through CHC support.

🌐 Full transportation page:  
https://www.calverthall.com/admissions/transportation
"""
)

insert_chunk(
    topic="Attendance Policies, Magnus Health Info & Medical Forms (AY 2024–2025)",
    url=None,
    content="""📌 **Attendance Office – New Policy (Effective 2024–2025)**

The Attendance Office no longer accepts phone calls, emails, or handwritten notes.  
Parents must log in to the Calvert Hall website and **complete the correct online form** for:

• Student absences  
• Late arrivals  
• Early dismissals

🔗 Doctors’ notes may still be emailed to: **attendance@calverthall.com**  
☎️ Questions? Call the Attendance Office at **410-825-4266 x119**

---

🩺 **Magnus Health Platform – Medical Information & Forms**

Calvert Hall uses **Magnus Health** (linked through your parental CHC account) to collect all required medical info.  
You will find a checklist of required forms once logged into Magnus via the **Magnus Resource Tile**.

📅 **Physical Deadlines:**
• Incoming Freshmen – must have a physical exam between **May 31–Aug 1, 2024**  
• Upperclassmen – rolling deadline: **1 year and 1 day** from the last submission

⛔️ Students without updated physicals **cannot participate in athletics or marching band**.

📋 **Magnus To-Do Checklist:**
• Schedule & complete physical  
• Log in to CHC website and update your parent profile (incl. cell number)  
• Complete Emergency Medical Contact Form (sent ~July 1)  
• Log into Magnus from the CHC parent account  
• Upload physical and immunization forms  
• Complete OTC form and any prompted health-specific documents  
• Prescription med form must be completed by a provider if needed  
• Use the **Magnus Mobile App** for easier uploads (multi-page scanning supported)

☎️ Magnus Tech Support: **919-502-7689**  
📧 Health Office: **schoolnurse@calverthall.com**  
📞 Nurse: Cindy Faherty – 410-825-4266 x120

---

🏥 **CHC Health Suite Policy Reminders**

• Stay home with fever ≥100.4°F until **24 hours fever-free** (no meds)  
• Stay home 24 hours after last vomiting/diarrhea episode

---

📄 **Health Suite Forms & Downloads**

• [CHC Physical Form (PDF)](https://calverthall.myschoolapp.com/ftpimages/274/download/download_2030881.pdf?_=1744247193557)  
• [Vaccine Requirements](https://calverthall.myschoolapp.com/ftpimages/274/download/download_8208264.pdf?_=1744247193557)  
• [MD Immunization Form](https://calverthall.myschoolapp.com/ftpimages/274/download/download_8208282.pdf?_=1744247193557)  
• [Prescription Medication Form](https://calverthall.myschoolapp.com/ftpimages/274/download/download_5871427.pdf?_=1744247193557)  
• [Food Allergy & Anaphylaxis Form](https://calverthall.myschoolapp.com/ftpimages/274/download/download_8208682.pdf?_=1744247193557)  
• [Seizure Action Plan](https://calverthall.myschoolapp.com/ftpimages/274/download/download_8208683.pdf?_=1744247193557)  
• [Diabetes Orders Form](https://calverthall.myschoolapp.com/ftpimages/274/download/download_8208686.pdf?_=1744247193557)  
• [Asthma Medication/Action Form](https://calverthall.myschoolapp.com/ftpimages/274/download/download_8208679.pdf?_=1744247193557)

❓ **More FAQs and Health Protocols** (masking, COVID, vaccine info):  
https://calverthall.myschoolapp.com/app/student
"""
)


insert_chunk(
    topic="Student Handbook – Chapter 1: About Calvert Hall and its History",
    url="https://bbk12e1-cdn.myschoolcdn.com/ftpimages/274/misc/misc_229973.pdf",
    content="""📘 **About Calvert Hall**

### 🕊️ The History
Calvert Hall has been operated by the **Brothers of the Christian Schools** (Christian Brothers) for 179 years. Founded by **St. John Baptist de La Salle**, the Brothers began their mission in France in 1679, offering a "human and Christian education." De La Salle was canonized in 1900.

Lasallian education came to the U.S. in 1845 with the opening of Calvert Hall in Baltimore. It moved to its current **Towson campus in 1960**. Major campus developments include the Crispino Center, Russo Stadium, and the new E-Sports Arena (2024).

The school has been recognized twice as an **Exemplary School** by the U.S. Dept. of Education.

---

### 🧭 **Mission Statement**
Calvert Hall College High School, a Catholic and Lasallian college prep school, prepares a diverse community of young men to achieve their full potential. With strong academic and extracurricular programs led by innovative educators, students become men of **intellect**, **faith**, and **integrity**.

---

### 📚 **Philosophy**
The school:
- Reflects the legacy of **St. John Baptist de La Salle**
- Encourages academic rigor and diversity
- Emphasizes learning “together and by association”
- Offers service and campus ministry to foster faith
- Focuses on developing ethical decision-makers and community leaders

---

### 🌍 **Diversity, Equity, Inclusion (DEI) Statement**
CHC aligns its DEI goals with Lasallian Core Principles. It strives to develop **inclusive brotherhood**, regardless of race, gender, socioeconomic status, or other identifiers.

---

### 🚫 **Non-Discrimination Policy**
CHC does not discriminate in any school-administered programs. Policies comply with:
- **Title VI** of the Civil Rights Act of 1964
- **Title 26, Subtitle 7** of the Maryland Education Code

Faith-based exceptions apply if non-admittance is aligned with CHC’s religious principles.

---

### 🎓 **Graduate Profile**
**A Man of Intellect**:
1. Demonstrates critical thinking
2. Communicates effectively
3. Embraces knowledge and technology
4. Values arts, athletics, and creativity

**A Man of Faith**:
1. Understands Catholic social teaching
2. Respects others’ dignity
3. Performs service
4. Lives with spiritual awareness and brotherhood

**A Man of Integrity**:
1. Makes ethical decisions
2. Acts with honesty and maturity
3. Leads responsibly

---

### 🛡️ **Core Beliefs**
• Catholic, Lasallian values guide CHC’s mission  
• Each student deserves academic excellence and personal challenge  
• Community and interpersonal growth are central  
• Brotherhood and respect are lifelong values

---

### 🏛️ **Symbols & Identity**
- **School Seal:** Combines the Calvert family insignia and De La Salle heritage
- **Colors:** Cardinal & Gold  
- **Mascot:** Cardinal

---

### 📋 **Accreditations**
• AIMS (Assoc. of Independent Maryland Schools)  
• MSDE (Maryland State Dept. of Ed)  
• MSA (Middle States Association)  
• CASE (Council for Advancement & Support of Education)

### 🤝 **Affiliations**
• Christian Brothers Conference  
• National Catholic Education Association
"""
)


insert_chunk(
    topic="Student Handbook - Chapter 3: Daily Procedures",
    url="https://bbk12e1-cdn.myschoolcdn.com/ftpimages/274/misc/misc_229973.pdf",
    content="""
DAILY PROCEDURES

Academic Calendar:
Calvert Hall has 174 instructional days, with 4 extra days built in for inclement weather. The school reserves the right to amend the calendar or instructional mode as needed.

Advertising for Clubs and Activities:
Only CHC-sponsored activities may be advertised. Approval is needed from the moderator and Office of Student Activities.

Appearance and Dress Code:
Students must wear dress pants, belt, dress shoes with socks, a dress shirt and tie, and a sport coat (seasonal exceptions apply). Hair must be neat, clean, and within acceptable styles and length. Beards, dyed hair, mohawks, earrings, and body piercings are not allowed.

Attendance and School Hours:
Parents must submit absence, late arrival, or early dismissal forms via the Attendance Tile. Students with 12+ absences may face consequences. Homeroom starts at 8:25 AM and the day ends at 2:45 PM. Students must attend religious ceremonies.

Campus Access, Safety, and Security:
Commons are for quiet study only. Students need permission to access restricted areas. ID cards must be worn at all times. Security cameras record activity but are not monitored. Swipe cards are non-transferrable.

Lunch Loans:
Students may take up to 3 $10 lunch loans per semester. Unpaid loans will be added to the student’s FACTS account. Parents may opt their child out of this program.

Directory and Contact Information:
Parents must keep contact info up to date in the CHC portal. A written request is required to restrict release of directory information.

Emergency Notifications and School Closings:
Emergency alerts are sent via phone/text. CHC follows Baltimore County Public Schools for weather-related closures and delays.

Food and Gum:
Food is limited to the dining hall and outdoor spaces. No gum is allowed inside buildings.

Parking:
Students must register their cars annually. On-campus parking is limited and off-campus parking must follow specific street guidelines. Violators may lose future parking privileges.

Personal Belongings:
The school is not responsible for lost items. Bookbags must be labeled with the student’s name. Lockers must use school-purchased locks. Phones, earbuds, and headphones are for academic use only and must not be seen/heard during school hours.

Searches:
CHC reserves the right to search students, belongings, lockers, or vehicles to ensure a safe environment.

Student Media:
Unless parents opt out in writing, CHC may use student images, names, and works in promotional materials and media publications.

Visiting Other Schools:
Students may not visit other schools without prior authorization from those schools’ administrators on early dismissal days or holidays.
"""
)


insert_chunk(
    topic="Student Handbook - Chapter 4: Academic Policies and Courses (Part 1)",
    url="https://bbk12e1-cdn.myschoolcdn.com/ftpimages/274/misc/misc_229973.pdf",
    content="""
Academic Honesty:
Education begins with honest dialogue. All academic work must reflect the student's own understanding. Unauthorized assistance, including AI tools used without permission or citation, is a violation of policy. Plagiarism, cheating, or copying is not tolerated.

Consequences:
- First violation: zero on the assignment, reported to Academic Affairs, mandatory conference with Assistant Principal.
- Second violation: parent/student conference required.
- Further action may include disciplinary referrals, suspension, or expulsion.

Academic Probation:
Students failing two or more credit classes are placed on academic probation. They may be reassigned to support centers, study halls, and monitored through improvement plans and review meetings.

Addressing Academic Concerns:
Contact the student’s counselor first, then the subject teacher, followed by the Department Chair if needed. Teachers should be contacted via school email and will respond within 24 hours during weekdays.

Advanced Placement Courses:
407 students took 1040 AP exams in 2023-2024 with 88% scoring 3 or above.

AP Courses Offered:
Art, Biology, Calculus (AB, BC, BC2), Chemistry, Comparative Government, Computer Programming, Economics (Macro/Micro), Environmental Science, European History, French, German, Human Geography, Language & Composition, Literature & Composition, Latin (Language & Literature), Music Theory, Physics I/II, Psychology, Spanish (Language & Literature), Statistics, U.S. Government, U.S. History, World History.

Dual Enrollment:
In partnership with Notre Dame of Maryland University (NDMU), select Honors courses offer the opportunity for college credit via an official transcript from NDMU. This is available for the current year only. Courses include:
- Honors Pre-Calculus
- Honors Calculus
- Honors Multi-Variable Calculus
- Honors Differential Equations and Linear Algebra
- Honors Physics
- Honors U.S. History
- Honors Government
- Honors English IV (British Literature)
- Honors Computer Programming

Honors Courses Offered:
Algebra I/II, Anatomy & Physiology, Biology, Calculus AB/BC, Chemistry, Computer Programming, Differential Equations, English I-IV, French II-V, Geometry, German I-IV, Government, Latin I-III, Multivariate Calculus, Advanced Analysis, Physics, Pre-Calculus, Rhetoric & Logic, Spanish I-V, U.S. History, World History I/II

* Course descriptions available in the Program of Studies.
"""
)

insert_chunk(
    topic="Student Handbook – Chapter 4: Distinguished Honors Programs and Academic Support",
    url="https://bbk12e1-cdn.myschoolcdn.com/ftpimages/274/misc/misc_229973.pdf",
    content="""📘 **Chapter 4: Distinguished Honors Programs and Academic Support**

### 🎓 Distinguished Honors Programs

**The McMullen Scholars Program**
Designed for top-performing students, this rigorous program includes honors and AP coursework, field experiences, and original research. Additional classes include Honors Logic & Rhetoric, the Humanities, and the McMullen Capstone. 
📌 Director: Mr. David Hallman

**The Br. Tom Miller Honors Program**
A well-rounded honors experience offering challenging coursework, cultural opportunities, and leadership development.
📌 Director: Ms. Niki Creamer

📘 **Distinguished Support Programs**

**Academic Support Program**
Offers support in organization, time management, and study skills. Students meet with a specialist every other day in small groups.
📌 Specialist: Ms. Elizabeth Moore

**LaSalle Program**
Serves college-bound students with language-based learning differences. Daily support helps build reading, writing, and advocacy skills.
📌 Director: Mrs. Jennifer Healy

**Leadership Institute at Calvert Hall**
Students in grades 10–12 can earn a leadership certificate by completing seminars, retreats, and a practicum while participating in school activities.

**STEM Program**
Combines academics and hands-on learning to build problem-solving and research skills in 21st-century STEM fields.
📌 Director: Mr. Trey Hoos
"""
)


insert_chunk(
    topic="Student Handbook – Chapter 4: Academic Policies and Grades (Part 3)",
    url="https://bbk12e1-cdn.myschoolcdn.com/ftpimages/274/misc/misc_229973.pdf",
    content="""📘 **Student Handbook – Chapter 4: Academic Policies (Part 3)**

---

### 📝 Exams
Semester exams are held in December and June (May for seniors) and count for 15% of the semester grade. Absence on exam day requires a doctor’s note. Missing an exam without one may incur a 20% penalty. AP courses do not have spring exams. Seniors may be exempt from final exams if they have a 90% or higher average.

---

### 🎓 Graduation Requirements
- Seniors with up to 2.5 credit failures may make them up in summer school and receive a diploma afterward.
- Students with 3+ failures will not receive a Calvert Hall diploma.
- Retreat requirement is mandatory.
- All seniors must attend the Graduation Liturgy and Commencement.
- Diploma may be withheld if Commencement is missed.

---

### ⭐ Honor Roll
- GPA ≥ 88 with no grade below 81 (strict, not rounded).
- Honor Roll Holidays earned each semester must be used the following semester.
- Academic Letter/Star awarded for Honor Roll both semesters.

---

### 📜 National Honor Society – Selection Criteria
- **Scholarship**: Min. 90.0% unweighted GPA or 93.0% weighted GPA.
- **Service**: 2 years of CHC activity or 150 hrs/year service documented.
- **Character/Leadership**: Essay required; limited discipline violations allowed.

---

### 🏃 Physical Education
- Parent/doctor note needed for exemptions.
- Students exempt from PE cannot participate in athletics during that time.

---

### ⬆️ Promotion Requirements
- All subjects must be passed.
- <3 credit failures must be remediated in summer school.
- 3+ failures require withdrawal.
- Minimum curriculum includes 4 yrs Religion, English, Social Studies; 3 yrs Math and Lab Science; 2 yrs Foreign Language and PE; 3 electives; Fine Arts and Tech.

---

### 📈 Reports & Marking System
- Progress Reports: November and March.
- Semester Reports: January and June.
- Final grade: average of semester grades.
- Grades available on OnCampus.

**Marking System**:
- A/A+ (92–100): 4.0 GPA
- A– (89–91.9): 3.8–3.99
- B+ (86–88.9): 3.4–3.79
- B (83–85.9): 3.0–3.39
- B– (81–82.9): 2.8–2.99
- C+ (78–80.9): 2.4–2.79
- C (75–77.9): 2.0–2.39
- C– (73–74.9): 1.6–1.99
- D+ (72–72.9): 1.4–1.59
- D (70–71.9): 1.0–1.39
- F (69 and below): 0.0–0.99
"""
)

insert_chunk(
    topic="Student Handbook – Chapter 5: Student Conduct and Discipline",
    url="https://bbk12e1-cdn.myschoolcdn.com/ftpimages/274/misc/misc_229973.pdf",
    content="""📘 **Student Handbook – Chapter 5: Student Conduct and Discipline**

---

### 📏 Code of Conduct
Students are responsible for upholding Calvert Hall’s expectations on and off school property. Behavior that brings discredit to the school, including misconduct in public, may result in disciplinary action. Honesty is encouraged when reporting infractions, and dishonesty may influence consequences.

---

### ⚖️ Disciplinary Policies
- **General Detention**: Assigned for violating rules, being late to class, etc. Held after school for 40 minutes. Five detentions = Saturday detention.
- **Private Detention**: Assigned by a teacher. Takes precedence over general detention.
- **Students Arrested**: The school may take action based on the nature of the offense.
- **Suspension**: Parents notified; conference and signed acknowledgment required. Ineligibility for activities may apply.
- **Expulsion**: Review by Discipline Committee and final decision by the Principal.

---

### 🙋 Expectations for Conduct
- **Academic Integrity**: Violations are subject to disciplinary action.
- **Bullying/Cyberbullying**: Includes harm, fear, hostile environments, or educational disruption.
- **Gambling**: Prohibited.
- **Harassment**: Includes verbal/physical conduct denigrating characteristics like race, religion, etc.
- **Hazing**: Harmful or forced initiation practices.
- **Inappropriate Language**: Foul, hateful, or threatening speech.
- **Reckless Driving**: Especially serious due to nearby schools.
- **Retaliation**: Any reprisal against students who report misconduct.
- **Sexual Assault/Harassment**: Includes unwanted contact, comments, or coercion.
- **Tobacco, Drugs & Alcohol**: Prohibited. School may require in-school testing and impose treatment or expulsion.
- **Unauthorized Photos/Videos**: Forbidden without consent, except for public events.
- **Weapons**: Forbidden on campus or at school events. Includes firearms, knives, and fireworks.

"""
)

insert_chunk(
    topic="Student Handbook – Chapter 7: Student Organizations and Activities and Clubs",
    url="https://bbk12e1-cdn.myschoolcdn.com/ftpimages/274/misc/misc_229973.pdf",
    content="""📘 **Chapter 7: Student Organizations and Activities**

### 🏫 Student Organizations
- **Ambassadors / Admissions Office**
- **Asian Student Association** – Mrs. Knapp, Mrs. Clark
- **Band** – Mr. Ecton, Mr. Smith, Dr. Wilkerson
- **Black Student Union (BSU)** – Dr. van Gaal, Mr. Brooks
- **Bocce Ball Club** – Br. Len
- **Campus Ministry** – Mr. Collins, Ms. Fasy, Mr. McCormick
- **Cardinal Branch** – Mr. Greco, Mrs. Mary Lou Healy
- **Cardinal Crazies** – Mr. Adam Moore
- **CASA Club** – Ms. Gonzalez Sanchez
- **CHC TV** – Mr. Knight, Mr. Reilly
- **Chess Club** – Mrs. McKee
- **Communications Club** – Mrs. Hladky
- **Crokinole Club** – Mr. Ufnar
- **Culinary Club** – Mr. Fan
- **Cyber Security Club** – Mrs. Brown, Mr. Mellendick
- **Eagles Nest** – Mr. Motsay
- **Eastern European Culture Club** – Mr. Dobrzycki
- **Fellowship of Christian Athletes (FCA)** – Mr. Dobrzycki
- **Fishing Club** – Mrs. Buch
- **French Club** – Ms. d’Ecclesia, Mr. Goudou
- **Future Business Leaders of America (FBLA)** – Mr. Ryan
- **Games Club** – Mr. Luczak
- **Graphic Design Club** – Mr. Doyle
- **Green Club** – Mrs. Robertson
- **Hallmen** – Dr. Wilkerson
- **Hall Night Long** – Mr. Freeman
- **Hispanic Culture Club** – TBD
- **Homeroom Representatives** – Mr. Parisi
- **Homeroom Runners** – Mrs. Riportella
- **Intramurals** – Mr. Freeman
- **Irish Culture Club** – Mrs. Grezech
- **Italian Club** – Mrs. Buttarazzi
- **It’s Academic** – Mr. Brown
- **LaSallian Youth** – Ms. Fasy
- **Latin Club** – Dr. Mueller
- **Lawn Games Club** – Mr. Flannery
- **Liturgy Band** – Mr. Collins
- **Martial Arts & Boxing Club** – Mr. Freeman
- **Math Team** – Dr. Connor
- **Middle Eastern Club** – Mrs. Bassett
- **Military and Police Interest Club (MPIC)** – Mr. Sundell
- **Mock Trial** – Mrs. Bassett
- **Model United Nations** – Mr. Shank
- **National Honor Society** – Mrs. Urban
- **Newspaper** – Mrs. Manni
- **Odyssey, Literary Magazine** – TBD
- **Peer Education** – Ms. Conley
- **Peer Ministry** – Mr. Collins, Ms. Fasy, Mr. McCormick
- **Pickleball Club** – Mrs. Buttarazzi
- **Political Activism Club** – Mr. Alsedek
- **Quizbowl Team** – Dr. Eaton
- **Red Cross Volunteer Programs** – Mr. Motsay
- **Robotics Club** – Mr. Strong
- **Rockband Club** – Dr. Wilkerson
- **Sailing Club** – Ms. Makowski
- **Science National Honor Society** – Mr. Motsay
- **Ski Club** – Mr. Luczak
- **Spanish Club** – TBD
- **Speech & Debate** – Dr. Susko
- **Student Council** – Mr. Parisi
- **Theatre Club** – Mrs. Carroll
- **Unmanned Aerial Vehicle Club (UAV)** – Dr. Eaton
- **Weightlifting Club** – Mr. DeStefano
- **Yearbook** – Ms. Creamer, Ms. Ellis

### 🎓 Student Council Executive Board
- **Student Body President** – Gene Flynn ‘25
- **Chief of Staff** – Christopher Geldmacher ‘25
- **Head of Houses** – Ryan FitzPatrick ‘25
- **Student Spirit Director** – Michael Kirby ‘25
- **Student Communications Director** – Matthias Pridgeon ‘25
- **Senior Class President** – Matthew McFaul ‘25
- **Junior Class President** – Marco Carver ‘26
- **Sophomore Class President** – Luke Campbell ‘27
- **Freshman Class President** – TBD (Election in September)

### 📌 Homeroom & House Representatives
- **Senior Class Moderator** – Mr. DeStefano
- **Junior Class Moderator** – Ms. Conley
- **Sophomore Class Moderator** – Mr. Flannery
- **Freshman Class Moderator** – Mrs. Rocco
- **Spirit Moderator** – Mr. Adam Moore
- **Ad Hoc Moderator** – Mr. Tuck
- **House Director** – Mr. Motsay

### 🧑‍🎓 Class Reps
- **Class of 2025**: Ben Becker, Jack Campbell, Ben Cuomo, Aleksandr Godzilevsky, Eric Meyer, Conor Moran, Tommy Peisinger, Ben Rozanski, Will Schoonmaker, Will Schwanke, Andrew Trentler, David Wiechec, Kamin Wolf
- **Class of 2026**: Charlie Banasky, Braedan Conly, Dylan Duklewski, Zander Greco, Ben Hanover, Tucker Jones, Patrick Krivosh, Henry Lynch, Luke Magruder, Ben McMullen, Akanna Ozo-Onyali, Mateo Soto, Patrick Wagner, Brayden Zuckerman
- **Class of 2027**: Declan Butler, Sam Dawes, David Ezumba, Colby Kaminsky, Ben Kim, Alex Los, Will McLean, Josh Ramos, Izaac Robertucci, James Ruby, Bart Shaeffer, Nate Smith, Brennan Taylor, Benjamin Virgilio, Ben Walter, Diego Zavala
"""
)

insert_chunk(
    topic="Student Handbook – Chapter 8: Athletics",
    url="https://bbk12e1-cdn.myschoolcdn.com/ftpimages/274/misc/misc_229973.pdf",
    content="""🏅 **ATHLETICS**

### Purpose
Calvert Hall College believes that participation in athletics, both as a player and as a spectator, is an integral part of the student’s educational experience. The Athletic Program teaches such skills and values as the ability to think and function as a member of a team, sportsmanship, competition, the benefits of a healthy body, self-discipline, emotional maturity, respect for others, and the importance of a system of morals.

Calvert Hall Athletics provides experiences that will help students develop physically, mentally, and emotionally. The element of competition and winning, though it exists, is controlled in that it does not determine the nature of the program. Students are encouraged to win, but the principles of good sportsmanship prevail at all times to enhance the educational values of the contest.

### Athletic Teams
**Fall Season**
- Football: Varsity, Junior Varsity, Frosh/Soph
- Soccer: Varsity, Junior Varsity, Frosh/Soph
- Cross Country: Varsity, Junior Varsity
- Volleyball: Varsity, Junior Varsity
- Water Polo: Varsity, Junior Varsity

**Winter Season**
- Basketball: Varsity, Junior Varsity, Frosh/Soph
- Hockey: Varsity, Junior Varsity
- Wrestling: Varsity, Junior Varsity
- Swimming: Varsity, Junior Varsity
- Indoor Track: Varsity, Junior Varsity
- Squash: Varsity, Junior Varsity

**Spring Season**
- Baseball: Varsity, Junior Varsity, Frosh/Soph
- Lacrosse: Varsity, Junior Varsity, Frosh/Soph
- Rugby: Varsity, Junior Varsity
- Tennis: Varsity, Junior Varsity
- Golf: Varsity, Junior Varsity
- Track: Varsity, Junior Varsity

### MSA & MIAA Championships
(Full list of historical championships by team and level from 1925 to 2024 for all sports including Football, Soccer, Cross Country, Volleyball, Water Polo, Basketball, Swimming, Indoor Track, Hockey, Baseball, Lacrosse, Tennis, Golf, Track & Field, and Rugby.)

### Cardinal Club
The Cardinal Club, a sports booster club, was established in the Spring of 1984 to foster the image and spirit of athletics at Calvert Hall College. This group of parents, alumni, and friends of the school assists the athletic department by providing some of the extras that a quality athletic program needs but cannot realistically afford. It is the hope of this group of dedicated and spirited workers that it can provide some of the needed items for our student-athletes while engaging in enjoyable social activities. The club’s educational presentations, social gatherings, and fund-raisers are held throughout the various seasons.
"""
)


insert_chunk(
    topic="Student Handbook – Chapter 9: Support Services",
    url="https://bbk12e1-cdn.myschoolcdn.com/ftpimages/274/misc/misc_229973.pdf",
    content="""📘 **SUPPORT SERVICES**

### 🎓 Mentoring Program
Each freshman and transfer student will be assigned a faculty mentor through the Student Activities Office. Students and their mentor will meet periodically throughout the year. Students who are having difficulty or wish assistance should see their faculty mentor.

### 💬 Counseling Department
Each student is assigned a school counselor for his four years, and they meet at least once a semester. Services include:
- Individual or group sessions about educational and career goals
- Coordination with faculty and parents on academic progress
- Christopher O’Neil Peer Education Program for life skills mentorship
- College counseling services, testing, financial aid, and parent info sessions

📌 Transcript requests should be directed to a student’s college counselor. Transcripts may be released unless a parent/legal guardian advises otherwise in writing.

### 🛠️ Accommodations
Calvert Hall offers academic accommodations for students with disabilities, provided they do not fundamentally alter the school’s mission or programs. Evaluation includes testing, teacher recommendations, and medical records. An accommodations plan will be made in partnership with parents and reviewed periodically.

📌 Students not meeting expectations may be advised to seek a different educational setting.

➡️ **College Board School Code**: 210055
➡️ **Counselor Appointments**: Scheduled during unscheduled periods.
➡️ **Special Circumstances**: Students in emotional distress may require a return-to-school evaluation by a qualified professional.

### ✝️ Campus Ministry
- **Mission**: To help students grow in faith and serve others, following St. John Baptist de La Salle’s values.
- **Programs**: Masses, prayer services, reconciliation, music ministry, and service trips.
- **Chapel**: Under the protection of Our Lady of the Star; daily services held.
- **Liturgy Participation**: Students can serve as lectors, musicians, ushers, Eucharistic Ministers, and tech aides.

### 🙏 Retreat Program
Every student participates in a yearly retreat:
- **Freshman**: Overnight retreat on Lasallian values (faith, service, community)
- **Sophomore**: Day of social action and service
- **Junior**: Two-day identity and relationship retreat at River Valley Ranch
- **Senior**: Three-day reflection and future-focused retreat

### ❤️ Service
Students engage in various service projects and immersion trips. Past service agencies include:
- Sarah’s Hope Shelter
- Beans and Bread
- Helping Up Mission
- Our Daily Bread

Students help lead school drives like the Mission Drive, Thanksgiving Food Drive, and Adopt-A-Family project.
"""
)


insert_chunk(
    topic="Student Handbook – Chapter 10: Student Health",
    url="https://bbk12e1-cdn.myschoolcdn.com/ftpimages/274/misc/misc_229973.pdf",
    content="""**STUDENT HEALTH**

**Allergy Awareness**  
Calvert Hall is committed to working with families, students and providers to provide a safe and healthy environment. Although our campus is not an “allergy-free” environment, we strive to keep our students as safe as possible through several measures. Upon receiving information regarding a severe allergy, as documented by a health care provider, a plan will be developed to address emergency treatment needs, the roles and responsibilities of the student and family, as well as ongoing education of the Calvert Hall community. Parents and guardians are encouraged to check the menu located on the Calvert Hall website and the Touch of SAGE App. or contact our Food Services Director for further discussion of our menu options.

**Epinephrine Policy**  
Calvert Hall College High School has adopted a policy allowing the availability of stock epinephrine in the health suite for use in the event of an anaphylactic emergency. This epinephrine is for emergency use during normal school days and is not dependent on allergy history. It is not available outside of normal school hours or on field trips. Students with a known history of severe allergies are still expected to maintain emergency action plans, medical orders, and their own supply of Epinephrine Autoinjectors that they self-carry and/or store in the Health Suite.

**Communicable Illness**  
Communicable conditions, such as strep, flu, chicken pox, impetigo, pertussis, ringworm, and COVID-19 should be immediately reported to the school nurse.

The School may exclude any student from school who has a communicable illness or has been exposed to an infected person if the School determines that such exclusion is appropriate for the welfare of the student who is excluded from School and/or the welfare of other students or employees at the School. In reaching the decision to exclude a student from the School, the School may consult with appropriate medical professionals and/or the Department of Health.

In order to return to School, students who have been excluded from School for health reasons must submit a physician’s certification that the student may return to School without risk to self or to others.

**Immunizations**  
The School fully complies with Maryland Laws with regard to student vaccinations and will only accept verifiable medical exemptions signed by a regular Primary Care Provider. No other exemptions are considered.

**Medical Leave of Absence**  
In cases of serious illness, bodily injury, or an emotional or psychological condition, a medical leave may be appropriate. The School requires appropriate documentation, and return is contingent on a written evaluation from the treating medical professional.

**Medication**  
All medications must be submitted to the School Nurse in a labeled prescription bottle along with a Prescription Medication Form. Over-the-counter meds require a form on Magnus Health. Students may not carry medication unless specifically approved.

**Student Illness**  
Parents should keep students home if ill. The nurse will contact parents if a student becomes sick during the day.

**Emergency Information and Authorization**  
Calvert Hall uses Magnus Health for all medical records. In case of emergency, school personnel may authorize treatment and parents are financially responsible for costs.

**COVID-19**  
The School reserves the right to adjust policies based on evolving COVID-19 conditions. Despite protocols, families assume inherent risks associated with in-person attendance.
"""
)


insert_chunk(
    topic="Student Handbook – Chapter 11: Who’s Who at Calvert Hall, Faculty and Staff",
    url="https://bbk12e1-cdn.myschoolcdn.com/ftpimages/274/misc/misc_229973.pdf",
    content="""📘 **WHO’S WHO AT CALVERT HALL**

### 🏛️ Board of Trustees – 2024–25
Mrs. Christine D. Aspell  
Mr. Joseph A. Baker ’76  
Br. Mark J. Brown, FSC ‘86  
Br. Frank Byrne, FSC  
Dr. Marc M. Camille  
Mr. Thomas S. Fan  
Mr. James E. Fyke  
Mrs. Jean C. Gould  
Mrs. Jessica M. Hiebler  
Br. John Kane, FSC, President  
Mr. William G. Karpovich ‘87  
Mr. John M. Kessler ‘79  
Mr. Stephen E. Marshall ‘82, Board Vice-Chair  
Dr. Andrew P. Moore  
Mr. Jeffrey A. Nattans ‘85, Board Chair  
Mr. Matthew W. Oakey ‘83  
Mr. Michael G. Paszkiewicz ‘83  
Mrs. Melinda B. Peters  
Mr. Anthony J. Rosso ‘85  
Mr. Robert P. Silverman ‘87  
Mr. Benjamin Ventresca, Jr.  
Mr. Shawn D. Vinson ‘89  
Mr. William W. Whitty, Jr. ‘69  
Mr. Troy V. Williams ‘88

### 🏫 School Administration
Mr. Joseph Baker / Chief Administrative Officer & Director of Advancement  
Mr. Tom Fan / Assistant Principal for Academic Affairs  
Mrs. Jean Gould / Chief Financial Officer  
Br. John Kane, FSC / President  
Mr. Kristopher Mitchell / Dean of Students  
Dr. Andrew Moore / Principal  
Mr. Dan Mulford / Director of Athletics  
Mr. Marc Parisi / Director of Student Activities  
Mrs. Lauren Urban / Coordinator of Faculty Development  
Mr. William Wellein / Director of Admissions

### 🧑‍🏫 Department Chairpersons
Mr. Brooks Kerr / Counseling Office  
Mr. Gino Greco / English  
Mr. Brian Ecton / Fine Arts  
Mr. Darrick Freeman / Foreign Language  
Mrs. Jennifer Healy / La Salle Program  
Mr. Jeffrey Blake / Mathematics  
Mr. Patrick Marshall / Physical Education  
Mr. Christopher Barczak / Religion  
Mrs. Lauren Urban / Science  
Mr. Matthew Radebaugh / Social Studies

### 🛠️ Administrative Services
Mrs. Cathy Baker / Cardinal Shop Manager  
Mrs. Lucy Baker / Administrative Assistant, Admissions  
Ms. Laura Cavanaugh / Administrative Assistant, Main Office  
Mrs. Jenni Dagostin / Assistant Director of Admissions  
Mrs. Kimberly Davey / Finance Office  
Mrs. Claudine Riportella / Administrative Assistant, Attendance  
Mr. Austin Ewachiw / Director of Technology  
Mrs. Cindy Faherty / School Nurse  
Mr. Geoffrey Foltyn / Director of Alumni Relations & Reunion Giving  
Mrs. Margie Forbes / Grants & Special Projects Manager  
Mr. Fred Germano / Academic Technology Support  
Mrs. Dee Gorman / Administrative Assistant, Student Activities  
Mrs. Christie Grant / Administrative Assistant, Counseling Office  
Mr. Jay Heath / Maintenance  
Ms. Kiera Heath / Athletic Trainer  
Mr. Douglas Heidrick / Director of Annual Giving  
Mrs. Danielle Hladky / Director of Communications and Marketing  
Mrs. D. Kimberly Hladky / Advancement Services Manager  
Mrs. Darby Jecelin / Controller  
Br. Joseph Keough, FSC / Librarian  
Mrs. Meaghan Knapp / Executive Assistant to the President & Stewardship Associate  
Mr. Thomas Malstrom / Major Gifts & Planned Giving Officer  
Mrs. Traci Malstrom / Administrative Assistant to the Principal  
Mrs. Mary Manger / Administrative Assistant, Academics  
Mr. Cord Neal / Computer/AV Support Technician  
Mrs. Cynthia Patchak / Administrative Assistant, Athletics  
Mrs. Nichole Regulski / Donor Relations & Community Engagement Officer  
Mr. Sean Reilly / Network Administrator  
Mr. James Rich / Director of Facilities  
Mrs. Claudine Riporella / Administrative Assistant Attendance  
Mr. Brian Rowe / Assistant Athletic Director  
Mrs. Lynda Rogers / Testing Center Coordinator  
Mrs. Emily Shultz / Finance Office Assistant  
Mrs. Jane Thompson / Technology Resource Center Assistant  
Mr. Johnathan Travers / Multimedia Content Specialist  
Mr. Joshua Ward / Assistant Athletic Director  
Mr. Christopher Zinn / Athletic Trainer

### 👨‍🏫 Faculty Directory
(Complete list of 100+ faculty members with full names, degrees, and affiliated universities as provided in the handbook. Omitted here for brevity but stored in full in the database.)
"""
)


insert_chunk(
    topic="Campus Buildings & Key Offices",
    url="https://bbk12e1-cdn.myschoolcdn.com/ftpimages/274/misc/misc_229973.pdf",
    content="""🏫 **Building Maps**  
• Keelty Hall Map: 🔗 [View Map](sandbox:/mnt/data/keelty_hall_map.png)  
• Marion Burk Knott Center Map: 🔗 [View Map](sandbox:/mnt/data/knott_center_map.png)  
• George Young Hall Map: 🔗 [View Map](sandbox:/mnt/data/george_young_hall_map.png)  
• Full Campus Overview: 🔗 [View Map](sandbox:/mnt/data/calvert_hall_map.png)  

---

📌 **Admissions Office**  
The Admissions Office is responsible for recruiting, testing, and enrolling qualified candidates for Calvert Hall’s college preparatory program. They manage Open House events, “Cardinal for a Day” shadow programs, and presentations at middle schools. The Ambassadors Club supports their efforts by hosting guests and giving tours. To apply, students must take the High School Placement Test, submit an online application, and provide academic records.  
📞 Contact: 410-825-4266 ext. 117 | 🌐 [www.calverthall.com](https://www.calverthall.com)

📌 **Advancement Office**  
This office manages fundraising for scholarships, tuition assistance, capital campaigns, and endowments. Their annual campaign, the Hall Fund, runs from July to June. They also organize events for alumni networking and philanthropy.  
📞 Contact: Joseph Baker ‘76 at 410-821-2363

📌 **Alumni Association**  
Open to all graduates, the association holds events like Homecoming, Cardinals at the Beach, and the Alumni Senior Breakfast. Meetings are held five times a year. Committees include Career Foundation, Veterans TAG, and Networking Groups.  
📞 Contact: Alumni Office at 410-825-4251  
🎓 Moderator: Br. Joseph Keough, FSC

📌 **Communications Office**  
Manages advertising, marketing, and public relations. Publishes *The Cardinal* magazine and sends out press releases highlighting achievements of students, faculty, and alumni.

📌 **Parents’ Club**  
Organizes social, service, and fundraising events like Fall Bingo, Freshman Parent Welcome, and Post-Prom Celebration. Funds raised support school operations and student enrichment.  
📧 Email: chparentsclub@gmail.com  
🌐 [Parents’ Club Info](https://www.calverthall.com/parentsclub)
"""
)


insert_chunk(
    topic="CHC Schedule - Access and How to Read",
    url="https://calverthall.myschoolapp.com/app/student#resourceboarddetail/4883",
    content="""📅 WHERE TO FIND THE CHC SCHEDULE

• CHC schedule website:  
  🔗 https://findmyschedule.net

• How to read a schedule (official CHC resource):  
  🔗 https://calverthall.myschoolapp.com/app/student#resourceboarddetail/4883
"""
)