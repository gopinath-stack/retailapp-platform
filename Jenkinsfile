pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                echo 'Building retailapp_platform'

                bat '''
                    cd
                    git --version
                '''
            }
        }
    }
}