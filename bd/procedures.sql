USE `sistema_academico`;
-- Procedimientos para Escuela
DROP procedure IF EXISTS `sistema_academico`.`sp_listar_escuela`;

DELIMITER $$
USE `sistema_academico`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_listar_escuela`()
BEGIN
    select * from escuela; 
END$$
DELIMITER ;

USE `sistema_academico`;
DROP PROCEDURE IF EXISTS `sp_escuela`;
DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_escuela`(
    IN accion VARCHAR(10),
    IN pid INT,
    IN pnombre VARCHAR(100)
)
BEGIN
    DECLARE estado VARCHAR(10);
    DECLARE mensaje VARCHAR(255);
    DECLARE codigo INT;

    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        ROLLBACK;
        SET estado = 'ERROR';
        SET mensaje = 'Ocurrió un error durante la operación';
        SET codigo = -1;
        SELECT estado, mensaje, codigo;
    END;

    START TRANSACTION;

    IF accion = 'I' THEN 
        INSERT INTO escuela(nombre) VALUES (pnombre);
        SET estado = 'CORRECTO';
        SET mensaje = 'OPERACION REALIZADA';
        SET codigo = LAST_INSERT_ID();

    ELSEIF accion = 'U' THEN
        UPDATE escuela SET nombre = pnombre WHERE id_escuela = pid;
        SET estado = 'CORRECTO';
        SET mensaje = 'OPERACION REALIZADA';
        SET codigo = pid;

    ELSEIF accion = 'D' THEN
        DELETE FROM escuela WHERE id_escuela = pid;
        SET estado = 'CORRECTO';
        SET mensaje = 'OPERACION REALIZADA';
        SET codigo = pid;

    ELSE
        SET estado = 'ERROR';
        SET mensaje = 'Acción no válida';
        SET codigo = 0;
        ROLLBACK;                
    END IF;
    COMMIT;
    SELECT estado, mensaje, codigo;    
END$$
DELIMITER ;

DROP PROCEDURE IF EXISTS sp_obtener_escuela;
DELIMITER $$

CREATE PROCEDURE sp_obtener_escuela(
    IN id_escuela INT
)
BEGIN
    SELECT * FROM escuela WHERE id_escuela = id_escuela;
END$$
DELIMITER ;

-- Procedimientos para Estudiante
DROP PROCEDURE IF EXISTS sp_obtener_estudiante;
DELIMITER $$

CREATE PROCEDURE sp_obtener_estudiante(
    IN id_estudiante INT
)
BEGIN
    SELECT * FROM estudiante WHERE id_estudiante = id_estudiante;
END$$
DELIMITER ;

DROP PROCEDURE IF EXISTS sp_listar_estudiante;
DELIMITER $$

CREATE PROCEDURE sp_listar_estudiante()
BEGIN
    SELECT * FROM estudiante;
END$$
DELIMITER ;

DROP PROCEDURE IF EXISTS sp_estudiante;
DELIMITER $$

CREATE PROCEDURE sp_estudiante(
    IN accion CHAR(1),
    IN id INT,
    IN nombres VARCHAR(100),
    IN apellidos VARCHAR(100),
    IN correo VARCHAR(100),
    IN id_escuela INT
)
BEGIN
    DECLARE estado VARCHAR(10);
    DECLARE mensaje VARCHAR(255);
    DECLARE codigo INT;

    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        ROLLBACK;
        SET estado = 'ERROR';
        SET mensaje = 'Ocurrió un error durante la operación';
        SET codigo = -1;
        SELECT estado, mensaje, codigo;
    END;

    START TRANSACTION;

    IF accion = 'I' THEN
        INSERT INTO estudiante(nombres, apellidos, correo, id_escuela)
        VALUES (nombres, apellidos, correo, id_escuela);
        SET estado = 'CORRECTO';
        SET mensaje = 'Operación realizada';
        SET codigo = LAST_INSERT_ID();

    ELSEIF accion = 'U' THEN
        UPDATE estudiante
        SET nombres = nombres, apellidos = apellidos, correo = correo, id_escuela = id_escuela
        WHERE id_estudiante = id;
        SET estado = 'CORRECTO';
        SET mensaje = 'Operación realizada';
        SET codigo = id;

    ELSEIF accion = 'D' THEN
        DELETE FROM estudiante WHERE id_estudiante = id;
        SET estado = 'CORRECTO';
        SET mensaje = 'Operación realizada';
        SET codigo = id;

    ELSE
        SET estado = 'ERROR';
        SET mensaje = 'Acción no válida';
        SET codigo = 0;
        ROLLBACK;
    END IF;

    COMMIT;
    SELECT estado, mensaje, codigo;

END$$
DELIMITER ;

-- Procedimiento para Curso
DROP PROCEDURE IF EXISTS sp_listar_cursos;
DELIMITER $$

CREATE PROCEDURE sp_listar_cursos()
BEGIN
    SELECT * FROM curso;
END$$
DELIMITER ;

DROP PROCEDURE IF EXISTS sp_curso;
DELIMITER $$

CREATE PROCEDURE sp_curso(
    IN accion CHAR(1),
    IN id INT,
    IN nombre VARCHAR(100),
    IN creditos INT
)
BEGIN
    DECLARE estado VARCHAR(10);
    DECLARE mensaje VARCHAR(255);
    DECLARE codigo INT;

    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        ROLLBACK;
        SET estado = 'ERROR';
        SET mensaje = 'Ocurrió un error durante la operación';
        SET codigo = -1;
        SELECT estado, mensaje, codigo;
    END;

    START TRANSACTION;

    IF accion = 'I' THEN
        INSERT INTO curso(nombre, creditos)
        VALUES (nombre, creditos);
        SET estado = 'CORRECTO';
        SET mensaje = 'Operación realizada';
        SET codigo = LAST_INSERT_ID();

    ELSEIF accion = 'U' THEN
        UPDATE curso
        SET nombre = nombre, creditos = creditos
        WHERE id_curso = id;
        SET estado = 'CORRECTO';
        SET mensaje = 'Operación realizada';
        SET codigo = id;

    ELSEIF accion = 'D' THEN
        DELETE FROM curso WHERE id_curso = id;
        SET estado = 'CORRECTO';
        SET mensaje = 'Operación realizada';
        SET codigo = id;

    ELSE
        SET estado = 'ERROR';
        SET mensaje = 'Acción no válida';
        SET codigo = 0;
        ROLLBACK;
    END IF;

    COMMIT;
    SELECT estado, mensaje, codigo;

END$$
DELIMITER ;


-- Procedimiento para Matrícula
DROP PROCEDURE IF EXISTS sp_listar_matriculas;
DELIMITER $$

CREATE PROCEDURE sp_listar_matriculas()
BEGIN
    SELECT * FROM matricula;
END$$
DELIMITER ;

DROP PROCEDURE IF EXISTS sp_matricula;
DELIMITER $$

CREATE PROCEDURE sp_matricula(
    IN accion CHAR(1),
    IN id INT,
    IN id_estudiante INT,
    IN id_curso INT,
    IN ciclo VARCHAR(10)
)
BEGIN
    DECLARE estado VARCHAR(10);
    DECLARE mensaje VARCHAR(255);
    DECLARE codigo INT;

    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        ROLLBACK;
        SET estado = 'ERROR';
        SET mensaje = 'Ocurrió un error durante la operación';
        SET codigo = -1;
        SELECT estado, mensaje, codigo;
    END;

    START TRANSACTION;

    IF accion = 'I' THEN
        INSERT INTO matricula(id_estudiante, id_curso, ciclo)
        VALUES (id_estudiante, id_curso, ciclo);
        SET estado = 'CORRECTO';
        SET mensaje = 'Operación realizada';
        SET codigo = LAST_INSERT_ID();

    ELSEIF accion = 'U' THEN
        UPDATE matricula
        SET id_estudiante = id_estudiante, id_curso = id_curso, ciclo = ciclo
        WHERE id_matricula = id;
        SET estado = 'CORRECTO';
        SET mensaje = 'Operación realizada';
        SET codigo = id;

    ELSEIF accion = 'D' THEN
        DELETE FROM matricula WHERE id_matricula = id;
        SET estado = 'CORRECTO';
        SET mensaje = 'Operación realizada';
        SET codigo = id;

    ELSE
        SET estado = 'ERROR';
        SET mensaje = 'Acción no válida';
        SET codigo = 0;
        ROLLBACK;
    END IF;

    COMMIT;
    SELECT estado, mensaje, codigo;

END$$
DELIMITER ;
