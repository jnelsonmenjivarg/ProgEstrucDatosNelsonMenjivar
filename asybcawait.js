console.log("Inicio del proceso");

function tarea(mensaje, tiempo) {
  return new Promise(resolve => {
    setTimeout(() => {
      console.log(mensaje);
      resolve();
    }, tiempo);
  });
}

async function ejecutarProceso() {
  await tarea("Cargando datos...", 6000);
  await tarea("Procesando información cargada...", 8000);
  await tarea("Proceso completado de carga de datos y procesaiento", 8000);
}

ejecutarProceso();

console.log("El programa sigue respondiendo...");



