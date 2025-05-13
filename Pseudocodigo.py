import graphviz

def crear_diagrama_gota():
    dot = graphviz.Digraph()

    # Inicio
    dot.node("A", "Inicio", shape="oval'")

    # Entrada de parámetros iniciales
    dot.node('B', 'Leer r0, h0, dr/dt, dh/dt, tiempo_max, pasos', shape='parallelogram')

    # Cálculo de tiempo y variables
    dot.node("C", 'Calcular t = linspace(0, tiempo_max, pasos)', shape='rectangle')
    dot.node("D", 'Calcular r(t), h(t)', shape='rectangle')
    dot.node('E', 'Calcular d = 2 * r, V = πr²h', shape='rectangle')
    dot.node('F', 'Calcular dV/dt = π(2rh dr/dt + r² dh/dt)', shape='rectangle')
    dot.node('G', 'Crear DataFrame con resultados', shape='rectangle')

    # Mostrar resultados y graficar
    dot.node('H', 'Mostrar resultados iniciales y finales', shape='rectangle')
    dot.node('I', 'Graficar curvas de d, V, dV/dt', shape='rectangle')

    # Decisión para exportar
    dot.node('J', '¿Exportar CSV?', shape='diamond')
    dot.node('K', 'Exportar CSV', shape='rectangle')
    dot.node('L', 'Fin', shape='oval')

    # Flujo gráfico
    dot.edge('A', 'B')
    dot.edge('B', 'C')
    dot.edge('C', 'D')
    dot.edge('D', 'E')
    dot.edge('E', 'F')
    dot.edge('F', 'G')
    dot.edge('G', 'H')
    dot.edge('H', 'I')
    dot.edge('I', 'J')
    dot.edge('J', 'K', label='Sí')
    dot.edge('J', 'L', label='No')
    dot.edge('K', 'L')

    return dot

crear_diagrama_gota()
diagrama = crear_diagrama_gota()
diagrama.render("diagrama_gota", format='png', view=True)
