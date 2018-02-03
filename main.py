from subprocess import Popen, PIPE

class SqlPlus():
    """Class is used in case if cx_Oracle module is unavailable. Meant to rise sqlplus process. """

    def __init__(self,con_str,sql_in):
        self.con_str = con_str
        self.sql_in = self.encode_decode(sql_in,"e")

    def connect(self,query):
        """establishes sqlplus session. It is done as one session per each call, this should be changed to hold connection"""
        self.sqlplus_session = Popen( ["sqlplus", "-l" ,"-s" , self.con_str ] , stdout=PIPE , stdin=PIPE )
        sep = self.encode_decode("set colsep '|'"+"\n","e")
        self.sqlplus_session.stdin.write(sep)
        self.sqlplus_session.stdin.write(query)
        return(self.sqlplus_session.communicate())

    def test_connection(self):
        test_query = self.encode_decode("select * from dual;","e")
        out  = self.connect(test_query)
        self.evaluate_result(out)

    def run(self):
        out  = self.connect(self.sql_in)
        self.result = self.evaluate_result(out)

    def evaluate_result(self,out):
        self.out = self.encode_decode(out[0],"d")
        if self.out.find("ORA") != -1 :
            print(self.out)
        else:
            return(self.out)


    def encode_decode(self,str_,mode_):
        if mode_ == "e":
            self.str_ = str_.encode('ascii')
            return self.str_
        else:
            self.str_ = str_.decode('ascii')
            return self.str_

    def split_result(self):
        #columns = [  for cols in self.result.strip().split('\n')[0].split() ]
        #for cols , rows , tt in self.result.strip().split('\n'):
        #    pass
        pass

    def execute(self):
        self.test_connection()
        self.run()
        #pars_result
        print("done")
