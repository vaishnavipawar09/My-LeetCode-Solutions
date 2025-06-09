-- Select patients whose conditions include a standalone word starting with 'DIAB1'
SELECT 
    patient_id, 
    patient_name, 
    conditions
FROM Patients
-- Use REGEXP to ensure 'DIAB1' starts a space-separated condition
WHERE conditions REGEXP '(^| )DIAB1[^ ]*($| )';
