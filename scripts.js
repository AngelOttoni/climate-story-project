// scripts.js

const ctx = document.getElementById('emissionsChart').getContext('2d');

// Dados fictícios para o gráfico de emissões
const emissionsData = {
    labels: ['1990', '1995', '2000', '2005', '2010', '2015', '2020'],
    datasets: [{
        label: 'Emissões de Gases de Efeito Estufa (MtCO2e)',
        data: [5000, 5200, 5400, 5800, 6000, 6200, 6500],
        backgroundColor: 'rgba(75, 192, 192, 0.2)',
        borderColor: 'rgba(75, 192, 192, 1)',
        borderWidth: 1
    }]
};

// Criação do gráfico
const emissionsChart = new Chart(ctx, {
    type: 'line',  // O tipo de gráfico que vamos usar
    data: emissionsData,
    options: {
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
});
