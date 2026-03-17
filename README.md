# CRM Laboral: Engineering Solutions Dashboard

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Supabase](https://img.shields.io/badge/Supabase-3ECF8E?style=for-the-badge&logo=supabase&logoColor=white)
![TailwindCSS](https://img.shields.io/badge/tailwindcss-%2338B2AC.svg?style=for-the-badge&logo=tailwind-css&logoColor=white)
![GitHub Pages](https://img.shields.io/badge/github%20pages-121013?style=for-the-badge&logo=github&logoColor=white)

> **"From Hardware Design to Data Intelligence"**

Este proyecto es un ecosistema de gestión de datos diseñado para automatizar y centralizar el seguimiento de procesos de selección técnica. Combina la precisión de la ingeniería electrónica con arquitecturas modernas de software **Serverless**.

## 🏗️ Arquitectura del Sistema (Decoupled)

El proyecto ha evolucionado hacia una estructura de alto rendimiento eliminando latencias de servidores intermedios:

- **`/docs` (Core Interface)**: Interfaz de usuario (Frontend) servida a través de **GitHub Pages**. Se conecta directamente a la capa de datos mediante el SDK de Supabase, eliminando tiempos de _cold-start_.
- **`/backend`**: Lógica de soporte y procesamiento pesado construida con **Python/FastAPI**. Funciona como motor de tareas administrativas y validaciones complejas.
- **`/data_pipeline`**: Motores de ETL (Extract, Transform, Load) para la limpieza y carga de datos masivos hacia la nube.
- **`/database`**: Capa de persistencia en **Supabase (PostgreSQL)** con seguridad **RLS (Row Level Security)** para transacciones directas y seguras.
- **`/research`**: Documentación técnica, investigación en LaTeX y archivos de ingeniería.

## 🛠️ Tech Stack

| Módulo              | Tecnologías                                        |
| :------------------ | :------------------------------------------------- |
| **Frontend**        | HTML5, Tailwind CSS, JavaScript (**Supabase SDK**) |
| **Persistencia**    | Supabase (PostgreSQL) con almacenamiento JSONB     |
| **Data Engine**     | Python 3.14+, FastAPI                              |
| **Infraestructura** | GitHub Pages (Edge), Linux (Fedora/Termux)         |

## 🚀 Características Principales

- **Zero-Latency Connection:** Acceso directo a base de datos optimizado con `preconnect` para un handshake inmediato.
- **Trazabilidad de Ingeniería:** Registro de estrategias basadas en principios **SOLID** y patrones de diseño de sistemas.
- **Arquitectura de Estado Sólido:** Reducción de puntos de falla al eliminar la dependencia de servicios PaaS externos para la visualización.
- **Responsive Design:** Dashboard optimizado para monitoreo desde dispositivos móviles y escritorio.

---

## ⚡ Conectemos

Como **Ingeniero Electrónico** especializado en el desarrollo de software y automatización, busco integrar el rigor del diseño de sistemas con la agilidad de las soluciones modernas en la nube.

[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/MarcosBernardC)

[![Portfolio](https://img.shields.io/badge/Portfolio-FF5722?style=for-the-badge&logo=google-chrome&logoColor=white)](https://marcosbernardc.github.io/PortafolioBernardC/)

**📧 Contacto Directo:** [bernardlab.dev@gmail.com](mailto:bernardlab.dev@gmail.com)  
**📍 Ubicación:** Lima, Perú (Disponible para roles Remotos / Híbridos)

---

_“Engineering is about solving problems with the best tools available, whether they are physical sensors or cloud-based microservices.”_
