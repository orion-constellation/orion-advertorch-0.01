    """
    Main interface for MLFlow and Weave integration
    - MLFlow
    - Weave (WandB)
    
    
    
    """

mlflow_settings = {
    'tracking_uri': 'http://localhost:5000'
}

wandb_settings = {
    'api_key': 'your_api_key_here'
}

experiment_config = {
    'tags': ['test', 'sample']
}

flow_config = {
    # Weave configuration details
}

interface = MLWeaveInterface(mlflow_settings, wandb_settings)
interface.run_experiment('Test Experiment', experiment_config, flow_config)
