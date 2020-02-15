-- Pregunta
-- ===========================================================================
-- 
-- Obtenga los cinco (5) valores más pequeños de la 3ra columna.
-- Escriba el resultado a la carpeta `output` del directorio actual.
-- 
fs -rm -f -r output;
--
-- >>> Escriba su respuesta a partir de este punto <<<

data = LOAD 'data.tsv' USING PigStorage()
    AS (
        letter:CHARARRAY,
        date:CHARARRAY,
        number:INT
    );
x = FOREACH data GENERATE number;
y = ORDER x BY number;
z = LIMIT y 5;
STORE z INTO 'output';
