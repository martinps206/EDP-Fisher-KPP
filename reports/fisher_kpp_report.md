# Informe Técnico: Modelo de propagación de epidemia con Fisher-KPP

## Objetivo
Simular y analizar la dinámica de una epidemia en un medio biológico continuo usando EDPs.

## Modelo Matemático
\[
\frac{\partial u}{\partial t} = D \frac{\partial^2 u}{\partial x^2} + ru\left(1 - \frac{u}{K}\right)
\]

## Implementación
- Método de Euler explícito
- Método Crank-Nicolson
- Validación con soluciones viajeras
- Exportación de datos para análisis estadístico

## Resultados
- Ondas de propagación confirmadas
- Velocidad dependiente de \( D \) y \( r \)
- El modelo se estabiliza en \( u \to K \)

## Recomendaciones
- Migrar el modelo a 2D para mayor realismo
- Incluir heterogeneidad en el medio
