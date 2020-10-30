pipeline {
  agent any
  stages {
  stage('install') {
    steps {
        pip install jira
    }
}
  stage('build') {
    steps {
        sh 'python3 main.py'
    }
}
  }
}