    """
    PROMETHEOUS MONITORING:
    - Monitoring the model and framework
    
    
    
    
    """
from prometheus_fastapi_instrumentator import Instrumentator
import fastapi 


def create_app() -> FastAPI:
    app = FastAPI()

    # Instrument the app for Prometheus
    Instrumentator().instrument(app).expose(app)

    return app

app = create_app()
    