module.exports = {
  apps: [{
    name: 'Fadiser',
    script: './index.js'
  }],
  deploy: {
    production: {
      user: 'ubuntu',
      host:  'ec2-18-221-107-128.us-east-2.compute.amazonaws.com'
      key: '~/.ssh/fadiser-1.pem',
      ref: 'origin/master',
      repo: 'git@github.tamu.edu:mailvijayasingh/Fadiser.git',
      path: '/home/ubuntu/source_code/',
      'post-deploy': 'npm install && pm2 startOrRestart ecosystem.config.js'
    }
  }
}
