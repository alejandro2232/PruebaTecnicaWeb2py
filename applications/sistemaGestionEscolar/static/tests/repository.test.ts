import { RepositorioApi } from "../ts/repository";

describe('RepositorioApi', () => {
  test('insertarEstudiante devolvera true al procesar correctamente', async () => {
    // Arrange
    const mockEstudiante = {nombre: "Daniel", apellido: 'Soraca'};
    const mockResponse = {message: 'Formulario procesado con éxito'};

    global.fetch = jest.fn().mockResolvedValue({
      json: jest.fn().mockResolvedValue(mockResponse),
    });


    const repo = new RepositorioApi();
    const resultado = await repo.insertarEstudiante(mockEstudiante);

    // Assert
    expect(resultado).toEqual(mockResponse);
  });

  test('insertarEstudiante devolvera false al encontrar un error', async () => {
    // Arrange
    const mockEstudiante = {nombre: "Daniel", apellido: 'Soraca'};
    const mockResponse = false;

    global.fetch = jest.fn().mockRejectedValue(mockResponse);

    const repo = new RepositorioApi();
    const resultado = await repo.insertarEstudiante(mockEstudiante);

    // Assert
    expect(resultado).toEqual(false);
  });

})