// Class representing the data model for student information
export class EstudiantesModel {
    // Constructor initializes the name and last name properties
    constructor() {
        this.nombre = '';
        this.apellido = '';
    }
    // Methods to update the values of the model
    // Method to set the name of the student
    setNombre(nombre) {
        this.nombre = nombre;
    }
    // Method to set the last name of the student
    setApellido(apellido) {
        this.apellido = apellido;
    }
    // Method to retrieve the student's information as an object
    obtenerEstudiante() {
        return {
            nombre: this.nombre,
            apellido: this.apellido
        };
    }
}
