# Cálculo de Perdas por Correntes de Foucault na Tampa de um Transformador

Este script em Python calcula as perdas por correntes parasitas (de Foucault) induzidas na tampa de um transformador, causadas pelo campo magnético gerado por barras condutoras. O cálculo é feito por meio de integração dupla em regiões da tampa, evitando os centros dos condutores.

## 📌 Objetivo

Determinar as perdas totais de energia, em watts, nas regiões da tampa do transformador expostas ao campo magnético gerado por diferentes correntes nos condutores.

## ⚙️ Como Funciona

1. **Modelo Matemático:**  
   Utiliza uma integral dupla sobre regiões específicas da tampa para calcular a densidade de corrente induzida e, com isso, as perdas por efeito Joule.

2. **Constantes e Parâmetros:**  
   - `a`: distância entre barras condutoras (m)
   - `w`: frequência angular da corrente (rad/s)
   - `mu`: permeabilidade magnética do meio (H/m)
   - `sigma`: condutividade elétrica do material da tampa (S/m)

3. **Integração:**  
   A integração é feita com `scipy.integrate.dblquad` sobre subáreas da tampa.

4. **Saída:**  
   Para cada corrente aplicada (2000 A, 2250 A, 2500 A, 2800 A), o código imprime as perdas calculadas e compara com valores de referência.

## 🔧 Dependências

Antes de rodar, instale as bibliotecas necessárias:

```bash
pip install numpy scipy
```

## ▶️ Como Executar

1. Salve o script em um arquivo, por exemplo `perdas_tampa.py`.
2. Execute com Python 3:

```bash
python perdas_tampa.py
```

## 📤 Saída Esperada

```plaintext
Perdas totais para corrente 2000A = 63.7W e erro de 0.0899999999999963W
Perdas totais para corrente 2250A = 80.69W e erro de 0.05000000000000426W
Perdas totais para corrente 2500A = 99.61W e erro de 0.060000000000002274W
Perdas totais para corrente 2800A = 124.91W e erro de 0.0899999999999892W
```

## 📚 Aplicações

Este script pode ser utilizado para:
- Projetar tampas de transformadores com menor perda térmica.
- Estimar a eficiência energética de transformadores em operação.
- Estudos acadêmicos sobre perdas magnéticas em estruturas metálicas.
