
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
{% load staticfiles %}
{% load static %} 
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
            <td style="padding-left:60px; font-weight:bold;">成功案例</td>
          </tr>
        </table></td>
      </tr>
      <tr>
        <td background="{% static 'qx/images/67_10.jpg' %}" height="144" valign="top" class="black12a"><table width="100%" border="0" cellspacing="0" cellpadding="0">
          <tr>
            <td width="7%">&nbsp;</td>
            <td width="88%" style="line-height:30px; font-size:13px;" valign="top">
			上海香港避风塘竹艺装修<br>
上海彭浦公园竹篱笆工程<br>
上海廷安绿地竹篱笆工程<br>
上海虹桥路水上人家竹艺装修<br>
上海泥城金盛国际酒店竹篱篱笆围墙<br>
上海永加路商务区竹林园艺<br>
吴江同里农家乐门头安装<br>
上海浦东人造竹林工程<br>
苏州水上饭店竹屋竹长亭<br>
上海纪王园艺公司竹围墙<br>
上海家乐福卖场竹艺柜台<br>
上海华山路领事馆竹围墙<br>
上海南翔小学竹亭工程<br>

			</td>
            <td width="5%">&nbsp;</td>
          </tr>
        </table></td>
      </tr>
      <tr>
        <td><img src="{% static 'qx/images/67_14.jpg' %}" width="669" height="15" alt=""></td>
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
    <td><img src="i{% static 'qx/images/67_25.jpg' %}" width="274" height="16" alt=""></td>
  </tr>
</table>
</td>
    <td width="31">&nbsp;</td>
  </tr>
  <tr>
    <td>&nbsp;</td>
    <td colspan="2" valign="top"><img src="{% static 'qx/images/di.jpg' %}" width="943" height="39" /></td>
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
