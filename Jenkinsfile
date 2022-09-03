pipeline {
    agent any 
    stages {
        stage('checkout') { 
            steps {
                git branch: '*',
                    credentialsId: '11290819-9856-4d42-b861-a0d076b436ea',
                    url: 'git@github.com:Intro-to-SW-Tools-and-Practices/Activities.git'
            }
        }
        stage('Linter') { 
            steps {
                sh 'python --version'
                sh 'pylint --exit-zero *.py'
            }
        }
        stage('UnitTest') { 
            steps {
                sh 'pytest' 
            }
        }
    }
}
