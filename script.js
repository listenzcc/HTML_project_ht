//iframe自适应高度的函数
var oTime = null;
function resize()
{
    if (oTime)
    {
        clearTimeout(oTime);
    }
    oTime = setTimeout(reset, 200);
}
//iframe自适应高度的函数
function reset()
{
	console.log('resetting');
    var frames = document.getElementsByName("iframe");
    var total_height = 350;
    for(var j=0;j<frames.length;j++)
    {
        frame = frames[j]
        var outHeight = frame.offsetHeight;
        var inHeight = frame.contentWindow.document.body.scrollHeight;
		console.log(outHeight*100000000+inHeight);
        if (outHeight != inHeight)
		{
			frame.style.height = (inHeight+10) + "px";
        }
        total_height += (inHeight+18);
    }
    var left_panel = document.getElementById("left_panel");
    left_panel.style.height = total_height + "px";
}
//Keep nav on screen
window.onscroll = function()
{
    var oDiv=document.getElementById("nav");
	var s = document.body.scrollTop||document.documentElement.scrollTop;
	oDiv.style.top=(s+800)+"px";
}
window.onload = function()
{
    var oDiv=document.getElementById("nav");
	var s = document.body.scrollTop||document.documentElement.scrollTop;
	oDiv.style.top=(s+800)+"px";
}
//onClick of readmore
function foo1(obj){
	var article = obj.id.slice(4);
	console.log(article);
	var frame = document.getElementById(article);
	console.log(frame.src);
	if (obj.textContent.indexOf("more") > 0)
	{
		frame.src = "htmls/"+article+"_context.html";
		obj.textContent = "Less of this";
	}else{
		frame.style.height = 0;
		frame.src = "htmls/"+article+"_title.html";
		obj.textContent = "Read more of this";
	}
}
