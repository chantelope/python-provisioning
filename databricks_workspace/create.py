from databricks.sdk import AccountClient

class Create:
    
    def __init__(self, workspace_name, location, pricing_tier):
        self.workspace_name = workspace_name
        self.location = location
        self.pricing_tier = pricing_tier        
    
    def new_databricks_workspace(workspace_name, location, pricing_tier):
              
        configuration = Create(workspace_name, location, pricing_tier)
        
        workspace = Create.workspace_configuration(configuration)
        
        return workspace
    
    def workspace_configuration(configuration):
        
        client = Create.account_client()
        
        account_workspace = client.workspaces
        
        workspace = account_workspace.create_and_wait(
            workspace_name = configuration.workspace_name,
            location = configuration.location,
            pricing_tier = configuration.pricing_tier
        )
        
        return workspace
        
    def account_client():
        
        client = AccountClient()
        
        return client