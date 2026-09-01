# 📘 Assignment: Database Basics with SQLite

## 🎯 Objective

Learn how to create, populate, and query a SQLite database in Python by building a simple student records system.

## 📝 Tasks

### 🛠️ Create the database and schema

#### Description
Create a SQLite database and define a `students` table that stores student names, IDs, and grades.

#### Requirements
Completed program should:

- Create a SQLite database file named `students.db`.
- Define a table named `students` with at least these columns:
  - `id` (integer primary key)
  - `name` (text)
  - `grade` (integer)
- Use Python's `sqlite3` module to connect to the database.
- Run the table creation code once so the database is ready for data.

### 🛠️ Add student records

#### Description
Insert several sample student records into the database and make sure the data is saved correctly.

#### Requirements
Completed program should:

- Add at least 5 student records.
- Insert each student with a unique ID, a name, and a grade.
- Confirm that the insert statements execute successfully.
- Example data:
  ```python
  (1, "Ava", 92)
  (2, "Leo", 88)
  (3, "Mia", 95)
  (4, "Noah", 81)
  (5, "Zoe", 90)
  ```

### 🛠️ Query and analyze the data

#### Description
Write queries to read the stored records and calculate simple statistics.

#### Requirements
Completed program should:

- Display all rows in the `students` table.
- Find the student with the highest grade.
- Calculate the average grade across all students.
- Print a student report using at least one `SELECT` statement with filtering or sorting.
- Example output:
  ```python
  Highest grade: Mia (95)
  Average grade: 89.2
  ```

