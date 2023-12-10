from databricks_workflow.create import Create
from databricks.sdk.service.jobs import CreateResponse, Task, NotebookTask

def test_should_create_databricks_workflow_job(mocker):
    
    host = "http://adb-test-workspace.com"
    token = "dapi123"
    job_name = "test-workspace"
    notebook_path = "Shared/folder"
    task_key = "task-key"
    
    task_list = build_task_list(notebook_path, task_key)
    
    expected = CreateResponse(
        job_id = "job-1"
    )
    
    mocker.patch("databricks_workflow.create.Create.job_task", return_value = task_list)
    mocker.patch("databricks_workflow.create.Create.workflow_configuration", return_value = expected)
    
    actual = Create.new_workflow_job(host, token, job_name, task_list, notebook_path)
    
    assert expected.job_id == actual.job_id
    
def test_should_create_databricks_job_task(mocker):
       
    task_key = "task-key"
    notebook_path = "Shared/folder"
    
    notebook = NotebookTask(
        notebook_path = notebook_path
    )
    
    expected = build_task_list(notebook_path, task_key)
    
    mocker.patch("databricks_workflow.create.Create.notebook_task", return_value = notebook)
    
    actual = Create.job_task(task_key, notebook_path)
    
    assert expected == actual
    
def test_should_create_databricks_notebook_task():
       
    notebook_path = "Shared/folder"
    
    expected = NotebookTask(
        notebook_path = notebook_path
    )
    
    actual = Create.notebook_task(notebook_path)
    
    assert expected == actual
    
def build_task_list(notebook_path, task_key):
    
    notebook = NotebookTask(
        notebook_path = notebook_path
    )
    
    task_list = list()
    
    task = Task(
        task_key = task_key,
        notebook_task = notebook     
    )
    task_list.append(task)
    
    return task_list