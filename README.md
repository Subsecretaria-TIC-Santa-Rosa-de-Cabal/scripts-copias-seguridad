```bash
pip install -r requirements.txt
```

---

## 📁 Estructura del repositorio

```txt
├── src/                      # Código principal de los scripts
├── .env.example              # Ejemplo de archivo de configuración de entorno
├── requirements.txt          # Dependencias del proyecto
└── README.md                # Este archivo
```

---

## ⚙️ Configuración

1. **Clonar el repositorio:**

   ```bash
   git clone https://github.com/Subsecretaria-TIC-Santa-Rosa-de-Cabal/scripts-copias-seguridad.git
   ```

2. **Copiar y editar el archivo de ejemplo de variables:**

   ```bash
   cp .env.example .env
   # Edita .env con tus rutas, credenciales y ajustes de backup
   ```

3. **Instalar dependencias:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configurar tareas programadas** (por ejemplo, con cron o systemd timers) para ejecutar automáticamente los scripts según tus necesidades.

---