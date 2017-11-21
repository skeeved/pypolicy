pipeline {
    agent { docker 'python:3.5.1' }
    stages {
        stage('test') {
            steps {
                sh 'sudo yum -y install python3-pytest'
                sh 'pytest'
            }
        }
    }
    post {
    success {
        slackSend channel: '#general',
                  color: 'good',
                  message: "The pipeline ${currentBuild.fullDisplayName} completed successfully."
        }
    }
}