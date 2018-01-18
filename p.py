from database import Database as db

global myDb
myDb = db()
data,is_pos = myDb.grab_data(100)
file = open("test_data.txt","a")
for i in range(99,-1,-1):
	file.write(str(data[i]) + " : " +is_pos[i] + "\n")
file.close()