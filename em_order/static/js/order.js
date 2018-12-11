//点击td的时候选中里面的checkbox
	$('td').click(function(){
		$(this).find(':checkbox').click();
	});
	//因为点击checkbox的同时由于时间冒泡也会触发td的click事件，所以要阻止checkbox的事件冒泡
	$("input[type='checkbox']").click(function(e){  
        e.stopPropagation();
}); 