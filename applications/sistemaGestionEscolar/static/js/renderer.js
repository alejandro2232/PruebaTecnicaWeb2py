// Class representing a renderer for a student registration form
export class FormularioRender {
    // Constructor that takes the ID of the container element
    constructor(containerId) {
        // Set the container property using the provided container ID
        this.container = document.getElementById(containerId);
    }
    // Method to render the student registration form
    renderer() {
        // HTML template for the student registration form
        const formularioHTML = `
        <div class="container mt-5">
        <div class="row justify-content-center">
        <div class="col-md-6">
            <h1>Registro de estudiantes</h1>    
                    <form id="registroEstudiantes" action="">
                        <div class="form-group">
                            <label for="nombre">Nombre</label>
                            <input type="text" class="form-control" id="nombre" name="nombre" required>
                        </div>
                        <div class="form-group">
                            <label for="apellido">Apellido</label>
                            <input type="text" class="form-control" id="apellido" name="apellido" required>
                        </div>
                        <button type="submit" class="btn btn-primary">Registrar Estudiantes</button>
                    </form>
                </div>
            </div>
        </div>`;
        // Check if the container element exists
        if (this.container != null) {
            // Set the inner HTML of the container with the form template
            this.container.innerHTML = formularioHTML;
        }
    }
}
