from databricks_workspace.get import Get
from databricks.sdk import WorkspaceClient

def test_should_get_databricks_workspace(mocker):
    
    host = "http://adb-test-workspace.com"
    token = "dapi123"
    
    configuration = Get(host, token)
    
    expected = WorkspaceClient(
        host = configuration.host,
        token = configuration.token
    )
    
    mocker.patch("databricks_workspace.get.Get.databricks_workspace_client", return_value = expected)
    
    actual = Get.databricks_workspace(host, token)
    
    assert expected == actual