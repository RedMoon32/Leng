var url='http://127.0.0.1:5002/'
function checkURL(tabID, changeInfo, tab){
	if (tab.url.indexOf('translate') > -1) {
		chrome.contextMenus.create({
			id:'1',
			title: 'Look up: %s',
			contexts: ['selection'],
			onclick: sendText
		});
	}
}
function sendText(info){
	$.get(url+'add_word/1000/'+info.selectionText, function(data,status){
		result=data;
		if (result['result']!='OK'){
			alert('Sorry, some error happened(');
		}
		else{
			alert('Word '+info.selectionText+' was added to your dictionary!')
		}
	});
	//console.log(info.selectionText);
}
chrome.tabs.onUpdated.addListener(checkURL);

