# Proyecto Final — Arquitecto Cloud
**Sistemas Operativos 750001C | Semestre 1 – 2026**
**Universidad del Valle**

---

## Equipo

| Nombre | Código | Rol |
|--------|--------|-----|
| Evelin Xiomara Astudillo Pedroza (XiomaraAP) | 2477871 | Sitio web y Video|
| Roony Alejandro Ausecha Lourido (Roony20-2026) | 2477957 | Documentación y Sitio Web |
| Jhojan Andrés Martínez Peñafiel (Jhojan9343) | 2478060 | Kubernetes / Orquestación |
| Felipe Ramírez Peñafiel (d1z1-3) | 2478061 | Backend Developer |
| Paola Andrea Torres Guerra (paolatorres-png) | 2478101 | Video y Sitio Web |

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
- Arquitectura: diagrama de arquitectura del proyecto
- Conclusiones: aprendizajes, dificultades y recomendaciones

---

## Diagrama de Arquitectura

> Insertar imagen del diagrama (draw.io / Miro / Lucidchart) indicando el flujo entre Nginx, el backend en Python y el clúster de Kubernetes.

---

## Conclusiones

### Aprendizajes
Lograr el despliegue con Minikube y mantener las réplicas activas fue el punto de inflexión del trabajo. Entender cómo Kubernetes gestiona la alta disponibilidad, viendo cómo el sistema reacciona para mantener los pods arriba, nos dio una perspectiva clara de lo que significa que un servicio sea realmente estable. Fue un proceso de aprender a dominar las herramientas de orquestación, entendiendo que la robustez del sistema depende de cómo configuramos cada pieza.

### Las dificultades reales
Nuestro mayor obstáculo no fue el código en sí, sino la infraestructura física con la que trabajamos. Al tener dispositivos con almacenamiento limitado y recursos muy ajustados para las máquinas virtuales, el proceso se volvió una lucha constante. Muchas veces el despliegue se interrumpía o quedaba a medias simplemente porque el sistema se quedaba sin espacio o se ahogaba por falta de memoria. Esto nos obligó a ser extremadamente cuidadosos y creativos para buscar espacio donde parecía no haberlo, lo que hizo que el proceso fuera mucho más lento y trabajoso de lo que esperábamos. Esa limitación física fue lo que realmente puso a prueba nuestra paciencia y capacidad para resolver problemas sobre la marcha.

### Recomendaciones técnicas
* **Gestión de recursos (Limit/Requests):** Es indispensable establecer `resources.limits` y `resources.requests` en los manifiestos YAML. Esto evita que el scheduler de Kubernetes sobreasigne recursos a los pods, previniendo el *node pressure* o el *eviction* de contenedores por falta de memoria RAM en entornos con hardware restringido.
* **Optimización de imágenes (Multi-stage builds):** Ante las limitaciones de almacenamiento, se recomienda implementar *multi-stage builds* en los Dockerfiles. Esto permite generar imágenes finales que solo contienen el artefacto compilado y las dependencias de ejecución, reduciendo drásticamente el peso de la imagen y ahorrando espacio en disco durante el *pulling*.
* **Uso de volúmenes efímeros:** Para procesos que requieren escritura temporal, se sugiere el uso de volúmenes de tipo `emptyDir` con un límite explícito de tamaño (`sizeLimit`). Esto asegura que el sistema no exceda la capacidad de almacenamiento del nodo durante la ejecución de los pods.
* **Limpieza de clúster:** Establecer un hábito de ejecución de comandos de purga de recursos huérfanos (`docker system prune` o `kubectl delete` de pods en estado `Evicted` o `Failed`) es necesario para liberar espacio en disco de forma periódica en ambientes de desarrollo con recursos limitados.

---

*Proyecto desarrollado para la asignatura Sistemas Operativos 750001C — Semestre 1, 2026*
---
