console.log("Inicio del proceso a valdiad");

setTimeout(() => {
  console.log("Cargando datos...");

  setTimeout(() => {
    console.log("Procesando información...");

    setTimeout(() => {
      console.log("Proceso completado");
    }, 5000);

  }, 5000);

}, 5000);

console.log("El programa sigue respondiendo...");
