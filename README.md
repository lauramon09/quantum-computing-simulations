# Quantum Computing & Cryptography Lab 

Este repositorio reúne simulaciones prácticas de protocolos fundamentales en computación y criptografía cuántica, desarrolladas en Python para facilitar el estudio de la mecánica cuántica aplicada a la información.

## Proyectos Incluidos

### 1. Quantum Error Correction (QEC) - 3-Qubit Code
Simulador de detección y corrección de errores de inversión de bit (*bit-flip*).
* **Lógica:** Implementa la codificación de un estado lógico $| \psi \rangle$ en un estado físico $| 000 \rangle$ o $| 111 \rangle$.
* **Detección:** Uso de operadores de paridad para la medición de síndromes sin colapsar el estado de los datos.

### 2. BB84 Protocol (Quantum Key Distribution)
Implementación del primer protocolo de distribución de claves cuánticas.
* **Simulación:** Generación de bits aleatorios, elección de bases (Rectilínea/Diagonal) y proceso de *Sifting*.
* **Seguridad:** Cálculo de la tasa de error (QBER) para la detección de intrusos (Eve) basada en el principio de incertidumbre.

## Conceptos Teóricos Implementados
* **Teorema de No Clonación:** Base de la seguridad en el protocolo BB84.
* **Superposición y Entrelazamiento:** Fundamentos de la redundancia cuántica.
* **Medición de Síndromes:** Técnica para corregir errores preservando la coherencia.

## Tecnologías
* Python 3.x
