const botonesFiltro = document.querySelectorAll('.filtro');
    const tarjetas = document.querySelectorAll('.mascota');

    botonesFiltro.forEach(boton => {
      boton.addEventListener('click', () => {
        const tipo = boton.dataset.tipo;

        tarjetas.forEach(tarjeta => {
          const mostrar = tipo === 'todos' || tarjeta.classList.contains(tipo);
          tarjeta.style.display = mostrar ? 'block' : 'none';
        });
      });
    });