// Função para criar o gráfico de barras com dados de resultados
function createResultsChart(results) {
    const labels = Object.keys(results);
    const data = Object.values(results);

    const ctx = document.getElementById('resultsChart').getContext('2d');
    new Chart(ctx, {
        type: 'bar',
        data: {
            labels: labels,
            datasets: [{
                label: 'Probability (%)',
                data: data,
                backgroundColor: 'rgba(54, 162, 235, 0.6)',
                borderColor: 'rgba(54, 162, 235, 1)',
                borderWidth: 1
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            scales: {
                y: {
                    beginAtZero: true,
                    max: 100  // Limita o eixo Y a 100%
                }
            },
            layout: {
                padding: 10
            },
            plugins: {
                legend: {
                    display: false
                }
            }
        }
    });
}
