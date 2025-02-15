node{
	stage('Cleanup'){
		cleanWs()
	}
	stage('Git'){
		checkout scm
	}
	stage('Build'){
		steps {
			try{
				sh 'python -m py_compile main.py'
			} catch{Exception e){
				echo e.toString()
				archiveArtifacts artifacts: '**/*.*', followSymlinks: false
				cleanWs()
			}
		}
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