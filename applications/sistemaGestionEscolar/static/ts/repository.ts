import { type EstudiantesModel } from './modelEstudiantes'

// Class representing an API repository for student-related operations
export class RepositorioApi {
  // Asynchronously inserts student data into the server
  async insertarEstudiante (estudiante: any): Promise<EstudiantesModel | boolean> {
    // Extract student data from the input parameter
    const data = estudiante
     // Use the Fetch API to send a POST request to the server
    return await fetch('/sistemaGestionEscolar/estudiante_controlador/procesar_formulario', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      // Convert the student data to JSON and include it in the request body
      body: JSON.stringify(data)
    })
      // Parse the response as JSON
      .then(async response => await response.json())
      .then(data => {
        // Log the success message from the server
        console.log(data.message)
        // Return the response data
        return data
      })
      .catch((error) => {
        // Log any errors that occur during the request
        console.log('Error:', error)
        // Return false if an error occurs
        return false
      })
  }
}
