"""
File containing the repository class that
calls the api for the registration of the student information.
"""

class EstudiantesRepository:
    """
    Repository class for managing student data in the database.
    """

    def __init__(self, db):
        """
        Initialize the repository with a database connection.

        Args:
            db: The database object being used.
        """
        self.db = db

    def create_estudiante(self, nombre, apellido):
        """
        Create a new student record in the database.

        Args:
            nombre (str): The student's name.
            apellido (str): The student's last name.

        Returns:
            int: The ID of the newly created student record.
        """
        return self.db.estudiantes.insert(nombre=nombre, apellido=apellido)

    def get_estudiantes(self):
        """
        Retrieve all student records from the database.

        Returns:
            Row: A Row object containing all student records.
        """
        return self.db(self.db.estudiantes).select()

    def get_estudiante(self, estudiante_id):
        """
        Retrieve a specific student record from the database.

        Args:
            estudiante_id (int): The ID of the student.

        Returns:
            Row: A Row object representing the student record.
        """
        return self.db(self.db.estudiantes.id == estudiante_id).select().first()

    def update_estudiante(self, id_estudiante, estado_param):
        """
        Updates the attendance status of a particular student in the database.

        Args:
            student_id (int): the ID of the student to update.
            param_status (str): The new status of the student.

        Returns:
            bool: True if the update was successful, False otherwise.
        """
        estudiante = self.get_estudiante(id_estudiante)

        if estudiante:
            estudiante.update_record(estado=estado_param)
            return True
        return False
