pipeline {
    agent any
    stages {
        stage('Checkout') { 
            steps {
                git(url: 'git@github.com:fabianamasini/jenkins-test.git', credentialsId: "", branch: "main")
            }
        }
        stage('Build') {
            steps {
                
            }
        }
        stage('Test') {
            steps {
               
            }
        }
    }
    post {
        always {
            junit(
                allowEmptyResults: true,
                testResults: '**/reports/junit/*.xml'
            )
            discordSend(description: "**Build number:** ${currentBuild.number}\n**Status:** ${currentBuild.currentResult}", footer: "", result: currentBuild.currentResult, title: JOB_NAME, webhookURL: "https://discordapp.com/api/webhooks/751121752079466587/aHybhfYyDJBDNgMva7hTYtwLkcVYHJCACiI5JDchjSli5APmMljAfRXVRTvLEejCDFbJ")
        }
    }
}