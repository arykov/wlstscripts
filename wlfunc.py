from java.lang import *
from java.io import *
from java.util.concurrent import *
import jarray

#copy files from src directory to dest directory. create whatever needed along the way.
def startWebLogic(domainDir, timeOut=300):
  pb = ProcessBuilder(jarray.array(["cmd", "/c", "startWebLogic.cmd"], String))
  pb.directory(File(domainDir))
  pb.redirectErrorStream(Boolean.TRUE);
  p = pb.start()
  waitFor(p, timeOut)
  
  

def waitFor(process, timeOut):  
  es = Executors.newCachedThreadPool()
  pm = ProcessMonitor(process, timeOut)
  future = es.submit(pm)  
  try:
    for i in range(timeOut):      
      try:
        retVal = future.get(1, TimeUnit.SECONDS)
        if future.isDone():          
          try:
	    future.cancel(Boolean.TRUE)
	  except:
	    pass
	  try:
	    es.shutdownNow()
	  except:
	    pass
          return retVal
      except TimeoutException, exc:
        pass
    
    raise Exception("Process did not start within alloted timeframe.")
  except:    
    try:
      future.cancel(Boolean.TRUE)
    except:
      pass
    try:
      es.shutdownNow()
    except:
      pass
      
  

class ProcessMonitor(Callable):
  def __init__(self, process, timeOut):
    self.process = process
    self.timeOut = timeOut
  
  def call(self):
    try:
      isr = InputStreamReader(self.process.getInputStream())
      reader = BufferedReader(isr)
      str = reader.readLine()      
      while str != None :        
        print str
        if "<WebLogicServer> <BEA-000360> <Server started in RUNNING mode>" in str:
          try:
            reader.close()
          except:
            pass
          try:
            isr.close()
          except:
            pass
          return Boolean.TRUE
        str = reader.readLine()
    except Exception, e:
      raise  RuntimeException(e)


  
  
  
  
  
