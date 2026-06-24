pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "student-flask-simple"
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/sahilhub22/student-flask-simple.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh 'docker build -t $DOCKER_IMAGE:$BUILD_NUMBER .'
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    // Stop old container if running
                    sh 'docker rm -f student-flask || true'
                    // Run new container
                    sh 'docker run -d --name student-flask -p 5000:5000 $DOCKER_IMAGE:$BUILD_NUMBER'
                }
            }
        }
    }
}
