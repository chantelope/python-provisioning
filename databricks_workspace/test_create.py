from databricks_workspace.create import Create
from databricks.sdk.service.provisioning import PricingTier, Workspace

def test_should_create_databricks_workspace(mocker):
    
    workspace_name = "test-workspace"
    location = "uksouth"
    pricing_tier = PricingTier.COMMUNITY_EDITION
    
    configuration = Create(workspace_name, location, pricing_tier)
    
    expected = Workspace(
        workspace_name = configuration.workspace_name,
        location = configuration.location,
        pricing_tier = configuration.pricing_tier
    )
    
    mocker.patch("databricks_workspace.create.Create.workspace_configuration", return_value = expected)
    
    actual = Create.new_databricks_workspace(workspace_name, location, pricing_tier)
    
    assert expected == actual