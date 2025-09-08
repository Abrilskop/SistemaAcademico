// Espera a que todo el contenido de la página (el DOM) esté cargado antes de ejecutar cualquier script.
document.addEventListener('DOMContentLoaded', function () {

    // === LÓGICA PARA ALERTAS DE ELIMINACIÓN (SWEETALERT2) ===
    
    // 1. Encontrar todos los botones que tienen la clase 'delete-btn'.
    const deleteButtons = document.querySelectorAll('.delete-btn');
    
    // 2. Recorrer cada botón encontrado.
    deleteButtons.forEach(button => {
        // 3. Añadir un evento 'click' a cada botón.
        button.addEventListener('click', function (event) {
            // Previene que el formulario se envíe inmediatamente.
            event.preventDefault();

            // Obtener los datos personalizados del botón que fue presionado.
            const formId = this.dataset.formId;
            const form = document.getElementById(formId);
            const escuelaNombre = this.dataset.escuelaNombre;

            // Si el formulario correspondiente existe...
            if (form) {
                // ...mostrar la alerta de confirmación.
                Swal.fire({
                    title: '¿Estás seguro?',
                    text: `¡No podrás revertir la eliminación de "${escuelaNombre}"!`,
                    icon: 'warning',
                    showCancelButton: true,
                    confirmButtonColor: '#d33', // Rojo para el botón de eliminar
                    cancelButtonColor: '#3085d6', // Azul para el botón de cancelar
                    confirmButtonText: 'Sí, ¡eliminar!',
                    cancelButtonText: 'Cancelar'
                }).then((result) => {
                    // Si el usuario hace clic en "Sí, ¡eliminar!"...
                    if (result.isConfirmed) {
                        // ...enviar el formulario para realizar la eliminación.
                        form.submit();
                    }
                })
            }
        });
    });

    // === LÓGICA PARA EL MENÚ HAMBURGUESA (SIDEBAR MÓVIL) ===

    // 1. Seleccionar los elementos necesarios del DOM por su ID.
    const sidebar = document.getElementById('sidebar');
    const sidebarToggle = document.getElementById('sidebar-toggle');
    const overlay = document.getElementById('overlay');

    // 2. Función para mostrar u ocultar el menú.
    const toggleSidebar = () => {
        // Añade o quita la clase 'active' para que el CSS haga su magia.
        sidebar.classList.toggle('active');
        overlay.classList.toggle('active');
    };

    // 3. Asegurarse de que los elementos existen antes de añadirles eventos.
    if (sidebarToggle && sidebar && overlay) {
        // 4. Cuando se hace clic en el botón hamburguesa, llamar a la función toggleSidebar.
        sidebarToggle.addEventListener('click', toggleSidebar);
        
        // 5. Cuando se hace clic en el fondo oscuro (overlay), también cerrar el menú.
        overlay.addEventListener('click', toggleSidebar);
    }

    // === LÓGICA PARA EL GRÁFICO DEL DASHBOARD (CHART.JS) ===

    // 1. Intentar seleccionar el canvas del gráfico.
    const chartCanvas = document.getElementById('estudiantesPorEscuelaChart');

    // 2. Si el canvas existe (es decir, estamos en la página del dashboard)...
    if (chartCanvas) {
        // 3. Obtener los datos de los elementos span ocultos y convertirlos de texto a objeto JavaScript.
        const chartLabels = JSON.parse(document.getElementById('chart-data-labels').textContent);
        const chartDataValues = JSON.parse(document.getElementById('chart-data-values').textContent);
        
        // 4. Crear el gráfico.
        const ctx = chartCanvas.getContext('2d');
        const myBarChart = new Chart(ctx, {
            type: 'bar',
            data: {
                labels: chartLabels,
                datasets: [{
                    label: 'N° de Estudiantes',
                    data: chartDataValues,
                    backgroundColor: 'rgba(74, 128, 255, 0.8)',
                    borderColor: 'rgba(74, 128, 255, 1)',
                    borderWidth: 1
                }]
            },
            options: {
                maintainAspectRatio: false,
                responsive: true,
                scales: {
                    y: {
                        beginAtZero: true,
                        ticks: {
                            // Asegurarse de que solo se muestren números enteros en el eje Y
                            stepSize: 1 
                        }
                    }
                },
                plugins: {
                    legend: {
                        display: false
                    }
                }
            }
        });
    }
});