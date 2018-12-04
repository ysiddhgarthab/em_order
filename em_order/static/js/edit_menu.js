function inputCheck(){
	var selectPage1 = document.getElementById("selectPage1").value.replace(/\s+/g,"");
	var selectPage2 = document.getElementById("selectPage2").value.replace(/\s+/g,"");
	var selectPage3 = document.getElementById("selectPage3").value.replace(/\s+/g,"");
	if(selectPage1==""){
		alert("早餐不能为空！")
		return false;
	}
	if(selectPage2==""){
		alert("午餐不能为空！")
		return false;
	}
	if(selectPage3==""){
		alert("晚餐不能为空！")
		return false;
	}
	return true;
}