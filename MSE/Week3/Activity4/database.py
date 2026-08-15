import sqlite3
import os
from datetime import date


DB_PATH = os.path.join(os.path.dirname(__file__), "w3_activity4.db")

def get_conn(path=DB_PATH):
	conn = sqlite3.connect(path)
	conn.row_factory = sqlite3.Row
	conn.execute("PRAGMA foreign_keys = ON")
	return conn


def create_tables(conn):
	cur = conn.cursor()
	cur.executescript("""
	CREATE TABLE IF NOT EXISTS lecturers (
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		name TEXT NOT NULL,
		email TEXT
	);

	CREATE TABLE IF NOT EXISTS courses (
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		code TEXT NOT NULL UNIQUE,
		name TEXT NOT NULL,
		lecturer_id INTEGER,
		FOREIGN KEY (lecturer_id) REFERENCES lecturers(id)
	);

	CREATE TABLE IF NOT EXISTS students (
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		student_id TEXT NOT NULL UNIQUE,
		name TEXT NOT NULL,
		email TEXT
	);

	CREATE TABLE IF NOT EXISTS enrolments (
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		student_id INTEGER NOT NULL,
		course_id INTEGER NOT NULL,
		enrol_date TEXT,
		FOREIGN KEY (student_id) REFERENCES students(id) ON DELETE CASCADE,
		FOREIGN KEY (course_id) REFERENCES courses(id) ON DELETE CASCADE,
		UNIQUE(student_id, course_id)
	);
	""")
	conn.commit()


def populate_sample_data(conn):
	cur = conn.cursor()

	# Clear existing data (for idempotence)
	cur.execute("DELETE FROM enrolments")
	cur.execute("DELETE FROM students")
	cur.execute("DELETE FROM courses")
	cur.execute("DELETE FROM lecturers")

	# Lecturers (2)
	lecturers = [
		("Dr. Alice Wong", "alice.wong@example.edu"),
		("Dr. Bob Smith", "bob.smith@example.edu"),
	]
	cur.executemany("INSERT INTO lecturers (name, email) VALUES (?, ?)", lecturers)

	# Courses (3)
	# Assign first two courses to lecturer 1, last course to lecturer 2
	courses = [
		("CS101", "Introduction to Programming", 1),
		("CS202", "Data Structures", 1),
		("CS303", "Databases", 2),
	]
	cur.executemany("INSERT INTO courses (code, name, lecturer_id) VALUES (?, ?, ?)", courses)

	# Students (5)
	students = [
		("S1001", "John Doe", "jdoe@example.com"),
		("S1002", "Jane Roe", "jroe@example.com"),
		("S1003", "Sam Green", "sgreen@example.com"),
		("S1004", "Lucy Liu", "lliu@example.com"),
		("S1005", "Mark Chan", "mchan@example.com"),
	]
	cur.executemany("INSERT INTO students (student_id, name, email) VALUES (?, ?, ?)", students)

	# Enrolments: create appropriate records; some students take multiple courses
	# We'll look up student and course internal IDs to be robust
	conn.commit()

	# helper to resolve ids
	def sid(student_student_id):
		r = cur.execute("SELECT id FROM students WHERE student_id = ?", (student_student_id,)).fetchone()
		return r["id"]

	def cid(course_code):
		r = cur.execute("SELECT id FROM courses WHERE code = ?", (course_code,)).fetchone()
		return r["id"]

	enrolments = [
		(sid("S1001"), cid("CS101")),
		(sid("S1001"), cid("CS202")),  # S1001 enrolled in 2 courses
		(sid("S1002"), cid("CS101")),
		(sid("S1003"), cid("CS101")),
		(sid("S1004"), cid("CS303")),
		(sid("S1005"), cid("CS202")),
		(sid("S1003"), cid("CS303")),  # S1003 enrolled in 2 courses
	]

	today = date.today().isoformat()
	cur.executemany("INSERT OR IGNORE INTO enrolments (student_id, course_id, enrol_date) VALUES (?, ?, ?)",
					[(s, c, today) for s, c in enrolments])
	conn.commit()


def query_students_per_course(conn):
	cur = conn.cursor()
	cur.execute("""
	SELECT c.code, c.name, COUNT(e.id) AS student_count
	FROM courses c
	LEFT JOIN enrolments e ON e.course_id = c.id
	GROUP BY c.id, c.code, c.name
	ORDER BY c.code
	""")
	return cur.fetchall()


def query_students_in_multiple_courses(conn):
	cur = conn.cursor()
	cur.execute("""
	SELECT s.student_id, s.name, COUNT(e.course_id) AS courses_count
	FROM students s
	JOIN enrolments e ON e.student_id = s.id
	GROUP BY s.id, s.student_id, s.name
	HAVING COUNT(e.course_id) > 1
	""")
	return cur.fetchall()


def main():
	# create/open database
	conn = get_conn()
	create_tables(conn)
	populate_sample_data(conn)

	print("Question 1: How many students are registered in each course?")
	rows = query_students_per_course(conn)
	for r in rows:
		print(f"{r['code']} - {r['name']}: {r['student_count']}")

	print("\nQuestion 2: Students enrolled in more than one course:")
	rows = query_students_in_multiple_courses(conn)
	if not rows:
		print("(none)")
	else:
		for r in rows:
			print(f"{r['name']} ({r['student_id']}) - {r['courses_count']} courses")


if __name__ == '__main__':
	main()


