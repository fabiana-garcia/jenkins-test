pipeline {
    agent any
    stages {
        stage('Checkout') { 
            steps {
                git(url: 'https://github.com/fabiana-garcia/jenkins-test', credentialsId: "", branch: "main")
            }
        }
        stage('Build') {
            steps {
                sh 'python -m main.py'
            }
        }
        stage('Test') {
            steps {
               sh 'python -m unittest discover'
            }
        }
    }
    post {
        always {
            junit(
                allowEmptyResults: true,
                testResults: '**/reports/junit/*.xml'
            )
        }
    }
}