from azure.identity import DefaultAzureCredential
from azure.mgmt.appcontainers import ContainerAppsAPIClient

class Create:
    
    def __init__(self, subscription_id, resource_group, location, app_name, env_name):
        self.subscription_id = subscription_id
        self.resource_group = resource_group
        self.location = location
        self.name = app_name
        self.env_name = env_name
    
    def container_app(subscription_id, resource_group, location, app_name, env_name):
        
        configuration = Create(subscription_id, resource_group, location, app_name, env_name)
        
        app = Create.app(configuration)
        
        return app
    
    def app(configuration):
        
        client = Create.container_app_client(configuration.subscription_id)
        
        client.managed_environments.begin_create_or_update(
            resource_group_name = configuration.resource_group,
            environment_name = configuration.env_name,
            environment_envelope = {
                "location": f"{configuration.location}"
            }
        )
        
        managedEnvironment = client.managed_environments.get(configuration.resource_group, "")
        
        client.container_apps.begin_create_or_update(
            resource_group_name = configuration.resource_group,
            container_app_name = configuration.name,
            container_app_envelope = {
                "location": f"{configuration.location}",
                "environmentId": f"{managedEnvironment.id}"
            }            
        )
        
        container_app = client.container_apps.get(configuration.resource_group, configuration.name)
        
        if container_app.id is not None:
            
            return True
        
        return False    
    
    def container_app_client(subscription_id):
        
        client = ContainerAppsAPIClient(
            credential = DefaultAzureCredential(),
            subscription_id = subscription_id
        )
        
        return client