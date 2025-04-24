import numpy as np
from scipy.integrate import dblquad

def perdas_na_tampa(Im, a, w, mu, sigma, x1, x2, y1, y2):
    constante = 0.5 * np.sqrt((w * mu) / (2 * sigma))

    integrando = lambda y, x: abs(((Im * a) / (2 * np.pi)) * np.sqrt(3*(x**2) + 3*(y**2) + (a**2) / 
        (((x**2) + (y**2)) * ((x**4) + (y**4) + 2*(x**2)*(y**2) - 2*(a**2)*(x**2) + 2*(a**2)*(y**2) + (a**4)))))**2

    # Integração dupla sobre a área definida
    resultado, erro = dblquad(
        integrando,
        x1, x2,          
        y1, y2         
    )
    
    return constante * resultado


# Parâmetros fixos
a = 0.114  
w = 2 * np.pi * 60  
mu =500*4*np.pi*1e-7   
sigma = 2e7

# Subdivisões da área, evitando os centros dos condutores
subareas = [
        (-0.295,-0.12, -0.135, 0.135),
        (-0.11,-0.01 , -0.135, 0.135),
        (0.01,0.11 , -0.135, 0.135),
        (0.12,0.295, -0.135, 0.135)
]

correntes = [
    (2000,63.79), (2250,80.74), (2500,99.67), (2800,125)
]


for corrente, erro in correntes:
    perdas_totais = 0
    for x1,x2,y1,y2 in subareas:
        perdas_totais += perdas_na_tampa(corrente, a, w, mu, sigma, x1, x2, y1, y2)
    print(f"Perdas totais para corrente {corrente}A = {perdas_totais}W e erro de {erro-perdas_totais}W")
