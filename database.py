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

	def insert_tweet_info(self,tweet_id,username,creation_date,text,is_text_positive,score,key):
		self.cursor.execute("INSERT INTO project.tweet_info VALUES('%s','%s','%s','%s','%s','%s','%s')" % (tweet_id,username,creation_date, text,is_text_positive,score,key))
		self.db.commit()
		
	def grab_data(self, size):
		data = []
		is_pos = []
		for i in range(size-1, -1, -1):
			self.cursor.execute("SELECT text,is_text_positive FROM project.tweet_info ORDER BY RAND() LIMIT 1")
			grabbed = self.cursor.fetchall()
			for row in grabbed :
				data.append( row[0])
				is_pos.append(row[1])
		for text in data:
			print(text)
