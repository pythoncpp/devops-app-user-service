node {
    // get the code from SCM
    stage('SCM') {
      git 'https://github.com/pythoncpp/devops-app-user-service.git'
    }

    // building the docker image
    stage('Build Docker image') {
      sh 'docker image build . -t pythoncpp/devops-app-user-service'
    }

    // pushing the image to the docker hub
    stage('Docker hub push') {
      withCredentials([usernamePassword(credentialsId: 'docker_hub', passwordVariable: 'password', usernameVariable: 'username')]) {
          // login to the docker hub
          sh 'docker login -u $username -p $password'

          // push the image to docker hub
          sh 'docker image push pythoncpp/devops-app-user-service'

          // delete the image from local machine
          sh 'docker image rm pythoncpp/devops-app-user-service'
      }
    }

    // deploy the db to kubernetes cluster
    stage('Deploy the application to Kubernetes') {
      try {
        // use create command for first time deployment
        sh 'kubectl create -f deployment.yml'
      } catch(ex) {
        // use apply command for next time deployment(s)
        sh 'kubectl apply -f deployment.yml'
      }
    }

    // deploy the db service to kubernetes cluster
    stage('Deploy the service to Kubernetes') {
      try {
        // use create command for first time deployment
        sh 'kubectl create -f service.yml'
      } catch(ex) {
        // use apply command for next time deployment(s)
        sh 'kubectl apply -f service.yml'
      }
    }
}
