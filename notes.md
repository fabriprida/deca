1. Inicializar GIT
    echo "# deca" >> README.md
    git init
    git add README.md
    git commit -m "first commit" 
    git branch -M main --> renombra la rama actual de master a main.
    git remote add origin https://github.com/fabriprida/deca.git --> agrega un repo remoto bajo el nombre 'origin'
    git push -u origin main  --> establece una relación entre esta rama local y origin main, para que al hacer push no haga falta decir a dónde.

2. BACKEND
  - Crear carpeta /backend. 
  - Crear virtualenv venv. 
  - Instalar dependencias con un requirements.txt: pip install fastapi uvicorn.
  - Crear main.py
  - Ejecutar servidor: uvicorn main:app --reload. 
    - El --reload habilita hot reload. 
    - Corre en 127.0.0.1:8000. En /docs se encuentra el swagger. 

3. FRONTEND 
  - Desde la carpeta raíz, creamos la aplicación React: npm create vite@latest frontend --template react
  - Instalamos dependencias y ejecutamos el servidor: 
    - cd frontend
    - npm install
    - npm run dev

4. PROXY
    - Configurar un proxy en Vite para que el frontend hable con el backend sin problemas. Las solicitudes que comiencen con 
    /api se redigiren al backend. 

5. 