pipeline {
  agent any
  stages {
    stage('build') {
    steps {
        pip install jira
        sh 'python3 main.py'
    }
}
  }
}