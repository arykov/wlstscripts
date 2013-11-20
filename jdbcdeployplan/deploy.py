dbUserName='username'
dbPassword='password'
dbUrl='jdbc:oracle:thin:@localhost:1521:XE'
domainLocation='/opt/bea/bea1035/user_projects/domains/testdomain'
domainUrl='t3://localhost:7001'
domainUser='weblogic'
domainPassword='welcome1'
earLocation='./my.ear'
planLocation='./myPlan.xml'


encryptedDbPassword=encrypt(dbPassword, domainLocation)


plan=loadApplication(earLocation, planLocation)
plan.createVariable('userName',dbUserName);
plan.createVariable('password', encryptedDbPassword);
plan.createVariable('url', dbUrl);



moduleOverride = plan.createModuleOverride('my', 'ear')
moduleDescriptor = plan.getModuleDescriptor('jdbc/myDS-jdbc.xml', 'my.ear')

variableAssignment = moduleDescriptor.createVariableAssignment();
variableAssignment.xpath='/jdbc-data-source/jdbc-driver-params/password-encrypted'
variableAssignment.name='password'

variableAssignment = moduleDescriptor.createVariableAssignment();
variableAssignment.xpath='/jdbc-data-source/jdbc-driver-params/properties/property/value'
variableAssignment.name='userName'


variableAssignment = moduleDescriptor.createVariableAssignment();
variableAssignment.xpath='/jdbc-data-source/jdbc-driver-params/url'
variableAssignment.name='url'


plan.save()


connect(domainUser, domainPassword, domainUrl)
deploy('my', earLocation, planPath=planLocation)
dumpStack()
