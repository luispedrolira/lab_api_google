## Paso 1 — Configuración del proyecto en GCP

Se configuró el proyecto en GCP Console y se estableció el Project ID activo mediante Cloud Shell.

![Configuración del proyecto en Cloud Shell](/img/paso-uno.png)

---

## Paso 2 — Habilitación de APIs necesarias

Se habilitaron los servicios requeridos para el laboratorio mediante el siguiente comando:

```bash
gcloud services enable \
  cloudfunctions.googleapis.com \
  cloudbuild.googleapis.com \
  places-backend.googleapis.com \
  run.googleapis.com
```

La operación finalizó exitosamente.

![Habilitación de APIs en Cloud Shell](/img/paso-dos.png)

---

## Paso 3 — Creación y restricción de la API Key

Se generó una API Key en GCP Console bajo *APIs & Services > Credentials*. Se aplicaron dos restricciones de seguridad:

- **Restricción de API:** limitada únicamente a Places API
- **Restricción de IP:** configurada con la IP pública de la máquina

Esto garantiza que la key no pueda ser utilizada desde otro origen aunque sea interceptada.

![API Key con restricciones aplicadas](/img/paso-tres.png)

---

## Paso 4 — Prueba local de la Cloud Function

Se implementaron los archivos `main.py` y `requirements.txt` y se probó la función localmente usando `functions-framework` antes de hacer el deploy a la nube.

**Comando para levantar el servidor local:**
```bash
functions-framework --target=maps_query --port=8080
```

**Comando de prueba:**
```bash
curl "http://localhost:8080?place=Mercado+Central+Guatemala"
```

La función respondió correctamente con datos geográficos en formato JSON, incluyendo coordenadas, nombre del lugar y `place_id`.

![Prueba local exitosa con curl](/img/paso-cuatro.png)

---

## Paso 5 — Deploy a Google Cloud Functions

Se realizó el deploy de la función a GCP usando Cloud Shell con el siguiente comando:

```bash
gcloud functions deploy maps-query \
  --gen2 \
  --runtime=python312 \
  --region=us-central1 \
  --source=. \
  --entry-point=maps_query \
  --trigger-http \
  --allow-unauthenticated \
  --set-env-vars MAPS_KEY=TU_API_KEY
```

El deploy finalizó con estado `ACTIVE` y GCP asignó la URL pública de invocación.

![Deploy exitoso de la Cloud Function](/img/paso-cinco.png)

**URL pública asignada:**
```
https://us-central1-boxwood-well-495323-r4.cloudfunctions.net/maps-query
```

![Invocación de la Cloud Function](/img/paso-seis.png)
