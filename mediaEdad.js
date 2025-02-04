//modulo importado
const fs = require('fs');


function calcularMediaEdad() {
   
    fs.readFile('fallecimientos.json', 'utf8', (err, data) => {
        if (err) {
            console.error('Error al leer el archivo:', err);
            return;
        }

        // Parsear el JSON
        const fallecimientos = JSON.parse(data);

        let sumaEdades = 0;
        let cantidad = 0;

        fallecimientos.forEach((persona) => {
            
            let edad = parseInt(persona.edad, 10);
            if (!isNaN(edad)) {
                sumaEdades += edad;
                cantidad++;
            }
        });

        //Calculo media
          if (cantidad > 0) {
            const mediaEdad = sumaEdades / cantidad;
            console.log('La media de edad es:', mediaEdad.toFixed(2));
        } else {
            console.log('No se pudo calcular la media de edad, no se encontraron edades válidas.');
        }
    });
}

//Llamamos
calcularMediaEdad();
