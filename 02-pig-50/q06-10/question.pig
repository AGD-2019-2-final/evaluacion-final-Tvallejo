-- 
-- Pregunta
-- ===========================================================================
-- 
-- Para el archivo `data.tsv` Calcule la cantidad de registros por clave de la 
-- columna 3. En otras palabras, cuántos registros hay que tengan la clave 
-- `aaa`?
-- 
-- Escriba el resultado a la carpeta `output` del directorio actual.
-- 
fs -rm -f -r output;
--
-- >>> Escriba su respuesta a partir de este punto <<<

data = LOAD 'data.tsv' USING PigStorage()
    AS (
        f1:CHARARRAY, 
        f2:BAG{t: TUPLE(p:CHARARRAY)}, 
        f3:MAP[]
    );
Y = FOREACH data GENERATE FLATTEN(KEYSET(f3)) AS key;
grouped = GROUP Y BY key;
counted = FOREACH grouped GENERATE group AS key, COUNT(Y) AS count;
STORE counted INTO 'output' USING PigStorage(',');
