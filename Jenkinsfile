pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "sahilhub22/student-flask-simple"
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

        stage('Push to DockerHub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', usernameVariable: 'USER', passwordVariable: 'PASS')]) {
                    sh 'echo $PASS | docker login -u $USER --password-stdin'
                    sh 'docker push $DOCKER_IMAGE:$BUILD_NUMBER'
                }
            }
        }

        stage('Deploy') {
            steps {
                echo "Deploy step goes here"
                // Example: sh 'docker run -d -p 5000:5000 $DOCKER_IMAGE:$BUILD_NUMBER'
            }
        }
    }
}
