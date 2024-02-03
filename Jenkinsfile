pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Checkout the code from the repository
                script {
                    git 'https://github.com/Venkatamunnangi/unit_test_jenkins_assignment'
                }
            }
        }

        stage('Build and Test Python') {
            steps {
                script {
                    // Install dependencies and run pytest for the Python project
                    sh 'pip install -r requirements.txt'
                    sh 'pytest test_math_utils.py'
                }
            }
        }
    }

    post {
        always {

            // Publish Pytest test results for Python
            publishTestResults(testResults: 'pytest.xml', failIfNoResults: true)

            // Archive artifacts (e.g., jar files)
            archiveArtifacts artifacts: '**/target/*.jar', fingerprint: true
        }
    }
}
