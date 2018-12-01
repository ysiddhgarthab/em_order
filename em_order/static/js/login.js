function inputCheck(){
	var username = document.getElementById("username").value
	var password = document.getElementById("password").value
	if(username.length<6||username.length>20||password.length<6||password.length>20){
		alert("请输入正确的用户名和密码！")
		return false;
	}
	return true;
}