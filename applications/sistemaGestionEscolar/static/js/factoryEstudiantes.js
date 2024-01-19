import { EstudiantesModel } from './modelEstudiantes.js';

// Class representing a factory for creating instances of EstudiantesModel
export class EstudiantesFactory {
    // Static method to create and return an instance of EstudiantesModel
    static crearInstancia() {
        // Return a new instance of EstudiantesModel
        return new EstudiantesModel();
    }
}
