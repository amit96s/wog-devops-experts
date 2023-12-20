pipeline {
    agent any
    
    stages {
        stage('Clone Repository') {
            steps {
                bat 'if exist wog-devops-experts rmdir /s /q wog-devops-experts'
                // Clone the GitHub repository
                bat 'git clone https://github.com/amit96s/wog-devops-experts.git'

                // Move into the cloned repository directory
                dir('wog-devops-experts') {
                    // Run docker build within the repository directory
                    bat 'docker build -t wog_amit_shemesh .'
                    bat 'docker-compose up -d'
                }
            }
        }

        stage('Run Tests and Tag') {
            steps {
                dir('wog-devops-experts') {
                    // Run e2e tests and capture the exit code
                    script {
                        def e2eExitCode = bat(script: 'python e2e.py', returnStatus: true)
            
                        // Check the exit code and proceed accordingly
                        if (e2eExitCode == 0) {
                            echo 'good'
                            bat 'docker login -u *** -p ***'
                            bat 'docker tag wog_amit_shemesh:1.0 amit1shemesh/wog_amit_shemesh:1.0'
                            bat 'docker push amit1shemesh/wog_amit_shemesh:1.0'
                            // Tests passed, tag and push the image
                        } else {
                            // Tests failed, abort the pipeline
                            echo 'bad'
                            error('e2e tests failed. Pipeline aborted.')
                        }
                    }
        }   }   }
    }
}
