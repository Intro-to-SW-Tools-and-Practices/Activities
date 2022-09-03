pipeline {
    agent any 
    stages {
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
