# 🎨 ARMONÍAS ANCESTRALES

> **Reviviendo la Naturaleza: Reconexión, Inspiración y Armonía en Cada Proyección**

---

## 📋 Descripción del Proyecto

**Armonías Ancestrales** es un proyecto innovador de arte y reconexión que surge en respuesta a los recientes incendios forestales en Bogotá. A través de proyecciones interactivas, talleres colaborativos y experiencias inmersivas, buscamos reconectar a las comunidades con su entorno natural.

Este sitio web presenta las actividades, información sobre preparación, y una galería de eventos relacionados con la iniciativa.

---

## 🛠️ Stack Tecnológico

### Composición del Proyecto:
- **HTML**: 62.1% - Estructura y contenido
- **CSS**: 33.9% - Estilos y diseño responsivo
- **JavaScript**: 0.5% - Interactividad del cliente
- **Python**: 3.5% - Scripts de utilidad (automatización de navbars)

### Tecnologías Principales:

#### Frontend
- **HTML5**: Estructura semántica
- **CSS3**: 
  - Diseño responsivo con media queries
  - Flexbox y Grid
  - Animaciones y transiciones
  - Variables CSS
  
- **JavaScript Vanilla**: 
  - Navegación responsiva (toggle de menú)
  - Carrusel de imágenes automático
  - Modales interactivos
  - Toggle de contenido expandible

#### Librerías Externas
- **Google Fonts**: Montserrat, Roboto Mono, Open Sans, Staatliches
- **Slick Carousel**: Carrusel de imágenes (opcional, importado vía CDN)

#### Scripts Utilitarios
- **Python**: Script `fix_navbars.py` para unificar barras de navegación en múltiples archivos HTML

---

## 📁 Estructura del Proyecto

```
armonias/
├── index.html                          # Página principal
├── prueba.html                         # Página de prueba
├── armonias.css                        # Estilos globales
├── armonias.js                         # Scripts globales
├── cards.css                           # Estilos de tarjetas
├── fix_navbars.py                      # Script de automatización
│
├── sections/                           # Sección de páginas principales
│   ├── actividades.html               # Página de actividades
│   ├── preparacion.html               # Página de preparación
│   ├── abtus.html                     # Página "Sobre nosotros"
│   ├── actividadesPrueb.html          # Prueba de actividades
│   └── section.css                    # Estilos de secciones
│
├── actividades/                        # Detalles de actividades
│   ├── act.css                        # Estilos de actividades
│   ├── act1.html                      # Taller de tejido
│   ├── act2.html                      # Segundo taller de tejido
│   ├── act3.html                      # Coloquio Armonías
│   └── act4.html                      # Taller de pigmentos naturales
│
├── preparacion/                        # Información de preparación
│   └── dias.css                       # Estilos de días/preparación
│
└── img/                                # Recursos de imagen
    ├── logo.png
    ├── icono.webp
    ├── carousel/                      # Imágenes del carrusel
    └── ...
```

---

## 🎯 Características Principales

### 📱 Página Principal (Index)
- **Carrusel Automático**: Rotación de imágenes cada 7 segundos
- **Navegación Responsiva**: Menú hamburguesa en dispositivos móviles
- **Calendario de Actividades**: Grid de eventos con estado (Finalizado/Próximo)
- **Marcas Colaboradoras**: Sección de logos animados en bucle infinito
- **Cards Interactivas**: Secciones de Actividades y Preparación

### 🎪 Secciones Principales

#### 1. **Actividades**
- Listado de talleres y eventos
- Modales con imágenes
- Contenido expandible (Show More/Ver Más)
- Grid responsive de imágenes

#### 2. **Preparación**
- Información sobre equipamiento
- Guía de preparación
- Galerías de imágenes interactivas

#### 3. **Sobre Nosotros**
- Equipo y contexto del proyecto
- Miembros destacados

---

## 🎨 Diseño y Estilos

### Paleta de Colores
- **Verde Principal**: `#5ba92f`, `#6a994e`, `#51d146`
- **Verde Oscuro**: `#081C15`
- **Grises**: `#222`, `#333`, `#d2d2d2`, `#242424`
- **Naranja Secundario**: `#f8a40b`
- **Blanco**: `#ffffff`

### Tipografía
- **Montserrat**: Títulos y encabezados (peso: 800)
- **Roboto Mono**: Cuerpo de texto y descripciones
- **Open Sans**: Elementos especiales
- **Staatliches**: Footer

### Responsividad
- **Mobile**: Max-width 600px
- **Tablet**: 768px
- **Desktop**: 1024px+

---

## ⚡ Funcionalidades JavaScript

### Navegación
```javascript
// Toggle del menú en dispositivos móviles
document.querySelector('.menu-toggle').addEventListener('click', () => {
    document.querySelector('.navbar ul').classList.toggle('showing');
});
```

### Carrusel
```javascript
// Rotación automática cada 7 segundos
setInterval(nextSlide, 7000);
```

### Modales Interactivos
```javascript
// Abre y cierra galerías con zoom
function toggleContent(id) {
    var content = document.getElementById(id);
    content.style.display = (content.style.display === "none") ? "block" : "none";
}
```

---

## 🐍 Utilidad Python

### `fix_navbars.py`
Script automatizado que unifica las barras de navegación en todos los archivos HTML del proyecto.

**Uso:**
```bash
python fix_navbars.py
```

**Funcionalidad:**
- Procesa archivos root: `index.html`, `prueba.html`
- Procesa subdirectorios: `sections/`, `actividades/`, `preparacion/`
- Reemplaza automáticamente los elementos `<nav>` con una plantilla unificada
- Ajusta rutas relativas según la profundidad de carpetas

---

## 🚀 Cómo Usar

### Instalación
1. Clona el repositorio:
   ```bash
   git clone https://github.com/Danvegamo/armonias.git
   ```

2. Navega al directorio:
   ```bash
   cd armonias
   ```

3. Abre `index.html` en tu navegador (o usa un servidor local)

### Servidor Local (Recomendado)
```bash
# Con Python 3
python -m http.server 8000

# Con Node.js (http-server)
npx http-server
```

Luego accede a `http://localhost:8000`

---

## 📸 Galería de Actividades

El proyecto incluye varios talleres y eventos:

- **🧵 Talleres de Tejido Colectivo** - Fecha: 8 de agosto de 2024
- **💬 Coloquio Armonías** - Fecha: 9 de agosto de 2024
- **🧵 Segundo Taller de Tejido** - Fecha: 15 de agosto de 2024
- **🎨 Taller de Pigmentos Naturales** - Fecha: 22 de agosto de 2024

---

## 🤝 Marcas Colaboradoras

El proyecto cuenta con el apoyo de múltiples marcas y organizaciones comprometidas con la sostenibilidad y reconexión natural. Las marcas se muestran en una sección animada en la página principal.

---

## 📞 Contacto

Para más información o colaboraciones, contacta a través del formulario en el sitio web o a través del botón "Contactate con nosotros" en la navegación.

**Eslogan:** *"Reconecta con tu entorno natural"*

---

## 📝 Licencia

Información sobre la licencia no disponible en este momento.

---

## 🔧 Cambios Recientes

- ✅ Unificación automática de barras de navegación
- ✅ Implementación de carrusel automático
- ✅ Diseño completamente responsivo
- ✅ Integración de modales interactivos
- ✅ Animaciones y transiciones suaves
- ✅ Script Python para automatización

---

## 💡 Notas de Desarrollo

- El sitio es un **fork** del proyecto original `blekk111/armonias`
- Utiliza principalmente **HTML, CSS y JavaScript vanilla** (sin frameworks pesados)
- Enfoque en **accesibilidad** y **experiencia móvil**
- Incluye utilidades de automatización con Python para mantenimiento
- Pesos de archivo optimizados (imágenes en formato `.webp`)

---

## 🎓 Aprendizajes Técnicos

Este proyecto demuestra:
- Desarrollo **frontend puro** sin frameworks
- Técnicas de **diseño responsivo** moderno
- Uso de **CSS Grid y Flexbox**
- Animaciones con **keyframes CSS**
- Manipulación del **DOM con JavaScript vanilla**
- Scripts de utilidad con **Python**
- Optimización de imágenes

---

**Creado por:** [@Danvegamo](https://github.com/Danvegamo)  
**Repositorio:** [Danvegamo/armonias](https://github.com/Danvegamo/armonias)  
**Última actualización:** Junio 2026
