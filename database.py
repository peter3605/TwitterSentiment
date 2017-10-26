import pymysql

#class that handles all interactions with database
#database name: project
#tables: tweet_info(tweet_id, user_id, creation_date, text, is_text_positive, sentiment_score)
class Database():
	
	#connect to database and create cursosr object to execute queries
	def __init__(self):
		hostname = "localhost"
		username = "root"
		password = "xanthosis"
		dbname = "project"
		self.db = pymysql.connect(hostname,  
							 username,       
							 password,     
							 dbname, use_unicode=True, charset="utf8")
		 
		self.cursor = self.db.cursor()

	def insert_tweet_info(self,tweet_id,username,creation_date,text,is_text_positive,score):
		self.cursor.execute("INSERT INTO project.tweet_info VALUES('%s','%s','%s','%s','%s','%s')" % (tweet_id,username,creation_date, text,is_text_positive,score))
		self.db.commit()
