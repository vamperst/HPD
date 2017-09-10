pipeline {
  agent {
    docker {
      image 'ubuntu'
    }
    
  }
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
        sh 'fpm -m "ops team" --url "http://firma.org" --description "nossa" -a noarch -s dir -t rpm -n hpd --rpm-user root --rpm-group root -v 0.0.1 --prefix /opt/hpd .'
      }
    }
    stage('Finalizando') {
      steps {
        sh 'echo "fazendo finalizando"'
      }
    }
  }
}