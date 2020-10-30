pipeline {
  agent any
  stages {
    stage('build') {
    steps {
        pip3 install jira
        sh 'python3 main.py'
    }
}
  }
}