def newEnv(name, members, dictionaries):
  return repository.create(factory.configurationItem('Environments/'+name,
    'udm.Environment', {'members':members,'dictionaries':dictionaries}))

oracleHost = repository.create(
    factory.configurationItem('Infrastructure/ora-10g-express-unix', 'overthere.SshHost',
        {'address':'ora-10g-express-unix','os':'UNIX', 'connectionType':'SFTP', 'username':'orauser', 'password':'0raus3r '}))

oracleClient = repository.create(
    factory.configurationItem(oracleHost.id+'/oracle-db', 'db.OracleClient',
        {'host':oracleHost.id,'oraHome':'/usr/lib/oracle/xe/app/oracle/product/10.2.0/server','sid':'xe','username':'scott','password':'tiger'}))



dmgrHost = repository.create(
    factory.configurationItem('Infrastructure/host-was-70', 'overthere.SshHost',
        {'address':'was-70','os':'UNIX', 'connectionType':'SFTP', 'username':'root', 'password':'centos'}))

dmgr = factory.configurationItem(dmgrHost.id + '/was-70Cell01', 'was.DeploymentManager',
    {'host':dmgrHost.id, 'username':'wsadmin', 'password':'wsadmin', 'wasHome':'/opt/ws/7.0/profiles/Dmgr01'})

print 'discover %s'% (dmgr.id)

cell = deployit.discover(dmgr)
repository.create(cell)



newEnv('was-existing-server',[dmgrHost.id,oracleHost.id, oracleClient.id,'Infrastructure/host-was-70/was-70Cell01/was-70Node01/existing-server'], [])
newEnv('was-existing-cluster',[dmgrHost.id,oracleHost.id,oracleClient.id,'Infrastructure/host-was-70/was-70Cell01/was-70Node01/existing-cluster-server-1','Infrastructure/host-was-70/was-70Cell01/was-70Node01/existing-cluster-server-2','Infrastructure/host-was-70/was-70Cell01/existing-cluster'], [])





  