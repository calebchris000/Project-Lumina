from pydantic import BaseModel


class StudentGradeIn(BaseModel):
    student_id: int
    subject_id: int
    grade: float
