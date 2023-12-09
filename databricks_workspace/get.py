from databricks.sdk import WorkspaceClient

class Get:
    
    def __init__(self, host, token):
        self.host = host
        self.token = token     
    
    def databricks_workspace(host, token):
              
        configuration = Get(host, token)
        workspace = Get.databricks_workspace_client(configuration)
        
        return workspace
        
    def databricks_workspace_client(configuration):
        
        client = WorkspaceClient(
            host = configuration.host,
            token = configuration.token
        )
        
        return client