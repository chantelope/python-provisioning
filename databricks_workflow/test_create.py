from databricks_workflow.create import Create
from databricks.sdk.service.jobs import CreateResponse, Task

def test_should_create_databricks_workflow_job(mocker):
    
    host = "http://adb-test-workspace.com"
    token = "dapi123"
    job_name = "test-workspace"
    task_list = list()
    
    task = Task(
        task_key = "task_key"        
    )
    task_list.append(task)
    
    expected = CreateResponse(
        job_id = "job-1"
    )
    
    mocker.patch("databricks_workflow.create.Create.workflow_configuration", return_value = expected)
    
    actual = Create.new_workflow_job(host, token, job_name, task_list)
    
    assert expected.job_id == actual.job_id