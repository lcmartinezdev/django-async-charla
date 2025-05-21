# Django Asíncrono Demo

Este repositorio contiene el código de ejemplo utilizado en la charla "Django Asíncrono: Desbloqueando el Poder de la Programación Async" para PyCon US.




## 🚀 Descripción

Una demostración práctica de las capacidades asíncronas de Django, comparando el rendimiento entre vistas síncronas y asíncronas al consumir APIs externas. El proyecto incluye ejemplos de:

- Vistas asíncronas vs síncronas
- Llamadas a APIs externas en paralelo
- Uso del ORM asíncrono de Django
- Implementación de `sync_to_async`

## ⚙️ Requisitos

- Python 3.8+
- Django 5.2+
- Cuenta gratuita en [WeatherAPI.com](https://www.weatherapi.com/)

## 🔧 Instalación

1. Clonar el repositorio:
```bash
git clone https://github.com/lcmartinezdev/django-async-charla.git
cd django-async-charla
```

2. Crear y activar un entorno virtual:
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

3. Instalar dependencias:
```bash
pip install -r requirements.txt
```

4. Configurar la API key:
```bash
export WEATHER_API_KEY="tu_api_key_de_weatherapi"
```

## 🏃 Ejecución

### Servidor de desarrollo WSGI (Django tradicional)
```bash
python manage.py runserver
```



## 📊 Demostración

El proyecto incluye dos endpoints principales:

1. `/sync_weather/` - Vista síncrona que hace llamadas secuenciales a WeatherAPI
2. `/async_weather/` - Vista asíncrona que hace llamadas paralelas a WeatherAPI

Cada endpoint consulta el clima de múltiples ciudades y muestra el tiempo total de ejecución.


## 📚 Recursos adicionales

- [Documentación oficial de Django Async](https://docs.djangoproject.com/en/stable/topics/async/)
- [WeatherAPI.com - Docs](https://www.weatherapi.com/docs/)
- [Presentación PyCon US](django-async.pdf)


## 📬 Contacto

- Twitter: [@lcmartinez_](https://c.com/lcmartinez_)
- Web: [lcmartinez.com](https://lcmartinez.com)
- Email: hola@lcmartinez.com

