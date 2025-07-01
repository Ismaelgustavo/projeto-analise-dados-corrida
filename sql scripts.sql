# Maiores distâncias
SELECT id AS Corrida,distancia AS KM_Corrido
FROM corridas
ORDER BY distancia DESC LIMIT 5;

# Média das Distância
SELECT AVG(distancia)
FROM corridas;

# Maiores velocidades médias alcançadas
SELECT id AS Corrida,  velocidade_media AS Velocidade
FROM corridas
ORDER BY velocidade_media DESC LIMIT 5;

# Dias da semanda com mais corridas
SELECT dia_semana,COUNT(dia_semana) AS qtd_dias
FROM corridas
GROUP BY dia_semana
ORDER BY qtd_dias DESC;

# Média de calorias 
SELECT AVG(calorias) AS Média_Calorias
FROM corridas;

# dias de descanso de cada corrida
SELECT *
FROM (
  SELECT 
    data_corrida,
    distancia,
    DATEDIFF(data_corrida, LAG(data_corrida) OVER (ORDER BY data_corrida)) AS dias_descanso
  FROM corridas
) AS sub
WHERE dias_descanso <= 10;

# Média de dia descanso por distância (Km) corrido
SELECT 
  ROUND(distancia) AS km_arredondado,
  AVG(dias_descanso) AS media_descanso
FROM (
  SELECT 
    distancia,
    DATEDIFF(data_corrida, LAG(data_corrida) OVER (ORDER BY data_corrida)) AS dias_descanso
  FROM corridas
) AS sub
GROUP BY km_arredondado
ORDER BY km_arredondado;






