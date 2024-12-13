PROYECTO DE GESTION UNIVERSITARIA

I. Introducción.

Descripción.

Este proyecto consiste en una aplicación de consola desarrollada en el lenguaje de programación Python, conectada a una base de datos MySQL. El programa permite gestionar de manera eficiente las operaciones administrativas y académicas de una universidad, incluyendo el registro de facultades, programas, profesores, estudiantes y cursos, así como las matrículas de los estudiantes en programas y cursos académicos.
Objetivo General.
Desarrollar un sistema de gestión universitaria que facilite las operaciones administrativas y académicas, optimizando los procesos relacionados con facultades, programas, profesores, estudiantes, cursos y matrículas.
Objetivos Específicos.
- Implementar funcionalidades CRUD para cada entidad del sistema.
- Establecer una conexión segura y eficiente con la base de datos MySQL.
- Diseñar un sistema escalable y mantenible que permita futuras ampliaciones.
- Garantizar una interfaz de usuario amigable y eficiente para la interacción en consola.
Alcance.
Este proyecto está diseñado para su uso en entornos de consola, proporcionando una solución robusta para la gestión universitaria. No incluye interfaces gráficas ni funciones web en su versión inicial, pero se prevé su escalabilidad hacia dichas plataformas.

II. Requisitos del Sistema.

Requisitos Funcionales del Sistema.

- Gestión de Facultades: CRUD que facilite operaciones de creación, lectura, actualización y eliminación de registros de las facultades. 
- Gestión de Programas Universitarios: CRUD que facilite operaciones de creación, lectura, actualización y eliminación de registros de los programas.
- Gestión de Estudiantes: CRUD que facilite operaciones de creación, lectura, actualización y eliminación de registros de los estudiantes.
- Gestión de Profesores: CRUD que facilite operaciones de creación, lectura, actualización y eliminación de registros de los profesores.
- Gestión de Cursos: CRUD que facilite operaciones de creación, lectura, actualización y eliminación de registros de los cursos.
- Gestión de Matriculas a Programas: CRUD que facilite operaciones de creación, lectura, actualización y eliminación de registros de las matriculas en programas.
- Gestión de Matriculas a Cursos: CRUD que facilite operaciones de creación, lectura, actualización y eliminación de registros de las matriculas en cursos.
- Menú Principal: Un menú interactivo para gestionar las diferentes entidades.

Requisitos No Funcionales del Sistema.

- Rendimiento: Procesamiento eficiente de solicitudes para minimizar los tiempos de ejecución.
- Mantenibilidad: Código estructurado y documentado para facilitar el mantenimiento.
- Escalabilidad: Diseño orientado a soportar ampliaciones futuras, como la migración a una plataforma web.

III. Arquitectura.

Patrón Arquitectónico.

Para garantizar una estructura escalable y fácil de mantener, el desarrollo se basará en la arquitectura MVC (Modelo, Vista, Controlador), lo que asegura una clara separación de responsabilidades y facilita futuras ampliaciones o modificaciones.

Tecnologías utilizadas.

- Lenguaje de programación: Se utiliza el lenguaje Python para la construcción de la lógica de la aplicación.
- Bases de datos: MySQL, para garantizar almacenamiento seguro y relaciones adecuadas entre entidades.

IV. Diseño

El proyecto está organizado en módulos según el patrón MVC, facilitando el desarrollo, mantenimiento y escalabilidad del sistema.

Descripción de Componentes

- Controller: Gestiona la lógica de negocio y conecta la vista con el modelo.
- Model: Representa las entidades del sistema y gestiona la interacción con la base de datos.
- View: Proporciona una interfaz para la interacción del usuario.

Estructura del código.

A continuación, se detalla la organización de los archivos y módulos del proyecto:
/ProyectoUniversidad
├── /controller
│   ├── curso.py
│   ├── estudiante.py
│   ├── facultad.py
│   ├── matriculaCurso.py
│   ├── matriculaPrograma.py
│   ├── profesor.py
│   └── programa.py
├── /model
│   ├── curso.py
│   ├── estudiante.py
│   ├── facultad.py
│   ├── matriculaCurso.py
│   ├── matriculaPrograma.py
│   ├── profesor.py
│   └── programa.py
├── /view
│   ├── curso.py
│   ├── estudiante.py
│   ├── facultad.py
│   ├── matriculaCurso.py
│   ├── matriculaPrograma.py
│   ├── principal.py
│   ├── profesor.py
│   └── programa.py
├── main.py
└── database.py

V. Instrucciones de Uso.

- Ejecuta el archivo main.py para iniciar la aplicación.
- En el menú principal, selecciona una de las opciones disponibles:
    1. Gestión de Facultades.
    2. Gestión de Programas.
    3. Gestión de Estudiantes.
    4. Gestión de Profesores.
    5. Gestión de Cursos.
    6. Gestión de Matrículas de Programas.
    7. Gestión de Matrículas de Cursos.
    8. Salir del programa.
- Sigue las instrucciones en pantalla para realizar las operaciones deseadas.
- Los datos ingresados serán procesados y almacenados en la base de datos.
