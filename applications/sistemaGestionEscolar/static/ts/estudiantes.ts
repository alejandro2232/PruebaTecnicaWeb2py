import { EstudiantesFactory } from './factoryEstudiantes.js'
import { FormularioRender } from './renderer.js'
import { RepositorioApi } from './repository.js'

export class ApiEstudiantes {
  // Method to render the student registration form
  renderizarFormulario (): void {
    const generarFormulario = new FormularioRender('formulario-container')
    generarFormulario.renderer()
  }

  // Method to register students based on form data
  async registrarEstudiantes (event: any): Promise<void> {
    event.preventDefault()
    // Access form input fields
    const campoNombreElement = document.querySelector('#nombre')
    const campoNombre = campoNombreElement as HTMLInputElement | null

    const campoApellidoElement = document.querySelector('#apellido')
    const campoApellido = campoApellidoElement as HTMLInputElement | null

    // Extract form data using FormData
    const formData = new FormData((event as Event).target as HTMLFormElement)
    const nombreEstudiante = formData.get('nombre') as string
    const apellidoEstudiante = formData.get('apellido') as string

    // Validate form data

    if (nombreEstudiante === '' || apellidoEstudiante === '') {
      alert('Por favor, complete todos los campos correctamente');
      return;
    }
    
    const contieneNumeros = /\d/.test(nombreEstudiante) || /\d/.test(apellidoEstudiante);
    
    if (contieneNumeros) {
      alert('Por favor, no ingrese números');
      return;
    }

    if (nombreEstudiante.length > 30 || apellidoEstudiante.length > 30) {
      alert('La longitud del nombre y el apellido no debe superar los 50 caracteres');
      return;
    }

    // Create an instance of the EstudiantesFactory and set student details
    const formulario = EstudiantesFactory.crearInstancia()
    formulario.setNombre(nombreEstudiante)
    formulario.setApellido(apellidoEstudiante)
    // Get student data from the factory instance
    const data = formulario.obtenerEstudiante()

    // Create an instance of RepositorioApi and insert the student data
    const repositorio = new RepositorioApi()
    try {
      await repositorio.insertarEstudiante(data)
      // Resto del código...
    } catch (error) {
      console.error('Error al insertar estudiante:', error)
    }

    // Clear form input fields after registration
    if (campoNombre !== null && campoApellido !== null) {
      campoNombre.value = ''
      campoApellido.value = ''
    }
  }
}

// Event listener to execute code after the DOM content is loaded
document.addEventListener('DOMContentLoaded', function () {
  // Create an instance of ApiEstudiantes
  const apiEstudiantes = new ApiEstudiantes()
  // Render the student registration form
  apiEstudiantes.renderizarFormulario()

  // Attach form submission event handler
  const formulario = document.getElementById('registroEstudiantes')
  if (formulario !== null) {
    // eslint-disable-next-line @typescript-eslint/unbound-method
    formulario.onsubmit = apiEstudiantes.registrarEstudiantes
  }
})
