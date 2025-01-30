import streamlit as st
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

# Título de la app con estilo
st.markdown("""
    <h1 style="text-align: center; color: #4CAF50; font-family: 'Arial', sans-serif;">Interfaz para Graficar y Verificar la Convexidad de Funciones</h1>
    """, unsafe_allow_html=True)

# Subtítulo
st.markdown("<h2 style='text-align: center; font-family: 'Arial', sans-serif;'>Ingrese una función matemática en términos de x</h2>", unsafe_allow_html=True)

# Fondo personalizado
st.markdown("""
    <style>
        .reportview-container {
            background-color: #f0f0f5;
        }
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            font-size: 16px;
        }
    </style>
""", unsafe_allow_html=True)

# Disposición en columnas
col1, col2 = st.columns([3, 1])

with col1:
    # Caja de texto para la función
    func_input = st.text_input('Ingresa una función (ejemplo: x**2, x**3, sin(x), cos(x)):', 'x**2')

with col2:
    # Imagen personalizada (usando la ruta local que proporcionaste)
    st.image("C:/Users/VICTUS/Documents/U-FINESI/NivelacionOptimizacion/ProgramacionNoLineal/images.jpg", width=100)

# Convierte la entrada a una función simbólica
x = sp.symbols('x')
try:
    # Convertir la entrada en una expresión simbólica
    func = sp.sympify(func_input)
    
    # Derivadas de la función
    f_prime = sp.diff(func, x)
    f_double_prime = sp.diff(f_prime, x)

    # Evaluar la segunda derivada en x = 0
    second_derivative_at_0 = f_double_prime.subs(x, 0)
    
    # Mostrar la información de la función y sus derivadas
    st.write(f'**Función ingresada**: {func}')
    st.write(f'**Primera derivada**: {f_prime}')
    st.write(f'**Segunda derivada**: {f_double_prime}')
    st.write(f'**Segunda derivada evaluada en x = 0**: {second_derivative_at_0}')

    # Verificar la convexidad
    if second_derivative_at_0 > 0:
        st.write('**La función es convexa en x = 0.**', unsafe_allow_html=True)
    else:
        st.write('**La función no es convexa en x = 0.**', unsafe_allow_html=True)

    # Graficar la función
    f_lambdified = sp.lambdify(x, func, "numpy")
    x_vals = np.linspace(-10, 10, 400)
    y_vals = f_lambdified(x_vals)

    # Mostrar la gráfica
    plt.figure(figsize=(8, 6))
    plt.plot(x_vals, y_vals, label=f'Gráfico de {func_input}', color='dodgerblue', linewidth=2)
    plt.title('Gráfico de la Función', fontsize=16, fontweight='bold', color='#4CAF50')
    plt.xlabel('x', fontsize=14)
    plt.ylabel('f(x)', fontsize=14)
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    plt.legend()
    st.pyplot(plt)

except Exception as e:
    st.write(f"Error al procesar la función: {e}")
