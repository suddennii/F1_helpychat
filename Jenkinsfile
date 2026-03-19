pipeline {
    agent any

    environment {
        // 반드시 우리가 설치 확인한 'python3.11'로 설정
        PYTHON_CMD = 'python3.11'
    }
    stages {
        stage('Checkout') {
            steps {
                echo 'GitLab 저장소 가져오기'
                checkout scm
            }
        }

        stage('Python Version Check') {
            steps {
                // python 버전확인
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
                
                # 2. 가상환경 안에서는 'pip' 명령어를 바로 쓸 수 있습니다.
                pip install --upgrade pip
                
                if [ -f requirements.txt ]; then
                    pip install -r requirements.txt
                fi
                
                pip install pytest
                
                # 3. 테스트 실행
                pytest tests/ --junitxml=pytest-report.xml || true
                """
            }
        }
    }
    post {
        always {
            echo '테스트 리포트 및 스크린샷 보관'
            // 1. 테스트 결과 리포트 보관
            junit allowEmptyResults: true, testResults: 'pytest-report.xml'
            // 2. 실패 시 찍힌 스크린샷 파일을 젠킨스 화면에 표시하도록 보관
            archiveArtifacts artifacts: 'screenshots/*.png', allowEmptyArchive: true
        }
    }
}