from .conexion_db import ConexionDB
from tkinter import messagebox

def crear_tabla():
  conexion = ConexionDB()

  sql = '''
  CREATE TABLE pelicula(
    id_pelicula INTEGER,
    nombre VARCHAR(100),
    duracion VARCHAR(10),
    genero VARCHAR(100),
    PRIMARY KEY (id_pelicula AUTOINCREMENT)
  )
  '''
  try:
    conexion.cursor.execute(sql)
    conexion.cerrar()
    titulo = 'Crear Registro'
    mensaje = 'Se creo la tabla en la base de datos'
    messagebox.showinfo(title=titulo, message=mensaje)
  except:
    titulo = 'Crear Registro'
    mensaje = 'La tabla ya existe en la base de datos'
    messagebox.showwarning(title=titulo, message=mensaje)


def borrar_tabla():
  conexion = ConexionDB()

  sql = 'DROP TABLE pelicula'

  try:
    conexion.cursor.execute(sql)
    conexion.cerrar()

    titulo = 'Borrar Registro'
    mensaje = 'La tabla en la base de datos se borro con exito'
    messagebox.showinfo(title=titulo, message=mensaje)
  except:
    titulo = 'Borrar Registro'
    mensaje = 'No hay tabla para borrar en la base de datos'
    messagebox.showerror(title=titulo, message=mensaje)
  

class Pelicula:
  def __init__(self, nombre, duracion, genero):
    self.id_pelicula = None
    self.nombre = nombre
    self.duracion = duracion
    self.genero = genero

  def __str__(self):
    return f'Pelicula [{self.nombre}, {self.duracion}, {self.genero}]'
  
def guardar(pelicula):
  conexion = ConexionDB()

  sql = f"""
  INSERT INTO pelicula(nombre, duracion, genero)
  VALUES ('{pelicula.nombre}', '{pelicula.duracion}', '{pelicula.genero}')
  """
  try:
    conexion.cursor.execute(sql)
    conexion.cerrar()
  except:
    titulo = 'Conexion al registro'
    mensaje = 'La tabla pelicula no existe en la base de datos'
    messagebox.showerror(title=titulo, message=mensaje)
    
def listar():
  conexion = ConexionDB()

  lista_peliculas = []
  sql = 'SELECT * FROM pelicula'

  try:
    conexion.cursor.execute(sql)
    lista_peliculas = conexion.cursor.fetchall()
    conexion.cerrar()
  except:
    titulo = 'Conexion al registro'
    mensaje = 'Crear la tabla en la base de datos'
    messagebox.showwarning(title=titulo, message=mensaje)
    
  return lista_peliculas


def editar(pelicula, id_pelicula):
  conexion = ConexionDB()

  sql = f"""UPDATE pelicula
  SET nombre = '{pelicula.nombre}', duracion = '{pelicula.duracion}', genero = '{pelicula.genero}'
  WHERE id_pelicula = {id_pelicula}
  """
  try:
    conexion.cursor.execute(sql)
    conexion.cerrar()
  except:
    titulo = 'Edición de Datos'
    mensaje = 'No se pudo editar este registro'
    messagebox.showerror(title=titulo, message=mensaje)

def eliminar(id_pelicula):
  conexion = ConexionDB()

  sql = f"""
  DELETE FROM pelicula WHERE id_pelicula = {id_pelicula}
  """

  try:
    conexion.cursor.execute(sql)
    conexion.cerrar()
  except:
    titulo = 'Eliminar Datos'
    mensaje = 'No se pudo eliminar el registro'
    messagebox.showerror(title=titulo, message=mensaje)