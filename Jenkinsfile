pipeline {
    agent any

    stages {
        stage('Get code') {
            steps {
                git branch: 'homework_12', url: 'https://github.com/Eduard-z/otus-course.git'

            }
        }
        stage('Prepare env') {
            steps {
                sh '''python3 -m venv test-env
                . test-env/bin/activate
                pip install -Ur requirements.txt
                mkdir -p selenium_tests/logs'''
            }
        }
        stage('Test') {
            steps {
                sh '''. test-env/bin/activate
                pytest -n=${number_of_threads} --environment=${environment} --url=${opencart_URL} --browser=${browser} --browser_version=${browser_version} selenium_tests/'''

            }
        }
    }

    post {
        always {
            allure includeProperties: false, jdk: '', results: [[path: 'allure-results']]
        }
    }
}
