import { EstudiantesFactory } from "../ts/factoryEstudiantes";
import { EstudiantesModel } from "../ts/modelEstudiantes";

describe('EstudiantesFactory', () => {
    test('crearInstancia debe retornar una instancia de EstudiantesModel', () => {
      const instancia = EstudiantesFactory.crearInstancia();
      expect(instancia).toBeInstanceOf(EstudiantesModel);
    });
  });

describe('EstudiantesModel', () => {
  test('inicialización del modelo', () => {
    const estudiante = new EstudiantesModel();
    expect(estudiante.nombre).toBe('');
    expect(estudiante.apellido).toBe('');
  });

  test('setNombre debería crear el nombre correctamente', () => {
    const estudiante = new EstudiantesModel();
    estudiante.setNombre('John');
    expect(estudiante.nombre).toBe('John');
  });

  test('setApellido debería crear el apellido correctamente', () => {
    const estudiante = new EstudiantesModel();
    estudiante.setApellido('Doe');
    expect(estudiante.apellido).toBe('Doe');
  });

  test('obtenerEstudiante debería devolver un objeto con nombre y apellido', () => {
    const estudiante = new EstudiantesModel();
    estudiante.setNombre('John');
    estudiante.setApellido('Doe');
    const resultado = estudiante.obtenerEstudiante();
    expect(resultado).toEqual({ nombre: 'John', apellido: 'Doe' });
  });
});

