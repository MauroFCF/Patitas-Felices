document.addEventListener("DOMContentLoaded", () => {
  // Validación del formulario
  const form = document.getElementById("formAdopcion");
  if (form) {
    form.addEventListener("submit", (e) => {
      e.preventDefault();
      const nombre = document.getElementById("nombre").value.trim();
      const email = document.getElementById("email").value.trim();
      const mascota = document.getElementById("mascota").value;
      const motivo = document.getElementById("motivo").value.trim();

      if (!nombre || !email || !mascota || motivo.length < 10) {
        alert("Por favor, completa todos los campos correctamente.");
      } else {
        alert(`Gracias ${nombre}, tu solicitud para adoptar a ${mascota} fue registrada.`);
        form.reset();
      }
    });
  }

  // Calculadora
  const calcularBtn = document.getElementById("calcular");
  if (calcularBtn) {
    calcularBtn.addEventListener("click", () => {
      const tipo = document.getElementById("tipo").value;
      const edad = parseInt(document.getElementById("edad").value);
      const tamano = document.getElementById("tamano").value;

      let costo = tipo === "perro" ? 30 : 20;
      if (tamano === "mediano") costo += 10;
      if (tamano === "grande") costo += 20;
      if (edad > 5) costo += 15;

      const res = document.getElementById("resultado");
      res.style.display = "block";
      res.className = "alert alert-success";
      res.textContent = `El costo mensual estimado es de $${costo}.`;
    });
  }
});
