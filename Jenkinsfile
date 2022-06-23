pipeline {
    agent {label 'macos'}

    stages {
        stage('Hello') {
            steps {
                echo 'Hello World'
                sh 'ls -l /Users/tian/Downloads'
                sh 'cat /Users/tian/Downloads/hello.txt'
            }
        }
    }
}
