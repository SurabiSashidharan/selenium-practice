pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'C:\\Users\\Yaashvy\\anaconda3\\python.exe -m venv .venv'
                bat '.venv\\Scripts\\pip install -r requirements.txt'
            }
        }       

        stage('Run Tests') {
            steps {
                bat '.venv\\Scripts\\pytest -v --html=report.html --self-contained-html'
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'report.html', allowEmptyArchive: true
        }
    }
}