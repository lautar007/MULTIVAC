# 🏡 MULTIVAC — Intérprete DSL SmartHome y Traductor a HTML

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg?logo=python&logoColor=white)](#)
[![Licencia: MIT](https://img.shields.io/badge/Licencia-MIT-green.svg)](#)
[![Dominio](https://img.shields.io/badge/Dominio-IoT%20%7C%20Compiladores%20%7C%20Automatizaci%C3%B3n-orange.svg)](#)

> Intérprete, analizador léxico/sintáctico y generador de código para un Lenguaje de Dominio Específico (DSL) reactivo orientado a la automatización de hogares inteligentes y entornos IoT. Desarrollado en el marco de la cátedra *Sintaxis y Semántica de los Lenguajes* (Ingeniería en Sistemas de Información — UTN FRRe).

---

## 📌 Descripción General

**MULTIVAC** es un motor de análisis estático e interpretación diseñado para procesar scripts declarativos y reactivos de domótica. En lugar de lidiar con interfaces complejas o sistemas dispersos, el usuario define reglas claras basadas en eventos de sensores físicos, control de actuadores, temporizadores y condiciones lógicas.

El núcleo del sistema analiza el texto, reconoce componentes léxicos, valida la estructura gramatical, detecta y reporta errores con precisión de línea y genera automáticamente un panel de control interactivo en formato HTML.

---

## ✨ Características Principales

- 🔍 **Análisis Léxico y Sintáctico Completo:**
  - Reconocimiento de palabras reservadas del dominio (`WHEN`, `EVERY`, `IF/THEN/ELSE`, `DO`, `END`).
  - Detección de literales y unidades compuestas contextuales (`°C`, `%`, `lux`, `s/m/h`, formatos de hora `HH:MM` y fechas `DD/MM/AAAA`).
  - Notación de punto para dispositivos y atributos (`dispositivo.atributo`).
- 🛡️ **Control Riguroso y Gestión de Errores:**
  - Detección de errores léxicos (símbolos inválidos, tokens no reconocidos).
  - Control de consistencia sintáctica y de ejecución (rutas o extensiones inválidas).
  - Reporte explícito con número de línea, cadena conflictiva y tipo de falla.
- 🌐 **Traductor y Generador de Dashboard HTML:**
  - Conversión directa de reglas analizadas a componentes visuales web (`<div>`, `<h1>`, listas estructuradas y enlaces `mailto:` automáticos para alertas por correo).
- ⚡ **Doble Modo de Ejecución:**
  - **Modo Interactivo (CLI):** Evaluación y reconocimiento de tokens en tiempo real para pruebas y depuración rápida.
  - **Ejecución desde Archivo:** Procesamiento en lote de archivos de reglas con extensión `.smart`.

---

## 🛠️ Tecnologías y Fundamentos Teóricos

- **Lenguaje Principal:** Python 3.10+
- **Conceptos de Ciencias de la Computación aplicados:**
  - Gramáticas Libres de Contexto (GLC / CFG)
  - Análisis Léxico (Scanner/Lexer) y Sintáctico (Parser)
  - Expresiones Regulares y Autómatas Finitos
  - Tablas de Símbolos y Árboles Sintácticos (AST)
  - Traducción dirigida por sintaxis (Generación de código HTML)

---

## 📂 Ejemplo de Sintaxis del Lenguaje (`.smart`)

El lenguaje implementa una lógica basada en eventos y condiciones reactivas:

```smart
// Activación automática de iluminación según luminosidad ambiental
WHEN sensor_luz < 250lux DO
    foco_entrada.estado = ON
    foco_entrada.brillo = 80%
    foco_patio.estado = ON
    foco_patio.color = blue
END

// Tarea periódica programada
EVERY 30m DO
    IF reloj.hora > 22:00 AND alarma.estado == OFF THEN
        persiana_sala.posicion = 0%
        cerradura_principal.estado = ON
        altavoz_comedor.mensaje = "Modo noche activado. Puertas aseguradas."
        altavoz_comedor.email = admin@smart-home.com.ar
    END
END

// Regla de seguridad y emergencia
IF sensor_humo == TRUE AND aire_acondicionado.estado == OFF THEN
    aire_acondicionado.estado = ON
    aire_acondicionado.modo = FRIO
    cerradura_principal.estado = OFF
    persiana_comedor.posicion = 100%
    altavoz_comedor.mensaje = "PELIGRO: Humo detectado en la vivienda."
    altavoz_comedor.email = bomberos@smart-home.com.ar
END
```
