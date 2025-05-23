# Write your MySQL query statement below
SELECT s.student_id, s.student_name, sb.subject_name, COUNT(e.student_id) AS attended_exams
FROM Students s
CROSS JOIN Subjects sb 
LEFT JOIN Examinations e
ON sb.subject_name = e.subject_name AND s.student_id = e.student_id
GROUP BY s.student_id, s.student_name, sb.subject_name
ORDER BY s.student_id, sb.subject_name;