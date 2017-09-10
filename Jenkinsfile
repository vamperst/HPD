pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        sh 'ls -l'
      }
    }
    stage('Tests') {
      steps {
        sleep 5
      }
    }
    stage('Approval') {
      steps {
        input 'Voce aprova para deploy?'
      }
    }
    stage('Deploy') {
      steps {
        sh 'echo "fazendo deploy"'
        sh 'docker build -f ruby/rest-api/Dockerfile -t test-docker-jenkins .'
      }
    }
    stage('Finalizando') {
      steps {
        sh 'echo "fazendo finalizando"'
        sh 'docker run -d -p 4567:4567 test-docker-jenkins ruby application.rb'
      }
    }
  }
}