import jenkins

###
server = jenkins.Jenkins('http://jenkins:8080', username='admin', password='admin')

###
user = server.getwhoami()

###
version = server.get_version()

###
jobcount = server.jobs_count()

###
server.build_job('foo')





if str(app) == "rentalfront":
back = server.build_job('rentalfront')
print back
print "deploy rentalfront"
if str(app) == "farepaymnet":
print "Deploy farepaymnet"
return statement("Deploying {0}".format(app))
if __name__ == '__main__':
app.run(host='0.0.0.0',debug=True)
