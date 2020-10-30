pipeline {
  agent any
  stages {
    stage('build') {
    steps {
       withEnv(['PYTHONPATH=/usr/lib/python3/']) {
    sh  'python3 main.py'
}
    }
}
  }
}