$(function(){
		var flagValue = $("#flagValue").val();
		$("#flag").find("option[value='"+flagValue+"']").attr("selected","selected");
	});

function inputCheck(){
	var eId = document.getElementById("eId").value.replace(/\s+/g,"");
	var eName = document.getElementById("eName").value.replace(/\s+/g,"");
	var password = document.getElementById("password").value.replace(/\s+/g,"");
	if(eId.length<6||eId.length>20){
		alert("请输入字符长度在6到20之间的员工号！")
		return false;
	}
	if(eName==""){
		alert("用户名不能为空！")
		return false;
	}
	if(password!=""){
		if(password.length<6||password.length>20){
			alert("请输入字符长度在6到20之间的密码！")
			return false;
		}
	}
	return true;
}