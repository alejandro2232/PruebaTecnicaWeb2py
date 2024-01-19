// Class representing the data model for student information
export class EstudiantesModel {
  // Public properties for the student's name and last name
  public nombre: string
  public apellido: string
  // Constructor initializes the name and last name properties
  constructor () {
    this.nombre = ''
    this.apellido = ''
  }

  // Methods to update the values of the model

  // Method to set the name of the student
  setNombre (nombre: string): void {
    this.nombre = nombre
  }

  // Method to set the last name of the student
  setApellido (apellido: string): void {
    this.apellido = apellido
  }
  // Method to retrieve the student's information as an object
  obtenerEstudiante (): { nombre: string, apellido: string } {
    return {
      nombre: this.nombre,
      apellido: this.apellido
    }
  }
}
