function inputCheck(){
	var eId = document.getElementById("eId").value.replace(/\s+/g,"");
	var username = document.getElementById("username").value.replace(/\s+/g,"");
	var password1 = document.getElementById("password1").value.replace(/\s+/g,"");
	var password2 = document.getElementById("password2").value.replace(/\s+/g,"");
	if(eId.length<6||eId.length>20){
		alert("请输入字符长度在6到20之间的员工号！")
		return false;
	}
	if(username==""){
		alert("用户名不能为空！")
		return false;
	}
	if(password1.length<6||password1.length>20||password2.length<6||password2.length>20){
		alert("请输入字符长度在6到20之间的员工号！")
		return false;
	}
	if(password1!=password2){
		alert("两次输入的密码不一致！")
		return false;
	}
	return true;
}