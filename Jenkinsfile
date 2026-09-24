pipeline {
    agent any

    parameters {

        choice(
            name: 'DEPLOYMENT_ACTION',
            choices: ['DEPLOY', 'ROLLBACK'],
            description: 'Choose deployment action'
        )

        choice(
            name: 'ENVIRONMENT',
            choices: ['UAT', 'PRODUCTION'],
            description: 'Choose environment'
        )

        choice(
            name: 'CONFIRM_PROD',
            choices: ['YES', 'NO'],
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

                echo "Action: ${params.DEPLOYMENT_ACTION}"
                echo "Environment: ${params.ENVIRONMENT}"
                echo "Version: ${params.VERSION}"
                echo "Production confirmation: ${params.CONFIRM_PROD}"
                echo "Git commit: ${env.GIT_COMMIT}"

                script {

                    if (params.ENVIRONMENT == 'PRODUCTION' &&
                        params.CONFIRM_PROD != 'YES') {

                        error 'Production deployment requires CONFIRM_PROD = YES'
                    }

                    if (bat(
                        script: "git rev-parse v${params.VERSION}",
                        returnStatus: true
                    ) != 0) {

                        error "Version tag v${params.VERSION} does not exist"
                    }
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                bat "docker build -t retail-app:${params.VERSION} ."
            }
        }

        stage('Run Docker Container') {
            steps {

                bat """
                    docker rm -f retail-app-${params.VERSION} 2>NUL || exit /B 0
                """

                bat """
                    docker run -d ^
                    --name retail-app-${params.VERSION} ^
                    -p 8081:8081 ^
                    retail-app:${params.VERSION}
                """
            }
        }

        stage('Health Check') {
            steps {

                bat """
                    powershell -Command "Start-Sleep -Seconds 5"
                """

                bat """
                    powershell -Command ^
                    "$response = Invoke-WebRequest http://localhost:8081/health -UseBasicParsing; ^
                    if ($response.StatusCode -ne 200) { exit 1 }"
                """

                echo 'Application health check passed'
            }
        }

    }

    post {

        success {
            echo 'Pipeline completed successfully'
        }

        failure {
            echo 'Pipeline failed'
        }
    }
}