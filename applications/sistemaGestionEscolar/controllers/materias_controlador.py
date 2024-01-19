"""
Controller class to handle the form events and execute the necessary actions.
"""
# -*- coding: utf-8 -*-
from render import Renderer
from factory.factoria_materia import MateriaFactory

renderizado = Renderer(db)


def admin_materias():
    """
    function in charge of creating CRUD views for the
    administration of the subject tables. Was implemented using sqlform.grid
    """
    # Creates a CRUD grid for the table 'materias' using sqlform.grid
    grid = SQLFORM.grid(db.materias, user_signature=False)

    # Returns a dictionary with the grid to be used in the view.
    return {'grid':grid}


def materias():
    """
    function in charge of using the render class to visualize the subject model.
    """
    # verify that the singleton pattern works correctly
    materia_factory1 = MateriaFactory()
    materia_factory2 = MateriaFactory()
    # Verify that both variables refer to the same instance, if
    # it is true it means that they are the same instance, therefore the singleton works.
    print(materia_factory1 is materia_factory2)
    print("El patrón Singleton funciona correctamente.")

    # Uses the render method to generate the html
    # objects and display the table of the subject model.
    materias_lista = renderizado.renderer_materias()

    # Create a dictionary of the model with the data of the subjects to be used in materias.html
    return {'materias_lista' : materias_lista}
