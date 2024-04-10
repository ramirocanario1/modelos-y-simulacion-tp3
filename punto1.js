// Calculo los valores aleatorios

let valoresAleatorios = [];
const cantidad = 100;
const ocurrencias = {};

for (let i = 0; i < cantidad; i++) {
  const valor = Math.floor(Math.random() * 100) + 1; // Generate numbers from 1 to 100
  valoresAleatorios.push(valor);

  if (ocurrencias[valor]) {
    ocurrencias[valor]++;
  } else {
    ocurrencias[valor] = 1;
  }
}

for (let i = 1; i <= 100; i++) {
  if (!ocurrencias[i]) {
    ocurrencias[i] = 0;
  }
}

const media = valoresAleatorios.reduce((acc, val) => acc + val, 0) / cantidad;
const desvioEstandar = Math.sqrt(
  valoresAleatorios.reduce((acc, val) => acc + Math.pow(val - media, 2), 0) /
    cantidad
);
const varianza = Math.pow(desvioEstandar, 2);

// Muestro las métricas obtenidas

document.getElementById("promedio").innerText = media.toFixed(2);
document.getElementById("desvio").innerText = desvioEstandar.toFixed(2);
document.getElementById("varianza").innerText = varianza.toFixed(2);

// Genero el histograma

const ctx = document.getElementById("grafico");

const chart = new Chart(ctx, {
  type: "bar",
  data: {
    labels: Array.from({ length: 100 }, (_, i) => i + 1),
    datasets: [
      {
        label: "Ocurrencias",
        data: Array.from({ length: 100 }, (_, i) => ocurrencias[i + 1]),
        backgroundColor: Array.from(
          { length: 100 },
          () => "rgba(54, 162, 235, 0.2)"
        ),
        borderColor: Array.from({ length: 100 }, () => "rgba(54, 162, 235, 1)"),
        borderWidth: 1,
      },
    ],
  },
  options: {
    scales: {
      y: {
        beginAtZero: true,
        precision: 0, // Set precision to 0 to display integers on the y-axis
        stepSize: 1, // Set the step size to 1 for one unit increments on the y-axis
      },
    },
  },
});
