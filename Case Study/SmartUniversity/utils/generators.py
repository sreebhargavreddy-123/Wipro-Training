def student_generator(students):
    for s in students:
        yield f"{s.id} - {s.name}"

