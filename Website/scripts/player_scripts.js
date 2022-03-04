function listInfo(playerContainerElementId,player){
	const playerContainerElement =  document.getElementById(playerContainerElementId);
	
	
	fetch('http://ouiouibaguette.duckdns.org:5000//oui/'+player)
		.then(response => response.json())
    	.then(Infos => {
    		playerContainerElement.appendChild(playerinfo(Infos));
    	})
}

function playerinfo(info){

	const infoPlayerName = document.createElement('a');
	infoPlayerName.setAttribute("id","pseudo");
	infoPlayerName.setAttribute('href',"../index.html");
	infoPlayerName.innerText = info[0].pseudo


	const anchorElementImg_lvl = document.createElement('img')
	anchorElementImg_lvl.setAttribute("alt","Image");
	anchorElementImg_lvl.setAttribute('src',"../image/experience_level.png")
	anchorElementImg_lvl.setAttribute("height",25);
	anchorElementImg_lvl.setAttribute("width",25);

	const infoPlayerLevel = document.createElement('li');
	infoPlayerLevel.setAttribute("class","info");
	infoPlayerLevel.setAttribute("id","level");
	infoPlayerLevel.innerText = info[1].level;
	infoPlayerLevel.appendChild(anchorElementImg_lvl);


	const anchorElementImg = document.createElement('img')
	anchorElementImg.setAttribute("alt","Image");
	anchorElementImg.setAttribute('src',"../image/trophie.png")
	anchorElementImg.setAttribute("height",25);
	anchorElementImg.setAttribute("width",25);

	const infoPlayerTrophies = document.createElement('li');
	infoPlayerTrophies.setAttribute("class","info");
	infoPlayerTrophies.setAttribute("id","trophie");
	infoPlayerTrophies.innerText = info[2].trophie;
	infoPlayerTrophies.appendChild(anchorElementImg);


	const infoPlayerWr = document.createElement('li');
	infoPlayerWr.setAttribute("class","info");
	infoPlayerWr.setAttribute("id","wr");
	infoPlayerWr.innerText = info[3].wr+'%';


	const Info_List = document.createElement('ul');
	Info_List.setAttribute("id","Player_info_list");
	Info_List.appendChild(infoPlayerLevel);
	Info_List.appendChild(infoPlayerTrophies);
	Info_List.appendChild(infoPlayerWr);

	const infoPlayer = document.createElement('div');
	infoPlayer.appendChild(infoPlayerName);
	infoPlayer.appendChild(Info_List);

	return infoPlayer
}

function fetch_tr(player){
	var x=[]
	var y=[]
	var w=[]

	var median = function(array) {
		array = array.sort();
		if (array.length % 2 === 0) { // array with even number elements
		   return (array[array.length/2] + array[(array.length / 2) - 1]) / 2;
		   }
		else {
		   return array[(array.length - 1) / 2]; // array with odd number elements
		}}


	fetch('http://ouiouibaguette.duckdns.org:5000//ouitr/'+player)
		.then(response => response.json())
    	.then(battles => {
    		for(let battle of battles){
    			x.push(battle.time)
    			y.push(Number(battle.tr))
    			w.push(Number(battle.tr))
    		}
    		
			
    		chart_creation(x,y);
    		Chart_info(Math.min.apply(null ,y),
    			Math.max.apply(null ,y),
    			median(w));
    		
    		
    	})
}

function Chart_info(min,max,median){
	const ctx = document.getElementById('oui');


	const anchorElementImg = document.createElement('img');
	anchorElementImg.setAttribute("alt","Image");
	anchorElementImg.setAttribute('src',"../image/trophie.png")
	anchorElementImg.setAttribute("height",25);
	anchorElementImg.setAttribute("width",25);
	const anchorElementImg_1 = document.createElement('img');
	anchorElementImg_1.setAttribute("alt","Image");
	anchorElementImg_1.setAttribute('src',"../image/trophie.png")
	anchorElementImg_1.setAttribute("height",25);
	anchorElementImg_1.setAttribute("width",25);
	const anchorElementImg_2 = document.createElement('img');
	anchorElementImg_2.setAttribute("alt","Image");
	anchorElementImg_2.setAttribute('src',"../image/trophie.png")
	anchorElementImg_2.setAttribute("height",25);
	anchorElementImg_2.setAttribute("width",25);
	
	const infoChartMin = document.createElement('li');
	infoChartMin.setAttribute("class","info_chart");
	infoChartMin.setAttribute("id","max_chart");
	infoChartMin.innerText = min;
	infoChartMin.appendChild(anchorElementImg_1);

	const infoChartMed = document.createElement('li');
	infoChartMed.setAttribute("class","info_chart");
	infoChartMed.setAttribute("id","max_chart");
	infoChartMed.innerText = median;
	infoChartMed.appendChild(anchorElementImg_2);

	const infoChartMax = document.createElement('li');
	infoChartMax.setAttribute("class","info_chart");
	infoChartMax.setAttribute("id","min_chart");
	infoChartMax.innerText = max;
	infoChartMax.appendChild(anchorElementImg);




	const Info_List = document.createElement('ul');
	Info_List.setAttribute("id","Chart_info_list");
	Info_List.appendChild(infoChartMin);
	Info_List.appendChild(infoChartMed);
	Info_List.appendChild(infoChartMax);
	ctx.appendChild(Info_List);

	

}


function chart_creation(x,y){
const ctx = document.getElementById('myChart').getContext('2d');
let myChart = new Chart(ctx, {
	type: "line",
	data: {
	        labels: x,
	        datasets: [{
	            label: '',
	            data: y,
	            fill: true,
	            borderColor: '#30BCED',
	            backgroundColor:'#30BCED',
	           hoverBorderWitdth:10,
	           tension: 0.25,
	           pointRadius:0,
	        }]
	    },
	options: {
		plugins:{   
						title:{
							display:true,
							color : '#FFFAFF',
							text: 'Trophie Chart',
							font: {
                        size: 20
                    },
						},
            legend: {
               display: false
                     },
                  },
	        transitions: {
		      show: {
		        animations: {
		          x: {
		            from: 0
		          },
		          y: {
		            from: 0
		          }
		        }
		      },
		      hide: {
		        animations: {
		          x: {
		            to: 0
		          },
		          y: {
		            to: 0
		          }
		        }
		      }
		    },
		    scales: {
		        x: {
		            grid: {
		                display:false
		            },
		            ticks: {
          					display:false
        				}
		        },
		        y: {
		            grid: {
		                display:false
		            },
		            ticks: {
          					color : '#FFFAFF',
          					font: {
                        size: 16
                    },
        				}
		        }
		    }
			
	    }
	
	 }   
);
}

