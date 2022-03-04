import os
from dotenv import load_dotenv
import sys
sys.path.insert(1, '..//Module//')
from DATABASE_HANDLER import Data_handler_my_sql
load_dotenv('..//..//.env')


host = os.getenv("DATABASE_IP")
database = os.getenv("DATABSE_NAME")
user = os.getenv("DATABASE_USR")
password = os.getenv("DATABASE_PASSWORD")

database_handler = Data_handler_my_sql(host, user, password, database)
temp = database_handler.get_tracked_usr()
for i in temp:
	if i[0]+'.html' not in os.listdir('/var/www/html/test/player/'):
		print(i[0],'Done')
		with open("/var/www/html/test/player/"+i[0]+".html","w", encoding="utf-8") as fich:
			fich.write("""
<html>
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<title>"""+i[0]+"""</title>
	<link rel="stylesheet" type="text/css" href="../../style/style_player.css">
	<link rel="icon" href="../../ouioui.png">
</head>
<body id="oui">
	<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/3.7.1/chart.min.js" crossorigin="anonymous" referrerpolicy="no-referrer"></script>
	<script type="text/javascript" src="../../scripts/player_scripts.js"></script>
	<div id="headers"></div>		
	<script>listInfo("headers",\""""+i[0]+"""\")</script>
	<div id="chart_container">
		<canvas id="myChart" width="40" height="40"></canvas>
		<script>fetch_tr(\""""+i[0]+"""\")</script>
	</div>
</body>
</html>
""")
