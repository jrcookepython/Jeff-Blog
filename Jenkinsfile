node{
	stage('Cleanup'){
		cleanWs()
	}
	stage('Git'){
		checkout scm
	}
	stage('Test'){
		echo 'Run unit tests'
	}
	stage('Cleanup'){
		cleanWs()
	}
}