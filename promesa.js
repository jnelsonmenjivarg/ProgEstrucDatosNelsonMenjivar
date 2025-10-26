console.log("Inicio del proceso");

function tarea(mensaje, tiempo) {
  return new Promise(resolve => {
    setTimeout(() => {
      console.log(mensaje);
      resolve();
    }, tiempo);
  });
}

tarea("Cargando datos...", 3000)
  .then(() => tarea("Procesando información...", 4000))
  .then(() => tarea("Proceso completado", 5000));

console.log("El programa sigue respondiendo...");