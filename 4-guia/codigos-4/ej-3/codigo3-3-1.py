import numpy as np
import matplotlib.pyplot as plt
from numpy.ma.core import argsort
import pandas as pd  # Para leer archivos
import geopandas as gpd  # Para hacer cosas geográficas
import seaborn as sns  # Para hacer plots lindos
import networkx as nx  # Construcción de la red en NetworkX
import scipy
y = scipy.linalg.solve_triangular(L, b, lower=True, unit_diagonal=True)
p = scipy.linalg.solve_triangular(U, y, lower=False, unit_diagonal=False)
