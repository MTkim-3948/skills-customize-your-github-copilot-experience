import sqlite3


def create_connection(db_name="students.db"):
    """Create and return a connection to a SQLite database."""
    conn = sqlite3.connect(db_name)
    return conn


def create_table(conn):
    """Create the students table."""
    pass


def add_student(conn, student_id, name, grade):
    """Insert a student record into the database."""
    pass


def get_all_students(conn):
    """Return every student record from the database."""
    pass


def get_highest_grade(conn):
    """Return the student with the highest grade."""
    pass


def get_average_grade(conn):
    """Return the average grade for all students."""
    pass


if __name__ == "__main__":
    conn = create_connection()
    create_table(conn)

    # Add sample records here
    # add_student(conn, 1, "Ava", 92)
    # add_student(conn, 2, "Leo", 88)

    # Query the database here
    # print(get_all_students(conn))
    # print(get_highest_grade(conn))
    # print(get_average_grade(conn))

    conn.close()
