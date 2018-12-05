$(function(){
		var fType = $("#h_fType").val();
		var fSpicy = $("#h_fSpicy").val();
		$("#fType").find("option[value='"+fType+"']").attr("selected","selected")
		$("#fSpicy").find("option[value='"+fSpicy+"']").attr("selected","selected")
	})