function listPosts(playerContainerElementId){
	const playerContainerElement =  document.getElementById(playerContainerElementId);
	
	fetch('http://ouiouibaguette.duckdns.org:5000//tracked')
		.then(response => response.json())
    	.then(players => {
    		for(let player of players){
    		playerContainerElement.appendChild(playerElement(player));
    	}
    	})	
}

function playerElement(player){
	const anchorElementText = document.createElement('a');
	anchorElementText.setAttribute('id','pseudo');
	var child = "./player/" + player.pseudo + ".html";
	anchorElementText.setAttribute('href',child);
	anchorElementText.innerText = player.pseudo;

	const anchorElementImg = document.createElement('img')
	anchorElementImg.setAttribute("alt","Image");
	anchorElementImg.setAttribute('src',"https://www.wikiclashroyale.fr/wp-content/uploads/2016/03/troph%C3%A9es.png")
	anchorElementImg.setAttribute("height",25);
	anchorElementImg.setAttribute("width",25);

	const anchorElementSpan_tr = document.createElement('span')
	anchorElementSpan_tr.setAttribute("id","Trophie");
	anchorElementSpan_tr.innerText = player.trophie

	const anchorElementSpan_img = document.createElement('span')
	anchorElementSpan_img.setAttribute("class","Image");
	anchorElementSpan_img.appendChild(anchorElementSpan_tr);
	anchorElementSpan_img.appendChild(anchorElementImg);


	const playerTittleElement = document.createElement('li');
	playerTittleElement.setAttribute("id","Player");
	playerTittleElement.appendChild(anchorElementText);
	playerTittleElement.appendChild(anchorElementSpan_img);

	return playerTittleElement
}
