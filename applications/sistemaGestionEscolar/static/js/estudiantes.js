var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    function adopt(value) { return value instanceof P ? value : new P(function (resolve) { resolve(value); }); }
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : adopt(result.value).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};
import { EstudiantesFactory } from './factoryEstudiantes.js';
import { FormularioRender } from './renderer.js';
import { RepositorioApi } from './repository.js';
export class ApiEstudiantes {
    // Method to render the student registration form
    renderizarFormulario() {
        const generarFormulario = new FormularioRender('formulario-container');
        generarFormulario.renderer();
    }
    // Method to register students based on form data
    registrarEstudiantes(event) {
        return __awaiter(this, void 0, void 0, function* () {
            event.preventDefault();
            // Access form input fields
            const campoNombreElement = document.querySelector('#nombre');
            const campoNombre = campoNombreElement;
            const campoApellidoElement = document.querySelector('#apellido');
            const campoApellido = campoApellidoElement;
            // Extract form data using FormData
            const formData = new FormData(event.target);
            const nombreEstudiante = formData.get('nombre');
            const apellidoEstudiante = formData.get('apellido');
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
                alert('La longitud del nombre y el apellido no debe superar los 30 caracteres');
                return;
            }
            // Create an instance of the EstudiantesFactory and set student details
            const formulario = EstudiantesFactory.crearInstancia();
            formulario.setNombre(nombreEstudiante);
            formulario.setApellido(apellidoEstudiante);
            // Get student data from the factory instance
            const data = formulario.obtenerEstudiante();
            // Create an instance of RepositorioApi and insert the student data
            const repositorio = new RepositorioApi();
            try {
                yield repositorio.insertarEstudiante(data);
                // Resto del código...
            }
            catch (error) {
                console.error('Error al insertar estudiante:', error);
            }
            // Clear form input fields after registration
            if (campoNombre !== null && campoApellido !== null) {
                campoNombre.value = '';
                campoApellido.value = '';
            }
        });
    }
}
// Event listener to execute code after the DOM content is loaded
document.addEventListener('DOMContentLoaded', function () {
    // Create an instance of ApiEstudiantes
    const apiEstudiantes = new ApiEstudiantes();
    // Render the student registration form
    apiEstudiantes.renderizarFormulario();
    // Attach form submission event handler
    const formulario = document.getElementById('registroEstudiantes');
    if (formulario !== null) {
        // eslint-disable-next-line @typescript-eslint/unbound-method
        formulario.onsubmit = apiEstudiantes.registrarEstudiantes;
    }
});
