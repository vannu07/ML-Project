import dagshub
dagshub.init(repo_owner='vannusingh9', repo_name='ML-Project', mlflow=True)

import mlflow
with mlflow.start_run():
    mlflow.log_param('parameter name', 'value')
    mlflow.log_metric('metric name', 1)
