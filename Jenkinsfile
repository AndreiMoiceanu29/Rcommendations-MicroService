pipeline{
    agent any
    stages{
        stage('Build'){
        steps{
            sh 'echo "Building..."'
        }
        }
        stage('Requirements'){
        steps{
            script{
            sh 'pip install -r requirements.txt'
            }
        }
        }
        stage("Static Code Analysis"){
            steps{
                    script {
                    sh 'find . -name \\*.py | xargs pylint -f parseable | tee pylint.log'
                    recordIssues(
                        tool: pyLint(pattern: 'pylint.log'),
                        unstableTotalHigh: 100,
                    )
                }
            }
        }
        stage('Test'){
        steps{
            sh 'echo "Testing..."'
        }
        }
        stage('Deploy'){
        steps{
            sh 'echo "Deploying..."'
        }
        }
    }
}