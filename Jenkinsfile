pipeline {
    agent any
    
    parameters {
        choice(
            name: 'DEPLOYMENT_ACTION',
            choices: ['DEPLOY' , 'ROLLBACK'],
            description: 'Choose_deployment_action'
        )

        choice(
            name: 'ENVIRONMENT',
            choices: ['UAT', 'PRODUCTION'],
            description: 'Choose environment'
        )

        choice(
            name: 'CONFIRM_PROD',
            choices: ['YES' , 'NO'],
            description: 'Confirm production deployment'
        )

        string(
            name: 'VERSION',
            defaultValue: '',
            description: 'Application version to deploy'
        )
    }

    stages {
        stage('Validate Parameters') {
            steps {
                echo "Action : ${params.DEPLOYMENT_ACTION}"
                echo "Environment: ${params.ENVIRONMENT}"
                echo "Version: ${params.VERSION}"
                echo "Production confirmation: ${params.CONFIRM_PROD}"
                echo "Git commit: ${env.GIT_COMMIT}"

                script {
                    if(params.ENVIRONMENT == 'PRODUCTION' && params.CONFIRM_PROD != 'YES') {
                        error 'Production deployment requires CONFIRM_PROD = yes'
                    }

                    if(bat(script: "git rev-parse v${params.VERSION}", returnStatus: true) != 0) {
                        error "Version tag v${params.VERSION} does not exist"
                    }
                }

                stage('Build Docker Image') {
                    steps {
                        bat "docker build -t retail-app:${params.VERSION} ."
                    }
                }

                stage('Run Docker Container') {
                    steps {
                        bat "docker run -d --name retail-app-${params.VERSION} -p 8081:8080 retail-app:${params.VERSION}"
                    }
                }

            }
        }
    }
}