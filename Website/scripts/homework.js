function listWorks(containerId){
	const container =  document.getElementById(containerId);
	var oui = false
	fetch('http://ouiouibaguette.duckdns.org:5000//hw')
		.then(response => response.json())
    	.then(works => {
    		for(let i = 1; i < works.length; i++){
    		if (works[i].date.length == 3){
    			oui = true
    		}
    		container.appendChild(WorkElement(works[i],oui));
    	}
    	})	
}

function WorkElement(work,oui){



	const WorkNameElement = document.createElement('span');
	WorkNameElement.setAttribute('id',"WorkToDo");
	WorkNameElement.innerText= work.title;

	const WorkdateElement = document.createElement('span');
	WorkdateElement.setAttribute('id',"date");
	if (oui) {
		WorkdateElement.innerText= work.date[0]+" "+work.date[1]+" "+work.date[2];
	} else {
		WorkdateElement.innerText= work.date[0];
	}
	

	const WorklinkElement = document.createElement('a');
	WorklinkElement.setAttribute('id',"link");
	WorklinkElement.setAttribute('href',work.link);
	WorklinkElement.appendChild(WorkNameElement)
	WorklinkElement.appendChild(WorkdateElement)

	const WorkContainerElement = document.createElement('div');
	WorkContainerElement.setAttribute('id',"WorkContainer");
	WorkContainerElement.appendChild(WorklinkElement)
	

	


	const playerTittleElement = document.createElement('li');
	playerTittleElement.setAttribute("id","Work");
	playerTittleElement.appendChild(WorkContainerElement);

	return playerTittleElement
}