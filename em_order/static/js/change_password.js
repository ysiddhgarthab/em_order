function change_password_check(){
	var cur_pwd  = document.getElementById("cur_pwd").value.replace(/\s+/g,"");
	var new_pwd1 = document.getElementById("new_pwd1").value.replace(/\s+/g,"");
	var new_pwd2 = document.getElementById("new_pwd2").value.replace(/\s+/g,"");

	if(cur_pwd.length<6 || cur_pwd.length>20){
		alert("请输入正确的原密码！")
		return false;
	}
	if(new_pwd1.length<6 || new_pwd1.length>20 || new_pwd2.length<6 || new_pwd2.length>20){
		alert("请输入字符长度在6到20之间的新密码！")
		return false
	}
	if(new_pwd1!=new_pwd2){
		alert("两次输入的密码不一致！")
		return false;
	}
}