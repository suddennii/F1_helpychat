pipeline {
    agent any

    environment {
        PYTHON_CMD = 'python3'
    }

    stages {

        stage('Checkout') {
            steps {
                echo 'GitHub 저장소 가져오기'
                checkout scm
            }
        }

        stage('Install Python') {
            steps {
                sh '''
                    echo "Python 설치 시작"
                    apt-get update
                    apt-get install -y python3 python3-pip python3-venv
                    python3 --version
                    pip3 --version
                '''
            }
        }

        stage('Python Version Check') {
            steps {
                sh "$PYTHON_CMD --version"
            }
        }

        stage('Install Dependencies & Test') {
            steps {
                echo '가상환경 생성 및 의존성 설치'
                sh """
                set -e

                # 1. 가상환경 생성 및 활성화
                $PYTHON_CMD -m venv venv
                . venv/bin/activate

                # 2. pip 업그레이드
                pip install --upgrade pip

                # 3. requirements.txt 설치
                if [ -f requirements.txt ]; then
                    pip install -r requirements.txt
                fi

                # 4. pytest 설치
                pip install pytest

                # 5. 테스트 실행 (JUnit XML 출력)
                pytest tests/ --junitxml=pytest-report.xml || true
                """
            }
        }
    }

    post {
        always {
            echo '테스트 리포트 및 스크린샷 보관'

            junit allowEmptyResults: true, testResults: 'pytest-report.xml'

            archiveArtifacts artifacts: 'screenshots/*.png', allowEmptyArchive: true
        }
    }
}