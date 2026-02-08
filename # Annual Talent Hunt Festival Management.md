# Annual Talent Hunt Festival Management System

## 1. Project Overview
This project is a high-level Python-based school management system developed to automate the coordination of the **Annual Talent Hunt Festival**. The system handles the end-to-end lifecycle of a festival: from parsing raw participant data and verifying eligibility criteria to organizing activities and generating grade-wise result reports. 

The implementation strictly adheres to **Object-Oriented Programming (OOP)** principles, specifically focusing on multi-level inheritance, data encapsulation via name mangling, and polymorphic behavior across specialized student and activity classes.

---

## 2. System Hierarchy & Inheritance
The architecture is designed using a "Base-to-Specialized" approach, allowing for clean data transitions between general participants and niche competition roles.

### 2.1 Participant Hierarchy
The `Participant` class acts as the root of the hierarchy, ensuring every person in the system has a standardized identity record.

* **Participant (Base Class)**: Defines core identity attributes (Name, ID) and encapsulates sensitive biological data (Birth Date, Gender).
* **Teacher (Subclass)**: Inherits from Participant. Extends the model with attributes for `subject` expertise, `mentor_grade`, and `judge` status.
* **Student (Subclass)**: Inherits from Participant. Acts as a container for academic and performance scores like `gpa`, `talent_score`, and `athletic_score`.
    * **Artist**: A specialized Student focused on creativity. Eligibility: **Age ≥ 16** AND **GPA > 6.0**.
    * **Athlete**: A specialized Student focused on physical performance. Eligibility: **GPA > 5.5** AND **Age ≥ 12**.
    * **Scholar**: A specialized Student focused on academic excellence. Eligibility: **Age ≥ 10**, **GPA ≥ 8.0**, and at least one **Olympiad score > 80**.

### 2.2 Activity Hierarchy
Activities are modeled to handle different types of competition logic, ensuring that a Talent Show is evaluated differently than a Math Olympiad.

* **Activity (Base Class)**: The central manager for event metadata, including participant rosters, teacher organizers, and `is_active` status.
* **SportsTournament**: Handles "Individual" or "Team" games. For team events, the class average of `compute_scores()` determines the winner.
* **TalentShow**: Specifically processes `Artist` objects to identify the top performer in creative categories.
* **AcademicCompetition**: Specifically processes `Scholar` objects, weighing Olympiad scores against GPA.

---

## 3. Comprehensive Class Member Reference

### 3.1 Participant Classes
| Member Name | Type | Class | Description |
| :--- | :--- | :--- | :--- |
| `name` | String | Participant | The full name of the individual. |
| `__birth_year` | Int | Participant | Private (mangled) year of birth used for age validation. |
| `calculate_age` | Method | Participant | Validates date boundaries (1-31, 1-12) and returns age; returns -1 for errors. |
| `__mentor_grade`| Int | Teacher | The grade level (6-12) the teacher is assigned to mentor. |
| `__gpa` | Float | Student | Grade Point Average; must be $\ge 5.0$ for any festival participation. |
| `compute_scores` | Method | Scholar | Complexity Logic: `sum(olympiad_scores) * (gpa * 10)`. |

### 3.2 Activity Classes
| Member Name | Type | Class | Description |
| :--- | :--- | :--- | :--- |
| `__max_participants` | Int | Activity | The registration limit; exceeds this and the activity marks as full. |
| `__is_active` | Bool | Activity | Status flag; requires at least 2 students to be considered active. |
| `determine_winner` | Method | SportsTournament | Logic branches based on the "Game Type" (Individual vs Team). |
| `evaluate_talent`| Method | TalentShow | Identifies the Artist with the highest computed performance level. |

---

## 4. Implementation Logic & Data Processing Flow

The system processes data through four distinct, sequential stages to ensure robust results:

### 4.1 Data Ingestion & Sanitation
The functions `load_participant_data()` and `load_activities_data()` parse the source CSV files. The system uses a `set_values()` dictionary-mapping approach to populate objects. If any data attribute (like a birth day of 32) fails the internal sanitation check, the system returns `-1` to prevent data corruption.

### 4.2 Specialized Object Mapping
The `specialised_students()` function performs a second-pass analysis of the student list. It converts generic `Student` objects into their specialized forms (`Artist`, `Athlete`, or `Scholar`) based on their `selected_activity`. Simultaneously, it generates grade-specific sub-reports (e.g., `class9-athlete.csv`) containing the computed scores for every eligible student in that category.

### 4.3 Activity Registration & Eligibility
In `register_activity()`, the system performs complex matching:
1. **Teacher Assignment**: Mentors are assigned to lead activities that match their `mentor_grade`.
2. **Eligibility Filtering**: Students are added to rosters only if they pass the category-specific `is_eligible()` checks.
3. **Activity Activation**: The system counts the final roster. If an activity has fewer than 2 participants, it is automatically marked inactive.

### 4.4 Result Compilation (Final Stage)
The `winner()` function iterates through Grades 6 to 12. For each grade, it generates a `gradeX.csv` file. The function checks for winners in a fixed sequence: Cricket, Chess, Mathematics, Science, Computers, and Blackrose. If an activity is active, it records the winner's `idi`; otherwise, it outputs "NA".

---

## 5. Complexity & Performance Analysis

| Operation | Time Complexity | Space Complexity | Technical Context |
| :--- | :--- | :--- | :--- |
| **Participant Parsing** | $O(N)$ | $O(N)$ | $N$ = total participants. Linear scan of CSV rows. |
| **Activity Mapping** | $O(A \times (N+T))$ | $O(N+T)$ | $A$ = activities. Nested loops for roster matching. |
| **Result Generation** | $O(G \times C)$ | $O(1)$ | $G$ = 7 grades, $C$ = 6 competitions. Efficient final write. |

---

## 6. Technical Safeguards & Developer Notes

* **Name Mangling**: To satisfy the requirement for private members, attributes like `__birth_day` are automatically transformed to `_Participant__birth_day`. This prevents accidental external modification and maintains data integrity.
* **Polymorphism**: Every class implements its own version of `show_values()` and `get_values()`. This allows the system to print the specific details of a Scholar (like Olympiad scores) using the same function call used for a Teacher (subject/grade).
* **Reference Integrity**: The tuple returned by `register_activity` ensures that activity data remains immutable during the final winner determination phase.

---

## 7. Setup & Execution Instructions

1. **Environment**: Ensure Python 3.8 or higher is installed.
2. **File Placement**: Ensure `easy_participant_data.csv` and `easy_activity_data.csv` are in the folder.
3. **Execution**:
   ```bash
   python 2024ME10805_Assignment_5_q5.8.py

## 8. Author
**Name**: Prasanna Prasad Mahajan
**Entry No**: 2024EE10805
**Department**: Electrical Engineering, IIT Delhi