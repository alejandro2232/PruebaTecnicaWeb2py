import { EstudiantesModel } from './modelEstudiantes'

// Class representing a factory for creating instances of EstudiantesModel
export class EstudiantesFactory {

   // Static method to create and return an instance of EstudiantesModel
  public static crearInstancia (): EstudiantesModel {
    // Return a new instance of EstudiantesModel
    return new EstudiantesModel()
  }
}
