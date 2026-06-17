## INTEGRANTES DEL PROYECTO:

Evelin Xiomara Astudillo Pedroza ()"\n"
Roony Alejandro Ausecha Lourido (Roony20-2026)
Jhojan Andrés Martínez Peñafiel (Jhojan9343)
Felipe Ramírez Peñafiel (d1z1-3)
Paola Andrea Torres Guerra (paolatorres-png)

## Descripción
Proyecto enfocado en la implementación de contenedores y despliegue en Kubernetes (k8s), estructurado para el entorno de sistemas operativos.

## Estructura del Repositorio
* `/backend`: código fuente del servidor HTTP en Python (Puerto 5000) y su respectivo Dockerfile de construcción basado en la distribución asignada.
* `/frontend`: archivos web estáticos de la aplicación y la configuración del servidor Nginx con sus volúmenes persistentes.
* `/k8s`: manifiestos de configuración de Kubernetes (Deployment y Service) para el despliegue orquestado en Minikube, configuración de 3 réplicas y exposición mediante NodePort.
* `/docs`: espacio exclusivo para el portal web de documentación técnica publicado en GitHub Pages, evitando conflictos de enrutamiento con los entornos de contenedores.
* `docker-compose.yml`: archivo de orquestación local multiconteiner para enlazar y validar la comunicación de los servicios de frontend y backend.
