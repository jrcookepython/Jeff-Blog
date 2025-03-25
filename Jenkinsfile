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
	stage('Artifact'){
		archiveArtifacts artifacts: '**/*.*', followSymlinks: false
	}
	stage('Cleanup'){
		cleanWs()
	}
}