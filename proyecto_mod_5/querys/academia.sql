# Creacion de la base de datos para proyecto de Academia de Programacion
CREATE DATABASE IF NOT EXISTS academia; # Esto es para evitar errores si la base de datos ya existe

USE academia; # Seleccionamos la base de datos para trabajar en ella

-- Tabla de Estudiantes
CREATE TABLE Estudiantes (
    id_estudiante INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100) NOT NULL,
    correo_electronico VARCHAR(100) NOT NULL UNIQUE,
    telefono VARCHAR(15)
);
-- Tabla profesores
CREATE TABLE Profesores (
    id_profesor INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100) NOT NULL,
    correo_electronico VARCHAR(100) NOT NULL UNIQUE,
    telefono VARCHAR(15),
    especialidad VARCHAR(100) NOT NULL
);
-- Tabla Cursos
CREATE TABLE Cursos (
    id_curso INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    descripcion TEXT,
    duracion_horas INT,
    id_profesor INT,
    FOREIGN KEY (id_profesor) REFERENCES Profesores(id_profesor)
        ON DELETE SET NULL ON UPDATE CASCADE
);

-- Tabla Matriculas  (N:N) se relaciona con Estudiantes y Cursos
CREATE TABLE Matriculas (
    id_matricula INT AUTO_INCREMENT PRIMARY KEY,
    estudiante_id INT,
    curso_id INT,
    fecha_matricula DATE,
    FOREIGN KEY (estudiante_id) REFERENCES Estudiantes(id_estudiante)
        ON DELETE CASCADE ON UPDATE CASCADE,
    -- Relaciona con Cursos
    FOREIGN KEY (curso_id) REFERENCES Cursos(id_curso)
        ON DELETE CASCADE ON UPDATE CASCADE
);

-- Tabla Horarios relacion (1:N) con Cursos y Horarios
CREATE TABLE Horarios (
    id_horario INT AUTO_INCREMENT PRIMARY KEY,
    curso_id INT,
    dia_semana VARCHAR(20),
    hora_inicio TIME,
    hora_fin TIME,
    FOREIGN KEY (curso_id) REFERENCES Cursos(id_curso)
        ON DELETE CASCADE ON UPDATE CASCADE
);
-- Inserts para Estudiantes
INSERT INTO Estudiantes (
    nombre, apellido, correo_electronico, telefono)
VALUES (
    'Juan', 'Pérez', 'juan.perez@email.com', '555123456'),
    ('Ana', 'García', 'ana.garcia@email.com', '555654321');

-- Inserts para Profesores
INSERT INTO Profesores (
    nombre, apellido, correo_electronico, telefono, especialidad)
VALUES (
    'Carlos', 'López', 'carlos.lopez@email.com', '555111222', 'Python'),
    ('María', 'Martínez', 'maria.martinez@email.com', '555333444', 'JavaScript');

-- Inserts para Cursos
INSERT IGNORE INTO Cursos (
    nombre, descripcion, duracion_horas, id_profesor)
VALUES (
        'Introducción a Python', 'Curso básico de programación en Python', 40, 1),
       ('JavaScript Avanzado', 'Curso avanzado de JavaScript', 60, 2);


-- Inserts para Matriculas
INSERT INTO Matriculas (
    estudiante_id, curso_id, fecha_matricula)
VALUES (
    1, 1, '2024-06-15'),
    (2, 2, '2024-06-16');

-- Inserts para Horarios
INSERT INTO Horarios (
    curso_id, dia_semana, hora_inicio, hora_fin)
VALUES (
    1, 'Lunes', '09:00:00', '11:00:00'),
    (2, 'Miércoles', '14:00:00', '16:00:00');

--Arreglo del error en el insert de cursos:
ALTER TABLE Cursos ADD UNIQUE (nombre);
-- 