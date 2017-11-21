pipeline {
    agent { docker 'python:3.5.1' }
    stages {
        stage('test') {
            steps {
                sh 'pytest'
            }
        }
    }
}