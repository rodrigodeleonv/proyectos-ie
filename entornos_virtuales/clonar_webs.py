"""Usando una libreria para clonar sitios web"""

import os
from pywebcopy import save_website


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(BASE_DIR, 'web_clonadas')

kwargs = {'project_name': 'usac'}

save_website(
    url='https://portal.ingenieria.usac.edu.gt/',
    project_folder=path,
    **kwargs
)
