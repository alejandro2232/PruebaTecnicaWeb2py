var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    function adopt(value) { return value instanceof P ? value : new P(function (resolve) { resolve(value); }); }
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : adopt(result.value).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};
// Class representing an API repository for student-related operations
export class RepositorioApi {
    // Asynchronously inserts student data into the server
    insertarEstudiante(estudiante) {
        return __awaiter(this, void 0, void 0, function* () {
            // Extract student data from the input parameter
            const data = estudiante;
            // Use the Fetch API to send a POST request to the server
            return yield fetch('/sistemaGestionEscolar/estudiante_controlador/procesar_formulario', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                // Convert the student data to JSON and include it in the request body
                body: JSON.stringify(data)
            })
                // Parse the response as JSON
                .then((response) => __awaiter(this, void 0, void 0, function* () { return yield response.json(); }))
                .then(data => {
                // Log the success message from the server
                console.log(data.message);
                // Return the response data
                return data;
            })
                .catch((error) => {
                // Log any errors that occur during the request
                console.log('Error:', error);
                // Return false if an error occurs
                return false;
            });
        });
    }
}
