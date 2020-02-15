-- 
-- Pregunta
-- ===========================================================================
-- 
-- Para el archivo `data.tsv` compute la cantidad de registros por letra. 
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
x = GROUP data BY letter;
y = FOREACH x GENERATE group AS letter, COUNT(data) AS count;
STORE y INTO 'output';
