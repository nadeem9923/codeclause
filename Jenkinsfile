pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                // Checkout code from GitHub
                git 'https://github.com/nadeem9923/codeclause.git'
            }
        }
        stage('Deploy with Ansible') {
            environment {
                ANSIBLE_HOSTS = '/etc/ansible/hosts'
            }
            steps {
                // Run Ansible playbook
                script {
                    ansiblePlaybook(
                        playbook: '/home/ec2-user/copyfiles.yml',
                    )
                }
            }
        }
    }
    
    // Define triggers to listen for GitHub webhook events
    triggers {
        githubPush()
    }
}
