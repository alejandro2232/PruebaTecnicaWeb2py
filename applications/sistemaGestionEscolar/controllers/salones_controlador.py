"""
Controller class to handle the form events and execute the necessary actions.
"""

# -*- coding: utf-8 -*-
from render import Renderer
from factory.factoria_salones import SalonesFactory

renderizado = Renderer(db)


def admin_salones():
    """
    function in charge of creating CRUD views for the
    administration of the classroom tables. Was implemented using sqlform.grid
    """
    # Creates a CRUD grid for the table 'salones' using sqlform.grid
    grid = SQLFORM.grid(db.salones, user_signature=False)
    # Returns a dictionary with the grid to be used in the view.
    return {'grid':grid}


def salones():
    """
    function in charge of using the render class to visualize the subject model.
    """
    # verify that the singleton pattern works correctly
    salones_factory1 = SalonesFactory()
    salones_factory2 = SalonesFactory()
    # Verify that both variables refer to the same instance, if
    # it is true it means that they are the same instance, therefore the singleton works.
    print(salones_factory1 is salones_factory2)
    print("El patrón Singleton funciona correctamente.")

    # Uses the render method to generate the html
    # objects and display the table of the subject model.
    salones_lista = renderizado.renderer_salones()

    # Create a dictionary of the model with the data of the subjects to be used in materias.html
    return {'salones_lista': salones_lista}
