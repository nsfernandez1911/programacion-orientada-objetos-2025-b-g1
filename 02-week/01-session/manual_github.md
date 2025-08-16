# 📘 Manual paso a paso para clonar, publicar y administrar un repositorio en GitHub

Este manual está diseñado para guiarte desde cero en el uso de **Git** y **GitHub**, explicando cómo clonar, publicar y administrar un repositorio.

---

## 🔧 1. Requisitos previos

Antes de empezar asegúrate de tener lo siguiente:

- Una cuenta en [GitHub](https://github.com/).
- Git instalado en tu computadora:  
  - **Windows:** Descárgalo desde [git-scm.com](https://git-scm.com/).  
  - **Linux (Debian/Ubuntu):**  
    ```bash
    sudo apt update && sudo apt install git -y
    ```
  - **MacOS (Homebrew):**  
    ```bash
    brew install git
    ```
- Un editor de código como [Visual Studio Code](https://code.visualstudio.com/).

Verifica la instalación de git con:
```bash
git --version
```

---

## 👤 2. Configurar tu identidad en Git

Configura tu nombre de usuario y correo (el mismo que usas en GitHub):

```bash
git config --global user.name "Tu Nombre"
git config --global user.email "tu_correo@example.com"
```

Verifica la configuración con:
```bash
git config --list
```

---

## 🌱 3. Crear un nuevo repositorio en GitHub

1. Inicia sesión en [GitHub](https://github.com/).
2. Haz clic en **New repository**.
3. Asigna un nombre al repositorio, por ejemplo: `mi-proyecto`.
4. Opcional: añade una descripción.
5. Selecciona si será **público** o **privado**.
6. Marca la opción **Initialize this repository with a README** (opcional pero recomendado).
7. Haz clic en **Create repository**.

---

## 📂 4. Clonar un repositorio de GitHub a tu computadora

Ve al repositorio creado y copia la URL en la opción **HTTPS** o **SSH** (recomendado si usas llaves SSH).

Ejemplo con HTTPS:
```bash
git clone https://github.com/usuario/mi-proyecto.git
```

Esto descargará el repositorio en una carpeta llamada `mi-proyecto`.

Entra al directorio:
```bash
cd mi-proyecto
```

---

## ✍️ 5. Hacer cambios y guardarlos en el repositorio local

1. Crea o modifica un archivo, por ejemplo:
   ```bash
   echo "# Hola GitHub" > hola.md
   ```

2. Agrega el archivo al área de preparación:
   ```bash
   git add hola.md
   ```

3. Guarda los cambios con un mensaje (commit):
   ```bash
   git commit -m "Agrego archivo hola.md"
   ```

---

## 🚀 6. Subir cambios al repositorio remoto en GitHub

Envía los cambios al repositorio en GitHub:
```bash
git push origin main
```

> **Nota:** si tu rama principal se llama `master`, reemplaza `main` por `master`.

---

## 📥 7. Actualizar tu repositorio local con los cambios de GitHub

Si alguien más hace cambios en GitHub o trabajas en otro equipo/computadora:

```bash
git pull origin main
```

---

## 🌳 8. Crear y usar ramas (branches)

Las ramas permiten trabajar en nuevas funcionalidades sin afectar la principal.

1. Crear una nueva rama:
   ```bash
   git checkout -b nueva-funcionalidad
   ```

2. Ver ramas disponibles:
   ```bash
   git branch
   ```

3. Cambiar a otra rama:
   ```bash
   git checkout main
   ```

4. Fusionar una rama con la principal:
   ```bash
   git merge nueva-funcionalidad
   ```

---

## 🛠️ 9. Administrar repositorios en GitHub

- **Ver historial de commits:**
  ```bash
  git log --oneline
  ```

- **Eliminar una rama local:**
  ```bash
  git branch -d nombre-rama
  ```

- **Eliminar una rama en GitHub:**
  ```bash
  git push origin --delete nombre-rama
  ```

- **Ignorar archivos no deseados:**  
  Crea un archivo llamado `.gitignore` y escribe dentro los nombres de carpetas o archivos a excluir. Ejemplo:
  ```
  node_modules/
  .env
  ```

---

## 🔒 10. Consejos de buenas prácticas

- Haz commits pequeños y frecuentes.
- Usa mensajes de commit claros (ej: `feat: agregar login de usuario`).
- Siempre sincroniza antes de empezar a trabajar (`git pull`).
- Usa ramas para nuevas funciones o correcciones.
- No subas información sensible (contraseñas, API keys).

---

## ✅ Resumen rápido de comandos

```bash
# Clonar un repositorio
git clone URL

# Ver estado de cambios
git status

# Agregar archivos al área de preparación
git add archivo.txt

# Guardar cambios
git commit -m "mensaje"

# Subir cambios a GitHub
git push origin main

# Descargar cambios desde GitHub
git pull origin main
```

---

## 📚 Recursos recomendados

- [Documentación oficial de Git](https://git-scm.com/doc)
- [GitHub Docs](https://docs.github.com/)
- Tutorial visual: [https://learngitbranching.js.org](https://learngitbranching.js.org)

---
