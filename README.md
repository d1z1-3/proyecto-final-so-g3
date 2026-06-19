# Proyecto Final — Arquitecto Cloud
**Sistemas Operativos 750001C | Semestre 1 – 2026**
**Universidad del Valle**

---

## Equipo

| Nombre | Código | Rol |
|--------|--------|-----|
| Evelin Xiomara Astudillo Pedroza (XiomaraAP) | 2477871 | Sitio web |
| Roony Alejandro Ausecha Lourido (Roony20-2026) | 2477957 | Documentación y sitio web |
| Jhojan Andrés Martínez Peñafiel (Jhojan9343) | 2478060 | Kubernetes / Orquestación |
| Felipe Ramírez Peñafiel (d1z1-3) | 2478061 | Backend Developer |
| Paola Andrea Torres Guerra (paolatorres-png) | 2478101 | Video y sitio web |

**Grupo asignado:** Grupo 3  
**Distribución gráfica:** Fedora 44  
**Distribución consola:** Fedora 44 Server  
**Imagen Docker base:** fedora:44

---

## Descripción
Proyecto enfocado en la implementación de contenedores y despliegue en Kubernetes (k8s), estructurado para el entorno de sistemas operativos.

---

## Estructura del Repositorio
* `/backend`: código fuente del servidor HTTP en Python (Puerto 5000) y su respectivo Dockerfile de construcción basado en la distribución asignada.
* `/frontend`: archivos web estáticos de la aplicación y la configuración del servidor Nginx con sus volúmenes persistentes.
* `/k8s`: manifiestos de configuración de Kubernetes (Deployment y Service) para el despliegue orquestado en Minikube, configuración de 3 réplicas y exposición mediante NodePort.
* `/docs`: espacio exclusivo para el portal web de documentación técnica publicado en GitHub Pages, evitando conflictos de enrutamiento con los entornos de contenedores.
* `docker-compose.yml`: archivo de orquestación local multiconteiner para enlazar y validar la comunicación de los servicios de frontend y backend.

---

## Componente 1: Virtualización con Linux

**Distribuciones instaladas:** VM Gráfica + VM Consola  
**Herramienta:** VirtualBox / VMware

### Evidencias
- Captura instalación VM gráfica
- Captura particionamiento (lsblk)
- Captura configuración de red
- Captura prueba SSH funcional

### Comandos principales
```bash
ip a                               # Ver interfaces de red
lsblk                               # Ver particiones
ssh usuario@ip_vm_consola           # Conectar por SSH
```

---

## Componente 2: Contenedores Docker

**Servicios implementados:**
- Frontend: Nginx sirviendo HTML estático (puerto 80) con volúmenes persistentes.
- Backend: Python HTTP (puerto 5000) basado en la distribución asignada.

### Evidencias
- Captura `docker compose up -d` (Validación y enlace multicontenedor)
- Captura navegador accediendo al frontend
- Captura `curl http://localhost:5000`

### Comandos principales
```bash
docker compose up -d
docker ps
docker images
curl http://localhost
curl http://localhost:5000
```

---

## Componente 3: Orquestación con Kubernetes

**Herramienta:** Minikube

### Manifiestos
Ubicados en la carpeta `/k8s`:
- `backend-deployment.yaml` — Configuración optimizada con 3 réplicas para el despliegue orquestado del backend.
- `frontend-nginx.yaml` — Configuración del despliegue del frontend con Nginx.
- Exposición mediante NodePort en puerto 30080.

### Evidencias
- Captura `kubectl get pods` (Mostrando las 3 réplicas corriendo)
- Captura `kubectl get svc`
- Captura acceso desde navegador
- Captura escalado a 3 réplicas

### Comandos principales
```bash
minikube start
kubectl apply -f k8s/backend-deployment.yaml
kubectl apply -f k8s/frontend-nginx.yaml
kubectl get pods
kubectl get svc
minikube service [nombre-servicio] --url
```

---

## Componente 4: Sitio Web de Documentación

**URL del sitio:** [https://d1z1-3.github.io/proyecto-final-so-g3/]  
**Video YouTube:** [https://youtu.be/...]

### Secciones del sitio
El portal web técnico está aislado en el directorio `/docs` para evitar conflictos de enrutamiento con los contenedores:
- Home: introducción y objetivos
- Equipo: integrantes con fotos y roles
- Componentes: descripción, capturas y comandos de cada uno
- Conclusiones: aprendizajes, dificultades y recomendaciones

---

## Diagrama de Arquitectura

> Insertar imagen del diagrama (draw.io / Miro / Lucidchart) indicando el flujo entre Nginx, el backend en Python y el clúster de Kubernetes.

---

## Conclusiones

1. [Aprendizaje principal sobre el despliegue y escalado de réplicas en k8s]
2. [Dificultad encontrada con las rutas/conflictos de Docker y cómo aislar la documentación en la carpeta /docs para GitHub Pages lo solucionó]
3. [Recomendación para futuros proyectos]

---

*Proyecto desarrollado para la asignatura Sistemas Operativos 750001C — Semestre 1, 2026*
