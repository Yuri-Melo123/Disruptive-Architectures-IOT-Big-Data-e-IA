CREATE OR REPLACE VIEW avg_temp_por_dispositivo AS
SELECT room_id, AVG(temperature) as avg_temp
FROM temperature_readings
GROUP BY room_id;

CREATE OR REPLACE VIEW leituras_por_hora AS
SELECT EXTRACT(HOUR FROM noted_date) as hora, COUNT(*) as contagem
FROM temperature_readings
GROUP BY hora
ORDER BY hora;

CREATE OR REPLACE VIEW temp_max_min_por_dia AS
SELECT DATE(noted_date) as dia,
       MAX(temperature) as temp_max,
       MIN(temperature) as temp_min
FROM temperature_readings
GROUP BY dia
ORDER BY dia;