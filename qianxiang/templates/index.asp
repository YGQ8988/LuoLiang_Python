
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
{% load staticfiles %}
<html xmlns="http://www.w3.org/1999/xhtml">

<head>
<meta http-equiv="Content-Type" content="text/html; charset=gb2312" />
<title>上海芊详建筑工程有限公司</title>
<link href="{% static 'qx/Scripts/web.css' %}" rel="stylesheet" type="text/css" />
</head>

<body topmargin="0" leftmargin="0">
<table width="1004" border="0" cellspacing="0" cellpadding="0" align="center">
  <tr>
    <td colspan="3"><img src="{% static 'qx/images/top.jpg' %}" width="1004" height="67" /></td>
  </tr>
  <tr>
    <td width="30">&nbsp;</td>
    <td width="943"><img src="{% static 'qx/images/banner.gif' %}" width="943" height="295" alt=""></td>
    <td width="31">&nbsp;</td>
  </tr>
  <tr>
    <td colspan="3" background="{% static 'qx/images/67_05.jpg' %}" height="71" valign="top"><table width="100%" height="65" border="0" cellpadding="0" cellspacing="0">
      <tr>
        <td width="30">&nbsp;</td>
        <td width="347" class="black12a"><div align="center" style="color:#FFFFFF">现在时刻：<script language=JavaScript>
function Year_Month(){ 
    var now = new Date();
    var yy = now.getYear(); 
    var mm = now.getMonth(); 
	var mmm=new Array();
	mmm[0]="1";
	mmm[1]="2 ";
	mmm[2]="3";
	mmm[3]="4";
	mmm[4]="5";
	mmm[5]="6";
	mmm[6]="7";
	mmm[7]="8";
	mmm[8]="9";
	mmm[9]="10";
	mmm[10]="11";
	mmm[11]="12";
	mm=mmm[mm];
    return(mm ); }
function thisYear(){ 
    var now = new Date(); 
    var yy = now.getYear(); 
    return(yy ); }
 function Date_of_Today(){ 
    var now = new Date(); 
    return(now.getDate() ); }
 function CurentTime(){ 
    var now = new Date(); 
    var hh = now.getHours(); 
    var mm = now.getMinutes(); 
    var ss = now.getTime() % 60000; 
    ss = (ss - (ss % 1000)) / 1000; 
    var clock = hh+':'; 
    if (mm < 10) clock += '0'; 
    clock += mm+':'; 
    if (ss < 10) clock += '0'; 
    clock += ss; 
    return(clock); } 
function refreshCalendarClock(){ 
document.all.calendarClock1.innerHTML = Year_Month(); 
document.all.calendarClock2.innerHTML = Date_of_Today(); 
document.all.calendarClock3.innerHTML =thisYear(); 
document.all.calendarClock4.innerHTML = CurentTime(); }
document.write('<font id="calendarClock3" > </font>年&nbsp;');
document.write('<font id="calendarClock1" > </font>月&nbsp;');
document.write('<font id="calendarClock2" > </font>日,&nbsp;&nbsp;');
document.write('<font id="calendarClock4" > </font>');
setInterval('refreshCalendarClock()',1000);
    </script></div></td>
        <td onmouseover="this.className='nore'" onmouseout="this.className='nore1'"><div align="center"><a href="{% url 'about' %}" class="dh">关于我们</a></div></td>
        <td onmouseover="this.className='nore'" onmouseout="this.className='nore1'"><div align="center"><a href="{% url 'product' %}" class="dh">工程图集</a></div></td>
        <td onmouseover="this.className='nore'" onmouseout="this.className='nore1'"><div align="center"><a href="{% url 'anli' %}" class="dh">成功案例</a></div></td>
        <td onmouseover="this.className='nore'" onmouseout="this.className='nore1'"><div align="center"><a href="" class="dh">竹文化</a></div></td>
        <td onmouseover="this.className='nore'" onmouseout="this.className='nore1'"><div align="center"><a href="{% url 'acontact' %}" class="dh">联系我们</a></div></td>
        <td width="31">&nbsp;</td>
      </tr>
    </table></td>
  </tr>
</table>


<table width="1004" border="0" cellspacing="0" cellpadding="0" align="center">
  <tr>
    <td width="30">&nbsp;</td>
    <td valign="top" background="{% static 'qx/images/67_16.jpg' %}"><table width="100%" border="0" cellspacing="0" cellpadding="0">
      <tr>
        <td background="{% static 'qx/images/67_07.jpg' %}" height="60"><table width="100%" height="44" border="0" cellpadding="0" cellspacing="0">
          <tr>
            <td height="20">&nbsp;</td>
          </tr>
          <tr>
            <td style="padding-left:60px; font-weight:bold;">关于我们</td>
          </tr>
        </table></td>
      </tr>
      <tr>
        <td background="{% static 'qx/images/67_10.jpg' %}" height="144" valign="top" class="black12a"><table width="100%" border="0" cellspacing="0" cellpadding="0">
          <tr>
            <td width="7%">&nbsp;</td>
            <td width="88%"  style="line-height:38px; font-size:14px;" valign="top"><p>&nbsp;&nbsp;&nbsp;  上海芊详建筑工程有限公司是一家专业经营竹艺工程公司从事竹木类工艺品数年,经验丰富、技术先进、别具一格,尤对宾馆、酒店、休闲度假及旅游景点生态园林的竹房、竹门楼、竹亭、竹廊、竹家具等设计制作一流,自有生产加工基地,供应各类竹窗帘、竹家具、庭院用品等。经营宗旨：诚实、信用。选择我们就是成功。让我们携手共创美好明天。<br />
&nbsp;&nbsp;&nbsp; 自公司成立以来经过十余年健康发展,目前已拥有一大批经验丰富的专业设计人员,经验丰富施工的队伍及专业的项目管理人员,正是以丰富施工经验,良好的信誉,优质的服务,良好的质量和合理价格受到了广大客户的好评,在行业中取得了较高的成绩。本公司所用竹材均选择优质的竹乡毛竹,经过严格的防蛀防酶处理,对每一道工序都一丝不苟,绿然竹艺让您以低廉成本建造出优质的竹建筑产品,为您打造出绿色自然、生态环保的竹建筑产品,真正为客户的财富创造出更多的价值——这就是绿然竹艺的目标。</p>
              </td>
            <td width="5%">&nbsp;</td>
          </tr>
        </table></td>
      </tr>
      <tr>
        <td><img src="{% static 'qx/images/67_14.jpg' %}" width="669" height="15" alt=""></td>
      </tr>
      <tr>
        <td><img src="{% static 'qx/images/67_16.jpg' %}" width="669" height="14" alt=""></td>
      </tr>
      <tr>
        <td background="{% static 'qx/images/67_18.jpg' %}" height="37"><table width="100%" border="0" cellspacing="0" cellpadding="0">
  <tr>
    <td width="87%" style="padding-left:60px;"><span style="font-weight: bold">产品展示</span>&nbsp; <span style="font-family: Arial, Helvetica, sans-serif; color: #999999">product</span></td>
    <td width="13%">&nbsp;</td>
  </tr>
</table>
</td>
      </tr>
      <tr>
        <td background="{% static 'qx/images/67_20.jpg' %}" height="149"><table width="100%" border="0" cellspacing="0" cellpadding="0">
          <tr>
            <td width="6%" height="147">&nbsp;</td>
            <td width="90%"><div id="demo" style="OVERFLOW: hidden; WIDTH:600px;">
      <table width="95%" align="center">
        <tr>
          <td id="demo1"><table width="100%">
              <tr>
                <td width="130"><img src="{% static 'qx/images/1.jpg' %}"  height="120" hspace="6" border="0" onmouseover='this.style.border="1px solid #e31a13"' onmouseout='this.style.border="1px solid #CCC"' style="border:1px solid #CCC;" /></td>
                <td width="130"><img src="{% static 'qx/images/2.jpg' %}"  height="120" hspace="6" border="0" onmouseover='this.style.border="1px solid #e31a13"' onmouseout='this.style.border="1px solid #CCC"' style="border:1px solid #CCC;" /></td>
                <td width="130"><img src="{% static 'qx/images/3.jpg' %}"  height="120" hspace="6" border="0" onmouseover='this.style.border="1px solid #e31a13"' onmouseout='this.style.border="1px solid #CCC"' style="border:1px solid #CCC;" /></td>
                <td width="130"><img src="{% static 'qx/images/4.jpg' %}"  height="120" hspace="6" border="0" onmouseover='this.style.border="1px solid #e31a13"' onmouseout='this.style.border="1px solid #CCC"' style="border:1px solid #CCC;" /></td>
                <td width="130"><img src="{% static 'qx/images/5.jpg' %}"  height="120" hspace="6" border="0" onmouseover='this.style.border="1px solid #e31a13"' onmouseout='this.style.border="1px solid #CCC"' style="border:1px solid #CCC;" /></td>
                <td width="130"><img src="{% static 'qx/images/6.jpg' %}"  height="120" hspace="6" border="0" onmouseover='this.style.border="1px solid #e31a13"' onmouseout='this.style.border="1px solid #CCC"' style="border:1px solid #CCC;" /></td>
                <td width="130"><img src="{% static 'qx/images/7.jpg' %}"  height="120" hspace="6" border="0" onmouseover='this.style.border="1px solid #e31a13"' onmouseout='this.style.border="1px solid #CCC"' style="border:1px solid #CCC;" /></td>
                <td width="130"><img src="{% static 'qx/images/8.jpg' %}"  height="120" hspace="6" border="0" onmouseover='this.style.border="1px solid #e31a13"' onmouseout='this.style.border="1px solid #CCC"' style="border:1px solid #CCC;" /></td>
              </tr>
          </table></td>
          <td id="demo2" valign="top"></td>
        </tr>
      </table>
    </div><script language="JavaScript" type="text/javascript">
		var speed=25
		demo2.innerHTML=demo1.innerHTML
		function Marquee(){
			if(demo2.offsetWidth-demo.scrollLeft<=0)
				demo.scrollLeft-=demo1.offsetWidth
			else{
				demo.scrollLeft++
			}
		}

var MyMar=setInterval(Marquee,speed)
		demo.onmouseover=function() {clearInterval(MyMar)}
		demo.onmouseout=function() {MyMar=setInterval(Marquee,speed)}
	      </script></td>
            <td width="4%">&nbsp;</td>
          </tr>
        </table></td>
      </tr>
      <tr>
        <td><img src="{% static 'qx/images/67_24.jpg' %}" width="669" height="16" alt=""></td>
      </tr>
    </table></td>
    <td width="274" valign="top" background="{% static 'qx/images/67_17.jpg' %}"><table width="274" border="0" cellspacing="0" cellpadding="0">
  <tr>
    <td background="{% static 'qx/images/67_08.jpg' %}" height="60"><table width="100%" height="37" border="0" cellpadding="0" cellspacing="0">
      <tr>
        <td height="13">&nbsp;</td>
      </tr>
      <tr>
        <td style="padding-left:20px;"><span style="font-size:14px; font-weight:bold; color:#FFFFFF">图片展示</span></td>
      </tr>
    </table></td>
  </tr>
  <tr>
    <td background="{% static 'qx/images/67_11.jpg' %}" height="144" style="padding-left:10px;"><script language="JavaScript" type="text/javascript">
	var tpics = '';
	var tlinks = '';
	var ttexts = '';
</script>
<!-- BEGIN imgnews -->
<script language="JavaScript" type="text/javascript">
	tpics = './pro/1.jpg|./pro/2.jpg|./pro/3.jpg|./pro/4.jpg|./pro/5.jpg|';
	ttexts = '1111|2222|3333|4444|5555';
</script>
<!-- END imgnews -->
<script language="JavaScript" type="text/javascript">

	var focus_width=224;  //图片的宽度
	var focus_height=170; //图片的高度
	var text_height=0;   //标题栏的宽度
	var swf_height = focus_height+text_height;
	var pics = tpics.substr(0, tpics.length - 1);
	var links = tlinks.substr(0, tlinks.length - 1);
	var texts = ttexts.substr(0, ttexts.length - 1);

	document.write('<object classid="clsid:d27cdb6e-ae6d-11cf-96b8-444553540000" codebase=""http://fpdownload.macromedia.com/pub/shockwave/cabs/flash/swflash.cab#version=6,0,0,0" width="'+ focus_width +'" height="'+ swf_height +'">');

	document.write('<param name="allowScriptAccess" value="sameDomain"><param name="movie" value="flash/play.swf"><param name="quality" value="high"><param name="bgcolor" value="#F0F0F0">');

	document.write('<param name="menu" value="false"><param name=wmode value="opaque">');

	document.write('<param name="FlashVars" value="pics='+pics+'&links='+links+'&texts='+texts+'&borderwidth='+focus_width+'&borderheight='+focus_height+'&textheight='+text_height+'">');

	document.write('<embed src="" wmode="opaque" FlashVars="pics='+pics+'&links='+links+'&texts='+texts+'&borderwidth='+focus_width+'&borderheight='+focus_height+'&textheight='+text_height+'" menu="false" bgcolor="#F0F0F0" quality="high" width="'+ focus_width +'" height="'+ focus_height +'" allowScriptAccess="sameDomain" type="application/x-shockwave-flash" pluginspage="" />');	
	
	document.write('</object>');
   //注意FLAH的路径地址	
</script></td>
  </tr>
  <tr>
    <td><img src="{% static 'qx/images/67_15.jpg' %}" width="274" height="15" alt=""></td>
  </tr>
  <tr>
    <td><img src="{% static 'qx/images/67_17.jpg' %}" width="274" height="14" alt=""></td>
  </tr>
  <tr>
    <td background="{% static 'qx/images/67_19.jpg' %}" height="37" style="padding-left:20px; padding-top:2px;"><span style="font-size:14px; font-weight:bold; color:#FFFFFF">联系我们</span></td>
  </tr>
  <tr>
    <td background="{% static 'qx/images/67_21.jpg' %}" height="149" class="black12a"><table width="100%" height="32" border="0" cellpadding="0" cellspacing="0">
      <tr>
        <td width="87%" style="padding-left:10px; line-height:35px;"><span style="font-weight: bold">上海芊详建筑工程有限公司 </span><br />
                  地址：上海上海闵行区纪鹤路876号 <br />
                  手机：13764616599
                  <br />   
				   电话：021-61521242<br />
		   邮箱：398972844@qq.com</td>
        <td width="13%">&nbsp;</td>
      </tr>
    </table></td>
  </tr>
  <tr>
    <td><img src="{% static 'qx/images/67_25.jpg' %}" width="274" height="16" alt=""></td>
  </tr>
</table>
</td>
    <td width="31">&nbsp;</td>
  </tr>
  <tr>
    <td>&nbsp;</td>
    <td colspan="2" valign="top"><img src="{% static 'qx/images/67_17.jpg' %}" width="943" height="39" /></td>
    <td>&nbsp;</td>
  </tr>
</table>
<table width="1004" border="0" cellspacing="0" cellpadding="0" class="black12a" align="center">
  <tr>
    <td align="center">版权所有：上海芊详建筑工程有限公司&nbsp;技术支持：<a href="http://www.qi-ju.com" target="_blank">企炬</a><br />
      地址：上海上海闵行区纪鹤路876号</td>
  </tr>
</table>
<!-- JiaThis Button BEGIN -->
<script type="text/javascript" src="http://v3.jiathis.com/code/jiathis_r.js?type=left&amp;btn=l1.gif" charset="utf-8"></script>
<!-- JiaThis Button END -->
</body>
</html>
