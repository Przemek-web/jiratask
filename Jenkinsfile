pipeline {
  agent any
  stages {
  stage('install') {
    steps {
        pip3 install jira
    }
}
  stage('build') {
    steps {
        sh 'python3 main.py'
    }
}
  }
}