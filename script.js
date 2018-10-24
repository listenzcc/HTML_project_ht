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
    var frames = document.getElementsByName("iframe");
    var total_height = 0;
    for(var j=0;j<frames.length;j++)
    {
        frame = frames[j]
        var outHeight = frame.offsetHeight;
        var inHeight = frame.contentWindow.document.body.scrollHeight;
        if (outHeight < inHeight)
	{
	    frame.style.height = (inHeight + 10) + "px";
        }
        total_height += (inHeight+10);
    }
    var left_panel = document.getElementById("left_panel");
    left_panel.style.height = total_height + "px";
}
