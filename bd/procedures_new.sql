-- --------------- nuevas actualizaciones

-- ELIMINAMOS EL PROCEDIMIENTO ANTERIOR SI EXISTE
DROP PROCEDURE IF EXISTS `sp_buscar_escuela_por_nombre`;

DELIMITER $$
CREATE PROCEDURE `sp_buscar_escuela_por_nombre`(
    IN p_nombre VARCHAR(100)
)
BEGIN
    -- Usamos LIKE y CONCAT para buscar coincidencias parciales.
    -- Ej: si p_nombre es 'sist', encontrará 'Ingeniería de Sistemas'.
    SELECT * 
    FROM escuela 
    WHERE nombre LIKE CONCAT('%', p_nombre, '%');
END$$
DELIMITER ;

USE `sistema_academico`;
DROP PROCEDURE IF EXISTS `sp_listar_matriculas`;

DELIMITER $$
CREATE PROCEDURE `sp_listar_matriculas`()
BEGIN
    SELECT 
        m.id_matricula,
        m.ciclo,
        m.id_estudiante,
        m.id_curso,
        CONCAT(e.nombres, ' ', e.apellidos) AS nombre_estudiante,
        c.nombre AS nombre_curso
    FROM matricula m
    JOIN estudiante e ON m.id_estudiante = e.id_estudiante
    JOIN curso c ON m.id_curso = c.id_curso
    ORDER BY m.id_matricula DESC;
END$$
DELIMITER ;

USE `sistema_academico`;

-- DASHBOARD
-- 1. PROCEDIMIENTO PARA OBTENER LOS CONTEOS TOTALES
DROP PROCEDURE IF EXISTS `sp_dashboard_counts`;
DELIMITER $$
CREATE PROCEDURE `sp_dashboard_counts`()
BEGIN
    SELECT
        (SELECT COUNT(*) FROM estudiante) AS total_estudiantes,
        (SELECT COUNT(*) FROM escuela) AS total_escuelas,
        (SELECT COUNT(*) FROM curso) AS total_cursos,
        (SELECT COUNT(*) FROM matricula) AS total_matriculas;
END$$
DELIMITER ;


-- 2. PROCEDIMIENTO PARA OBTENER EL NÚMERO DE ESTUDIANTES POR ESCUELA
DROP PROCEDURE IF EXISTS `sp_dashboard_estudiantes_por_escuela`;
DELIMITER $$
CREATE PROCEDURE `sp_dashboard_estudiantes_por_escuela`()
BEGIN
    SELECT 
        e.nombre AS escuela_nombre,
        COUNT(est.id_estudiante) AS numero_estudiantes
    FROM escuela e
    LEFT JOIN estudiante est ON e.id_escuela = est.id_escuela
    GROUP BY e.id_escuela
    ORDER BY numero_estudiantes DESC;
END$$
DELIMITER ;


-- 3. PROCEDIMIENTO PARA OBTENER LAS ÚLTIMAS MATRÍCULAS
DROP PROCEDURE IF EXISTS `sp_dashboard_ultimas_matriculas`;
DELIMITER $$
CREATE PROCEDURE `sp_dashboard_ultimas_matriculas`()
BEGIN
    SELECT 
        CONCAT(e.nombres, ' ', e.apellidos) AS nombre_estudiante,
        c.nombre AS nombre_curso,
        m.ciclo
    FROM matricula m
    JOIN estudiante e ON m.id_estudiante = e.id_estudiante
    JOIN curso c ON m.id_curso = c.id_curso
    ORDER BY m.id_matricula DESC
    LIMIT 5; -- Traemos solo las últimas 5 para mantener la lista corta
END$$
DELIMITER ;