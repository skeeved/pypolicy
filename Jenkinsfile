pipeline {
    agent { dockerfile true }
    stages {
        stage('test') {
            steps {
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