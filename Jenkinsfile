pipeline {
  agent any
  stages {
    stage('build') {
    steps {
        export 'PYTHONPATH=$PATH_TO_MODULE:$PYTHONPATH'
        sh 'python3 main.py'
    }
}
  }
}