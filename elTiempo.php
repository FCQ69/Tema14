<?php
// URL de la API
$url = 'https://api.open-meteo.com/v1/forecast?latitude=40.2842&longitude=-3.7942&hourly=temperature_2m';

$response = file_get_contents($url);
$data = json_decode($response, true);

$temperaturas = $data['hourly']['temperature_2m'];
$fechas = $data['hourly']['time'];


$fechas_unicas = array_unique(array_map(function($fecha) {
    return substr($fecha, 0, 10); 
}, $fechas));

$fechas_deseadas = array_slice($fechas_unicas, 0, 3); 


foreach ($fechas_deseadas as $fecha) {
    $temp = $temperaturas[array_search($fecha, $fechas)];
    echo "Fecha: $fecha - Temperatura: $temp °C\n <br>";
}
?>
