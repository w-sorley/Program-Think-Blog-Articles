# 吐槽一下 Windows 的安全漏洞——严重性超乎想象 

-----

 先插播一个“广而告之”。  
 [上一篇博文](https://program-think.blogspot.com/2017/03/Why-Linux-Is-More-Secure-Than-Windows-and-macOS.html)的评论数突破【一千】大关。感谢热心读者的捧场 :)  
 参与讨论的读者增多了之后，俺再次提醒大伙儿：网上的沟通要注意素质，理性讨论，避免过于情绪化。另外，要避免逻辑谬误的陷阱（参见《[扫盲逻辑谬误](https://program-think.blogspot.com/2011/03/logical-fallacies.html)》）。  
 评论数猛增也暴露出之前未发现的一个“评论区的 Bug”。经过几位热心读者的大力支持（帮俺测试），该 bug 已经在前天修复。在此，向这几位热心读者郑重地表示感谢！  
   
   
 ## ★引子
---

  
 前一篇博文《[为什么桌面系统装 Linux 可以做到更好的安全性（相比 Windows & macOS 而言）](https://program-think.blogspot.com/2017/03/Why-Linux-Is-More-Secure-Than-Windows-and-macOS.html)》发出后，不出所料，引发了一些争议。  
 有些读者提的批评意见，指出了俺博文某些地方不严密，俺表示感谢，并且也在博文中加了补充说明（以免引起误解）。  
 但也有些读者的留言，给人感觉是替微软“洗地”的。  
 比如 131楼37单元 的评论说（下面是原话）：  
 
> linux平均的漏洞寿命是5年（Kees Cook），COW漏洞更是存在了9年才被修复。很难想象windows会拖这么久。  
 当俺看到该评论的【最后一句】，不禁哑然失笑——Windows 的安全漏洞之多，在安全业界是有目共睹滴；Windows 安全漏洞潜伏时间之长，在业界也是有目共睹滴。  
 俺写上一篇博文的时候，主要是介绍 Linux（桌面系统）相对于 Windows 和 macOS 的安全优势。当时想给微软留点面子，所以没怎么狠批 Windows 的安全问题。如今有人跳出来洗地，俺就借这个机会，抖一下 Windows 的阴暗面。program-think  
   
   
 ## ★事先声明
-----

  
 为了严密性，避免有人抬杠，俺先说明一下：本文讨论的是用于【桌面】的 Windows 系统。  
 服务端的 Windows、手机端的 Windows、嵌入设备的 Windows，均【不在】本文讨论范围。  
   
   
 ## ★预备知识
-----

  
 ### ◇何为“漏洞”？

  
 关于这个概念的解释，请参见《[如何防止黑客入侵](https://program-think.blogspot.com/2010/06/howto-prevent-hacker-attack-0.html)》系列的第4篇（链接在”[这里](https://program-think.blogspot.com/2010/08/howto-prevent-hacker-attack-4.html)“）。  
   
 ### ◇何为“安全漏洞”？

  
 （同上）  
   
 ### ◇何为“补丁”？

  
 （同上）  
   
 ### ◇啥是“漏洞的潜伏期”？

  
 从漏洞开始引入软件的这个时间点，一直到漏洞被曝光（被公开）的时间点，中间这个时期是“潜伏期”。漏洞一旦被曝光（被公开），软件厂商（开发软件的公司/组织）通常会发布补丁，用于修复此漏洞。  
 在潜伏期，由于漏洞尚未被公开，因此也就【没有】补丁；但是，有可能某些黑客/骇客已经发现了该漏洞，于是这帮人就可以在【没有补丁的情况下】，充分利用该漏洞。  
 可以这么说：可供利用的“未公开漏洞”（处于潜伏期的漏洞）是攻击者的天堂。  
   
 ### ◇【不要】混淆“未公开漏洞”和“零日漏洞”

  
 “零日漏洞”，洋文也叫：“Zero-Day 或 0-Day”。  
 “未公开漏洞”和“零日漏洞”，概念上是完全不同滴，危险性也是完全不同滴——“未公开漏洞”更危险。  
 关于这两者的区别，请看《[如何防止黑客入侵](https://program-think.blogspot.com/2010/06/howto-prevent-hacker-attack-0.html)》系列的第4篇（链接在“[这里](https://program-think.blogspot.com/2010/08/howto-prevent-hacker-attack-4.html)”）。  
   
 ### ◇啥是“CVE”？

  
 CVE 是洋文“Common Vulnerabilities and Exposures”的缩写。  
 通俗地说：这是全球最大、最权威、最有影响力的漏洞库。由美国的非营利组织 MITRE 负责维护和运营。几乎每一个曝光的操作系统漏洞（不论是 Windows 家族还是 Linux 家族、mac 家族、BSD 家族），通常都有对应的 CVE 编号。  
 在 CVE 漏洞库中，每一个漏洞都分配一个唯一的编号，形式如：CVE-YYYY-NNNN。其中的 YYYY 是四位数的年份，NNNN 是四位数的递增编号。  
   
   
 ## ★Windows 安全漏洞举例——对最近2个自然年的统计
----------------------------

  
 为了体现本文的说服力，俺以【事实说话】。  
 下面列出的漏洞，【全部来自微软官网】。也就是说，这些安全漏洞全部都是微软自己承认滴。这些漏洞波及（影响）的范围，也都是微软官方承认滴。  
 考虑到俺只是一介屁民，时间和精力很有限，俺不可能把微软官网历史上所有的安全漏洞都汇总一遍。所以俺挑选了最近的2个【完整自然年】，作为举例——分别是 2016 和 2015。  
   
 ### ◇2016年

  
 **微软在该年度发布了【153个】安全公告**（全部清单在“[这个链接](https://technet.microsoft.com/library/security/mt674627.aspx)”）。  
 请原谅俺的耐心和精力有限，只列出【前20个】（算是抽样）。  
 注：  
 下面列出的安全公告是该年度的前20条，都是在年初曝光的。此时的最新版本是 Win 10。（“Windows Server 2016”要到2016年【下半年】才发布）  
 在2016年上半年，仍然提供支持的最老版本是 Windows Vista。  
 因此，下列的漏洞，如果影响范围是【从 Vista 到 Win10】，那么这个漏洞就是【全系列漏洞】——影响了（漏洞曝光时）所有的 Windows 版本。  
   
 <center><table border="1" cellspacing="0"><tbody>
<tr><th>微软安全公告</th><th>漏洞数</th><th>漏洞的 CVE 号</th><th>漏洞类型</th><th>漏洞所在模块</th><th>潜伏期</th><th>影响范围</th><th>描述</th></tr>
<tr><td><a href="https://technet.microsoft.com/library/security/MS16-001" target="_blank" rel="nofollow">MS16-001</a></td><td>2</td><td>CVE-2016-0002<br />
CVE-2016-0005</td><td><span style="color:red;">远程执行代码</span></td><td>IE 浏览器</td><td><span style="color:red;">10年</span></td><td>从 IE7 到 IE11<br />
&#65288;对应系统版本&#65289;从 Vista 到 Win8.1</td><td>攻击者构造特定网页&#65292;当受害者用上述版本的 IE 访问&#65292;就中招</td></tr>
<tr><td><a href="https://technet.microsoft.com/library/security/MS16-002" target="_blank" rel="nofollow">MS16-002</a></td><td>2</td><td>CVE-2016-0003<br />
CVE-2016-0024</td><td><span style="color:red;">远程执行代码</span></td><td>Edge 浏览器</td><td>1年</td><td>Edge<br />
&#65288;对应系统版本&#65289;Win10</td><td>攻击者构造特定网页&#65292;当受害者用上述版本的 Edge 访问&#65292;就中招</td></tr>
<tr><td><a href="https://technet.microsoft.com/library/security/MS16-003" target="_blank" rel="nofollow">MS16-003</a></td><td>1</td><td>CVE-2016-0002</td><td><span style="color:red;">远程执行代码</span></td><td>VBS 脚本引擎</td><td><span style="color:red;">10年</span></td><td>从 VBS 5.7 到 5.8<br />
&#65288;对应系统版本&#65289;从 Vista 到 Windows Server 2008 R2</td><td>攻击者构造特定网页&#65288;嵌入特定的 VBS 脚本&#65289;&#65292;如果受害者使用的 IE 含有上述版本的 VBS 引擎&#65292;就中招</td></tr>
<tr><td><a href="https://technet.microsoft.com/library/security/MS16-004" target="_blank" rel="nofollow">MS16-004</a></td><td>4</td><td>CVE-2016-0010<br />
CVE-2016-0012<br />
CVE-2016-0017<br />
CVE-2016-0035</td><td><span style="color:red;">远程执行代码</span></td><td>Office</td><td><span style="color:red;">9年</span></td><td>从 Office 2007 到 2016</td><td>攻击者构造特定文档&#65288;Excel&#12289;PowerPoint&#65289;&#65292;当受害者用上述版本的 Office 打开&#65292;就中招</td></tr>
<tr><td><a href="https://technet.microsoft.com/library/security/MS16-005" target="_blank" rel="nofollow">MS16-005</a></td><td>2</td><td>CVE-2016-0008<br />
CVE-2016-0009</td><td><span style="color:red;">远程执行代码</span></td><td>内核的 GDI32 模块<br />
内核的 Win32k.sys 模块</td><td><span style="color:red;">10年</span></td><td>从 Vista 到 Win8.1</td><td>攻击者构造特定网页&#65292;不论受害者用哪种浏览器访问&#65292;都会中招</td></tr>
<tr><td><a href="https://technet.microsoft.com/library/security/MS16-006" target="_blank" rel="nofollow">MS16-006</a></td><td>1</td><td>CVE-2016-0034</td><td><span style="color:red;">远程执行代码</span></td><td>Silverlight</td><td>5年</td><td>Silverlight 5</td><td>攻击者构造特定网页&#65292;当受害者的浏览器安装了上述版本的 Silverlight&#65292;就中招</td></tr>
<tr><td><a href="https://technet.microsoft.com/library/security/MS16-007" target="_blank" rel="nofollow">MS16-007</a></td><td>6</td><td>CVE-2016-0014<br />
CVE-2016-0015<br />
CVE-2016-0016<br />
CVE-2016-0018<br />
CVE-2016-0019<br />
CVE-2016-0020</td><td><span style="color:red;">远程执行代码</span><br />
<span style="color:maroon;">本地提升权限</span><br />
安全特性绕过</td><td>内核的动态库加载<br />
DirectShow<br />
RDP&#65288;远程桌面&#65289;</td><td><span style="color:red;">10年</span></td><td>从 Vista 到 Win10<br />
<span style="color:red;">&#12304;全系列漏洞&#12305;</span></td><td>攻击者可以构造特定文件&#65292;当受害者打开该文件会引发 DirectShow 的堆溢出&#65288;缓冲区溢出&#65289;并执行恶意代码&#12290;<br />
攻击者可以构造特定的动态库&#65292;当受害者的系统加载该动态库会中招&#65292;攻击代码可以提升到管理员权限&#12290;<br />
攻击者可以利用 RDP 的漏洞在没有密码的情况下登录</td></tr>
<tr><td><a href="https://technet.microsoft.com/library/security/MS16-008" target="_blank" rel="nofollow">MS16-008</a></td><td>2</td><td>CVE-2016-0006<br />
CVE-2016-0007</td><td><span style="color:maroon;">本地提升权限</span></td><td>内核</td><td><span style="color:red;">10年</span></td><td>从 Vista 到 Win8.1</td><td>如果攻击者有机会在受害者的系统中执行代码&#65292;就可以利用该漏洞提升到&#8220;管理员权限&#8221;</td></tr>
<tr><td><a href="https://technet.microsoft.com/library/security/MS16-009" target="_blank" rel="nofollow">MS16-009</a></td><td>13</td><td>CVE-2016-0041<br />
CVE-2016-0059<br />
CVE-2016-0060<br />
CVE-2016-0061<br />
CVE-2016-0062<br />
CVE-2016-0063<br />
CVE-2016-0064<br />
CVE-2016-0067<br />
CVE-2016-0068<br />
CVE-2016-0069<br />
CVE-2016-0071<br />
CVE-2016-0072<br />
CVE-2016-0077</td><td><span style="color:red;">远程执行代码</span><br />
<span style="color:maroon;">本地提升权限</span></td><td>IE 浏览器</td><td><span style="color:red;">10年</span></td><td>从 IE9 到 IE11<br />
&#65288;对应系统版本&#65289;从 Vista 到 Win10<br />
<span style="color:red;">&#12304;全系列漏洞&#12305;</span></td><td>攻击者构造特定网页&#65292;当受害者用上述版本的 IE 访问&#65292;就中招&#12290;<br />
这次公告包含大量 IE 浏览器的缓冲区溢出漏洞&#12290;</td></tr>
<tr><td><a href="https://technet.microsoft.com/library/security/MS16-010" target="_blank" rel="nofollow">MS16-010</a></td><td>-</td><td>-</td><td>-</td><td>Exchange Server</td><td>-</td><td>-</td><td>&#65288;这个是关于服务端软件的漏洞&#65292;与本文无关&#65289;</td></tr>
<tr><td><a href="https://technet.microsoft.com/library/security/MS16-011" target="_blank" rel="nofollow">MS16-011</a></td><td>4</td><td>CVE-2016-0060<br />
CVE-2016-0061<br />
CVE-2016-0062<br />
CVE-2016-0080</td><td><span style="color:red;">远程执行代码</span></td><td>Edge 浏览器</td><td>1年</td><td>Edge<br />
&#65288;对应系统版本&#65289;Win10</td><td>攻击者构造特定网页&#65292;当受害者用上述版本的 Edge 访问&#65292;就中招</td></tr>
<tr><td><a href="https://technet.microsoft.com/library/security/MS16-012" target="_blank" rel="nofollow">MS16-012</a></td><td>2</td><td>CVE-2016-0046<br />
CVE-2016-0058</td><td><span style="color:red;">远程执行代码</span></td><td>PDF Library<br />
Windows Reader</td><td>3年</td><td>从 Win8.1 到 Win10</td><td>攻击者构造特定文档&#65292;当受害者用上述版本的 Reader 打开&#65292;就中招</td></tr>
<tr><td><a href="https://technet.microsoft.com/library/security/MS16-013" target="_blank" rel="nofollow">MS16-013</a></td><td>1</td><td>CVE-2016-0038</td><td><span style="color:red;">远程执行代码</span></td><td>Windows Journal</td><td><span style="color:red;">10年</span></td><td>从 Vista 到 Win10<br />
<span style="color:red;">&#12304;全系列漏洞&#12305;</span></td><td>攻击者构造特定的 Journal 文档&#65292;当受害者打开&#65292;就中招</td></tr>
<tr><td><a href="https://technet.microsoft.com/library/security/MS16-014" target="_blank" rel="nofollow">MS16-014</a></td><td>4</td><td>CVE-2016-0040<br />
CVE-2016-0041<br />
CVE-2016-0042<br />
CVE-2016-0049</td><td><span style="color:red;">远程执行代码</span><br />
<span style="color:maroon;">本地提升权限</span></td><td>内核</td><td><span style="color:red;">10年</span></td><td>从 Vista 到 Win10<br />
<span style="color:red;">&#12304;全系列漏洞&#12305;</span></td><td>如果攻击者有机会在受害者的系统中执行代码&#65292;就可以利用该漏洞提升到&#8220;管理员权限&#8221;</td></tr>
<tr><td><a href="https://technet.microsoft.com/library/security/MS16-015" target="_blank" rel="nofollow">MS16-015</a></td><td>6</td><td>CVE-2016-0022<br />
CVE-2016-0039<br />
CVE-2016-0052<br />
CVE-2016-0053<br />
CVE-2016-0055<br />
CVE-2016-0056</td><td><span style="color:red;">远程执行代码</span></td><td>Office</td><td><span style="color:red;">9年</span></td><td>从 Office 2007 到 2016</td><td>攻击者构造特定文档&#65288;Word&#12289;Excel&#65289;&#65292;当受害者用上述版本的 Office 打开&#65292;就中招</td></tr>
<tr><td><a href="https://technet.microsoft.com/library/security/MS16-016" target="_blank" rel="nofollow">MS16-016</a></td><td>1</td><td>CVE-2016-0051</td><td><span style="color:maroon;">本地提升权限</span></td><td>WebDAV</td><td><span style="color:red;">10年</span></td><td>从 Vista 到 Win10<br />
<span style="color:red;">&#12304;全系列漏洞&#12305;</span></td><td>如果攻击者有机会在受害者的系统中执行代码&#65292;就可以利用该漏洞提升到&#8220;管理员权限&#8221;</td></tr>
<tr><td><a href="https://technet.microsoft.com/library/security/MS16-017" target="_blank" rel="nofollow">MS16-017</a></td><td>1</td><td>CVE-2016-0036</td><td><span style="color:maroon;">本地提升权限</span></td><td>RDP&#65288;远程桌面&#65289;</td><td><span style="color:red;">7年</span></td><td>从 Win7 到 Win10</td><td>如果受害者的系统开启了远程桌面服务&#65292;攻击者通过远程桌面登录到该系统之后&#65292;可以利用此漏洞提升到&#8220;管理员权限&#8221;</td></tr>
<tr><td><a href="https://technet.microsoft.com/library/security/MS16-018" target="_blank" rel="nofollow">MS16-018</a></td><td>1</td><td>CVE-2016-0048</td><td><span style="color:maroon;">本地提升权限</span></td><td>内核 Win32k.sys 模块</td><td><span style="color:red;">10年</span></td><td>从 Vista 到 Win8.1</td><td>如果攻击者有机会在受害者的系统中执行代码&#65292;就可以利用该漏洞提升到&#8220;管理员权限&#8221;</td></tr>
<tr><td><a href="https://technet.microsoft.com/library/security/MS16-019" target="_blank" rel="nofollow">MS16-019</a></td><td>2</td><td>CVE-2016-0033<br />
CVE-2016-0047</td><td>拒绝服务</td><td>dotNet Framework</td><td><span style="color:red;">10年</span></td><td>从 dotNet Framework 2.0 到 4.6<br />
&#65288;对应系统版本&#65289;从 Vista 到 Win10<br />
<span style="color:red;">&#12304;全系列漏洞&#12305;</span></td><td>攻击者构造特定的 XSLT 文档&#65292;当受害者打开会导致系统崩溃&#12290;<br />
&#65288;.Net Framework 2.0 发布于2006年&#65292;漏洞的潜伏期从那年起算&#65289;</td></tr>
<tr><td><a href="https://technet.microsoft.com/library/security/MS16-020" target="_blank" rel="nofollow">MS16-020</a></td><td>-</td><td>-</td><td>-</td><td>Active Directory</td><td>-</td><td>-</td><td>&#65288;这个是关于服务端软件的漏洞&#65292;与本文无关&#65289;</td></tr>
</tbody></table></center>   
 ### ◇2015

  
 **微软在该年度发布了【135个】安全公告**（全部清单在“[这个链接](https://technet.microsoft.com/library/security/dn903755.aspx)”）。  
 请原谅俺的耐心和精力有限，只整理出【前20个】（算是抽样）。  
 注：  
 下面列出的安全公告是该年度的前20条，都是在年初曝光的。此时的最新版本是 Win 8.1。（“Windows 10 和 Windows Server 2016”要到2015年【下半年】才发布）  
 在2015年上半年，仍然提供支持的最老版本是 Windows 2003。  
 因此，下列的漏洞，如果影响范围是【从 Win2003 到 Win8.1】，那么这个漏洞就是【全系列漏洞】——影响了（漏洞曝光时）所有的 Windows 版本。  
   
 <center><table border="1" cellspacing="0"><tbody>
<tr><th>微软安全公告</th><th>漏洞数</th><th>漏洞的 CVE 号</th><th>漏洞类型</th><th>漏洞所在的模块</th><th>潜伏期</th><th>影响范围</th><th>描述</th></tr>
<tr><td><a href="https://technet.microsoft.com/library/security/MS15-001" target="_blank" rel="nofollow">MS15-001</a></td><td>1</td><td>CVE-2015-0002</td><td><span style="color:maroon;">本地提升权限</span></td><td>内核的 ahcache.sys 模块</td><td><span style="color:red;">6年</span></td><td>从 Win7 到 Win8.1</td><td>如果攻击者有机会在受害者的系统中执行代码&#65292;就可以利用该漏洞提升到&#8220;管理员权限&#8221;</td></tr>
<tr><td><a href="https://technet.microsoft.com/library/security/MS15-002" target="_blank" rel="nofollow">MS15-002</a></td><td>1</td><td>CVE-2015-0014</td><td><span style="color:red;">远程执行代码</span></td><td>Telnet 服务</td><td><span style="color:red;">12年</span></td><td>从 Win2003 到 Win8.1<br />
<span style="color:red;">&#12304;全系列漏洞&#12305;</span></td><td>如果受害者的系统启用了 telnet 服务&#65292;攻击者远程连上 telnet 的 TCP 端口后&#65292;可以利用该漏洞执行恶意代码&#12290;</td></tr>
<tr><td><a href="https://technet.microsoft.com/library/security/MS15-003" target="_blank" rel="nofollow">MS15-003</a></td><td>1</td><td>CVE-2015-0004</td><td><span style="color:maroon;">本地提升权限</span></td><td>User Profile 服务</td><td><span style="color:red;">12年</span></td><td>从 Win2003 到 Win8.1<br />
<span style="color:red;">&#12304;全系列漏洞&#12305;</span></td><td>如果攻击者有机会在受害者的系统中执行代码&#65292;就可以利用该漏洞提升到&#8220;管理员权限&#8221;</td></tr>
<tr><td><a href="https://technet.microsoft.com/library/security/MS15-004" target="_blank" rel="nofollow">MS15-004</a></td><td>1</td><td>CVE-2015-0016</td><td><span style="color:maroon;">本地提升权限</span></td><td>WebProxy 模块</td><td><span style="color:red;">9年</span></td><td>从 Vista 到 Win8.1</td><td>如果攻击者有机会在受害者的系统中执行代码&#65292;就可以利用该漏洞提升到&#8220;管理员权限&#8221;</td></tr>
<tr><td><a href="https://technet.microsoft.com/library/security/MS15-005" target="_blank" rel="nofollow">MS15-005</a></td><td>1</td><td>CVE-2015-0006</td><td>安全特性绕过</td><td>NLA 服务</td><td><span style="color:red;">12年</span></td><td>从 Win2003 到 Win8.1<br />
<span style="color:red;">&#12304;全系列漏洞&#12305;</span></td><td>当攻击者与受害者处于同一个网络&#65288;domain&#65289;&#65292;攻击者可以利用此漏洞进行 DNS/LDAP 欺骗&#12290;</td></tr>
<tr><td><a href="https://technet.microsoft.com/library/security/MS15-006" target="_blank" rel="nofollow">MS15-006</a></td><td>1</td><td>CVE-2015-0001</td><td>安全特性绕过</td><td>WER&#65288;错误报告&#65289;</td><td>3年</td><td>从 Win8 到 Win8.1</td><td>攻击者需要先登录到系统中&#65292;然后利用此漏洞可以读取任何进程的内存&#12290;</td></tr>
<tr><td><a href="https://technet.microsoft.com/library/security/MS15-007" target="_blank" rel="nofollow">MS15-007</a></td><td>-</td><td>-</td><td>-</td><td>Network Policy Server</td><td>-</td><td>-</td><td>&#65288;这个是关于服务端软件的漏洞&#65292;与本文无关&#65289;</td></tr>
<tr><td><a href="https://technet.microsoft.com/library/security/MS15-008" target="_blank" rel="nofollow">MS15-008</a></td><td>1</td><td>CVE-2015-0011</td><td><span style="color:maroon;">本地提升权限</span></td><td>内核 mrxdav.sys 模块</td><td><span style="color:red;">12年</span></td><td>从 Win2003 到 Win8.1<br />
<span style="color:red;">&#12304;全系列漏洞&#12305;</span></td><td>如果攻击者有机会在受害者的系统中执行代码&#65292;就可以利用该漏洞提升到&#8220;管理员权限&#8221;</td></tr>
<tr><td><a href="https://technet.microsoft.com/library/security/MS15-009" target="_blank" rel="nofollow">MS15-009</a></td><td>41</td><td>涉及的漏洞太多<br />
不逐一列出 CVE</td><td><span style="color:red;">远程执行代码</span><br />
拒绝服务</td><td>IE 浏览器</td><td><span style="color:red;">14年</span></td><td>从 IE6 到 IE11<br />
<span style="color:red;">&#12304;IE 全系列漏洞&#12305;</span><br />
&#65288;对应系统版本&#65289;从 Win2000 到 Win8.1</td><td>攻击者构造特定网页&#65292;当受害者用上述版本的 IE 访问&#65292;就中招</td></tr>
<tr><td><a href="https://technet.microsoft.com/library/security/MS15-010" target="_blank" rel="nofollow">MS15-010</a></td><td>6</td><td>CVE-2015-0003<br />
CVE-2015-0010<br />
CVE-2015-0057<br />
CVE-2015-0058<br />
CVE-2015-0059<br />
CVE-2015-0060</td><td><span style="color:maroon;">本地提升权限</span><br />
<span style="color:red;">远程执行代码</span></td><td>内核 Win32k.sys 模块</td><td><span style="color:red;">12年</span></td><td>从 Win2003 到 Win8.1<br />
<span style="color:red;">&#12304;全系列漏洞&#12305;</span></td><td>攻击者构造特定网页&#65292;内含特定的 TrueType 字体&#12290;不论受害者用哪种浏览器访问&#65292;都会中招</td></tr>
<tr><td><a href="https://technet.microsoft.com/library/security/MS15-011" target="_blank" rel="nofollow">MS15-011</a></td><td>1</td><td>CVE-2015-0008</td><td><span style="color:red;">远程执行代码</span></td><td>Group Policy</td><td><span style="color:red;">12年</span></td><td>从 Win2003 到 Win8.1<br />
<span style="color:red;">&#12304;全系列漏洞&#12305;</span></td><td>如果攻击者掌握了某个&#8220;主域控制器&#8221;&#65292;可以通过构造特定的&#8220;域策略&#8221;并下发&#65292;所有加入该域的主机都会中招&#12290;</td></tr>
<tr><td><a href="https://technet.microsoft.com/library/security/MS15-012" target="_blank" rel="nofollow">MS15-012</a></td><td>3</td><td>CVE-2015-0063<br />
CVE-2015-0064<br />
CVE-2015-0065</td><td><span style="color:red;">远程执行代码</span></td><td>Office</td><td><span style="color:red;">8年</span></td><td>从 Office 2007 到 2013</td><td>攻击者构造特定文档&#65288;Word&#12289;Excel&#65289;&#65292;当受害者用上述版本的 Office 打开&#65292;就中招</td></tr>
<tr><td><a href="https://technet.microsoft.com/library/security/MS15-013" target="_blank" rel="nofollow">MS15-013</a></td><td>1</td><td>CVE-2014-6362</td><td>安全特性绕过</td><td>Office</td><td><span style="color:red;">8年</span></td><td>从 Office 2007 到 2013</td><td>该漏洞可以让攻击者绕过 ASLR&#65288;地址空间布局随机化&#65289;&#65292;有助于后续进行&#8220;远程执行代码&#8221;的攻击</td></tr>
<tr><td><a href="https://technet.microsoft.com/library/security/MS15-014" target="_blank" rel="nofollow">MS15-014</a></td><td>1</td><td>CVE-2015-0009</td><td>安全特性绕过</td><td>Group Policy</td><td><span style="color:red;">12年</span></td><td>从 Win2003 到 Win8.1<br />
<span style="color:red;">&#12304;全系列漏洞&#12305;</span></td><td>攻击者可以利用此漏洞进行&#8220;中间人攻击&#8221;&#65292;篡改&#8220;主域控制器&#8221;下发的组策略&#65292;使得&#8220;域成员主机&#8221;收到的组策略变得缺乏安全性&#12290;</td></tr>
<tr><td><a href="https://technet.microsoft.com/library/security/MS15-015" target="_blank" rel="nofollow">MS15-015</a></td><td>1</td><td>CVE-2015-0062</td><td><span style="color:maroon;">本地提升权限</span></td><td>内核</td><td><span style="color:red;">8年</span></td><td>从 Win7 到 Win8.1</td><td>如果攻击者有机会在受害者的系统中执行代码&#65292;就可以利用该漏洞提升到&#8220;管理员权限&#8221;</td></tr>
<tr><td><a href="https://technet.microsoft.com/library/security/MS15-016" target="_blank" rel="nofollow">MS15-016</a></td><td>1</td><td>CVE-2015-0061</td><td>信息泄漏</td><td>图形组件</td><td><span style="color:red;">12年</span></td><td>从 Win2003 到 Win8.1<br />
<span style="color:red;">&#12304;全系列漏洞&#12305;</span></td><td>攻击者构造特定的网页或文档&#65288;其中嵌入特定的 TIFF 图片&#65289;&#65292;当受害者打开该网页或文档&#65292;就中招&#65288;攻击者可以获取某些进程的内存&#65289;</td></tr>
<tr><td><a href="https://technet.microsoft.com/library/security/MS15-017" target="_blank" rel="nofollow">MS15-017</a></td><td>-</td><td>-</td><td>-</td><td>VMM Server&#65288;虚拟机管理服务器&#65289;</td><td>-</td><td>-</td><td>&#65288;这个是关于服务端软件的漏洞&#65292;与本文无关&#65289;</td></tr>
<tr><td><a href="https://technet.microsoft.com/library/security/MS15-018" target="_blank" rel="nofollow">MS15-018</a></td><td>9</td><td>CVE-2015-0056<br />
CVE-2015-0099<br />
CVE-2015-0100<br />
CVE-2015-01622<br />
CVE-2015-01623<br />
CVE-2015-01624<br />
CVE-2015-01625<br />
CVE-2015-01626<br />
CVE-2015-01634</td><td><span style="color:red;">远程执行代码</span></td><td>IE 浏览器</td><td><span style="color:red;">14年</span></td><td><br />
从 IE6 到 IE11<br />
<span style="color:red;">&#12304;IE 全系列漏洞&#12305;</span><br />
&#65288;对应系统版本&#65289;从 Win2000 到 Win8.1</td><td>攻击者构造特定网页&#65292;当受害者用上述版本的 IE 访问&#65292;就中招</td></tr>
<tr><td><a href="https://technet.microsoft.com/library/security/MS15-019" target="_blank" rel="nofollow">MS15-019</a></td><td>1</td><td>CVE-2015-0032</td><td><span style="color:red;">远程执行代码</span></td><td>VBS 脚本引擎</td><td><span style="color:red;">12年</span></td><td>从 VBS 5.6 到 5.8<br />
&#65288;对应系统版本&#65289;从 Win2003 到 Windows Server 2008 R2</td><td>攻击者构造特定网页&#65288;嵌入特定的 VBS 脚本&#65289;&#65292;如果受害者使用的 IE 含有上述版本的 VBS 引擎&#65292;就中招</td></tr>
<tr><td><a href="https://technet.microsoft.com/library/security/MS15-020" target="_blank" rel="nofollow">MS15-020</a></td><td>2</td><td>CVE-2015-0081<br />
CVE-2015-0096</td><td><span style="color:red;">远程执行代码</span></td><td>WTS&#65288;文本服务&#65289;<br />
内核的动态库加载</td><td><span style="color:red;">12年</span></td><td>从 Win2003 到 Win8.1<br />
<span style="color:red;">&#12304;全系列漏洞&#12305;</span></td><td>攻击者构造特定的网页或文档&#65292;当受害者打开该网页或文档&#65292;就中招<br />
攻击者可以构造特定的远程共享目录或者USB盘&#65292;当受害者用&#8220;资源管理器&#8221;访问该共享目录或U盘&#65292;就中招</td></tr>
</tbody></table></center>   
   
 ## ★关于 Windows 安全漏洞的“潜伏期”——实际情况比统计表中看到的更长
--------------------------------------

  
 在微软官方的安全公告中，明确指出：生命周期已经结束（已经终止支持）的 Windows 版本，是【不会】出现在安全公告中的。  
 考虑到这点，所以俺上面列出的“潜伏期”总是【偏小】滴。  
 为啥捏？俺来解释一下：  
 假设有一个 WinXP 的安全漏洞，一直遗留在 Windows 内核中，一直到 2016年 才被发现。此时，微软的安全公告列出的受影响系统，只会包含：从 Windows Vista 一直到 Win10。而不会有 WinXP 和 Win2003。因为在 2016年，这两个系统已经终止支持。  
 对该漏洞，俺如果根据微软的安全公告计算潜伏期，（由于微软公布的信息不足）俺只能从 Vista 开始算起。得出的计算结果是 **10年**（Vista 是2006年发布）；但实际上，这个漏洞的潜伏期是 **15年**（应该从 2001年 发布 WinXP 开始算起）。  
 但即使这样（由于信息不足而导致计算出的“潜伏期”偏小），你也会发现：Windows 的安全漏洞，潜伏期都很长。  
   
 为了方便跟漏洞列表中的“潜伏期”作对照，俺列出各个 Windows 版本的生命周期。  
 <center><table border="1" cellspacing="0"><tbody>
<tr><th>操作系统版本</th><th>发布时间</th><th>终止支持时间</th></tr>
<tr><td>Windows 2000</td><td>2000年2月</td><td>2010年7月</td></tr>
<tr><td>Windows XP</td><td>2001年10月</td><td>2014年4月</td></tr>
<tr><td>Windows Server 2003</td><td>2003年4月</td><td>2015年7月</td></tr>
<tr><td>Windows Vista</td><td>2006年11月</td><td>2017年4月</td></tr>
<tr><td>Windows Server 2008</td><td>2008年2月</td><td>2020年1月</td></tr>
<tr><td>Windows 7</td><td>2009年7月</td><td>2020年1月</td></tr>
<tr><td>Windows Server 2008 R2</td><td>2009年7月</td><td>2020年1月</td></tr>
<tr><td>Windows 8</td><td>2012年10月</td><td>2023年1月</td></tr>
<tr><td>Windows Server 2012</td><td>2012年10月</td><td>2023年10月</td></tr>
<tr><td>Windows 8.1</td><td>2013年10月</td><td>2023年1月</td></tr>
<tr><td>Windows Server 2012 R2</td><td>2013年10月</td><td>2023年10月</td></tr>
<tr><td>Windows 10</td><td>2015年7月</td><td>2026年10月</td></tr>
<tr><td>Windows Server 2016</td><td>2016年9月</td><td>2027年1月</td></tr>
</tbody></table></center>   
   
 ## ★为啥 IE 浏览器的漏洞特别危险？
------------------

  
 浏览器相关的漏洞，特别危险——因为攻击者可以构造一个“挂马的网页”，当你访问这个页面就会中招。  
 这种情况下，很多安全工具是【无法】帮助防范的，原因如下：  
 1. 因为你的浏览器总是要上网的，所以你的防火墙，不论设置了多么严格的规则，也【无法】防范这类“基于 Web 的攻击”。  
 2. 如果攻击者利用的是【未公开】漏洞，你安装的杀毒软件很可能【无法】防范。因为杀毒软件是基于【事后收集】来形成杀毒软件的特征库。针对未公开漏洞的攻击代码，尚未进入它们的特征库。  
 3. 很多杀毒软件吹嘘他们具有“基于行为识别的防范机制”。这大部分都是用来进行市场营销宣传的噱头，其效果令人怀疑。  
   
   
 ## ★（在 Windows 上）改用其它浏览器上网，并【不能】消除 IE 的危险性
---------------------------------------

  
 很多读者看了上面一段，吓坏了。他们肯定在想，要换一个浏览器，别再用 IE 了。  
 但是俺想提醒你一下：**（在 Windows 上）IE 是无处不在滴，即使你改用其它浏览器（比如 Chrome/Firefox），依然存在 IE 的风险。** 
 下面俺来解释一下——为啥【IE 是无处不在滴】。  
 从上世纪90年代的 Win98 一直到 Win10（2015年发布），IE 都是内置（捆绑）到 Windows 中的。你【没办法】从 Windows 中【彻底移除】IE。没法移除也就算了，但是有很多软件会依赖 IE 的组件来处理 Web 内容。这种情况下，能针对 IE 的攻击代码，通常也可以攻击这些“调用了 IE 的软件”。  
   
 举个“邮件客户端依赖 IE”的例子：  
 当你用 Outlook 或 Outlook Express 收邮件，如果你收到的邮件内容是基于 HTML 的（这很常见），那么 Outlook/Outlook Express 会调用 IE 相应的组件来渲染这些含有 HTML 内容的邮件。不光是 Outlook 或 Outlook Express，其它一些【第三方】的邮件客户端软件，也会依赖 IE 的组件来渲染 HTML 内容的邮件。这种做法很普遍，因为 IE 是 Windows 的标配，对那些开发邮件客户端的程序员来说，这么干是最省事儿的（俺也做过 Windows 程序猿，很清楚这种玩法）。  
 在这种情况下，如果 IE 存在未公开漏洞，攻击者就可以通过给你发（HTML 格式的）邮件，来利用这个漏洞，从而让你中招。  
   
 再举个“Office 依赖 IE”的例子：  
 用 Windows 的同学，俺相信 95% 以上都装了 Office。不管你平时是否需要文字处理，反正 Office 基本上是 Windows 的标配。  
 假设 IE 的 Web 引擎存在某个【未公开的】缓冲区溢出漏洞，可以导致“执行代码”。那么攻击者可以在网上提供一个 Word 格式（doc/docx）的文档（或者通过邮件/IM 等方式分发这个文档），文档中包含基于 HTML 的 Web 内容。这段 HTML 是精心构造的，可以利用 IE 的上述漏洞。那么，当你拿到这个文档并双击打开，此时 Windows 会启动 Word 来加载该文档，Word 发现文档中有 Web 内容，会调用 IE 的引擎来渲染，于是你就中招了。由于这个漏洞可以导致“执行代码”，那么攻击者可以在你的系统中安装一个木马。之后就可以玩很多花样啦 :(  
   
   
 ## ★更要命的是——IE 浏览器的安全漏洞还特别多
-----------------------

  
 某个专门研究 IE 的御用骇客说过一句话（大意是）：IE 的漏洞之多，就像筛子一样。  
 看完俺下面的统计数字，你就能体会——此话一点不夸张。  
   
 在俺整理的这40个公告中，累计漏洞数 129 个，“浏览器相关”的漏洞占了很大比例：  
 65个是 IE 浏览器本身的漏洞  
 6个是 Edge 浏览器本身的漏洞  
 6个是 其它模块的漏洞（但可以通过 IE 或 Edge 触发）  
   
 也就是说，在俺抽样的40个安全公告中，浏览器相关的漏洞（77个），占了漏洞总数的比例是 59.6%。而这些浏览器相关的漏洞，类型是【远程执行代码】又占了很大比例。这种类型的漏洞是最危险的（没有之一）。  
   
 可能有些同学会怀疑：俺抽样的这40个安全公告，在统计学上有偏差。  
 那俺还可以再告诉你另一批数据（更吓人）——几乎每一个月，都会有 IE 相关的安全公告，而且 IE 的公告披露的漏洞往往很多（通常在十个左右）。下面拿 2016年 来举例：  
   
 <center><table border="1" cellspacing="0"><tbody>
<tr><th>安全公告编号</th><th>发布时间</th><th>IE 漏洞数</th></tr>
<tr><td>MS16-009</td><td>2月</td><td>13个</td></tr>
<tr><td>MS16-023</td><td>3月</td><td>13个</td></tr>
<tr><td>MS16-037</td><td>4月</td><td>6个</td></tr>
<tr><td>MS16-051</td><td>5月</td><td>5个</td></tr>
<tr><td>MS16-063</td><td>6月</td><td>10个</td></tr>
<tr><td>MS16-084</td><td>7月</td><td>14个</td></tr>
<tr><td>MS16-095</td><td>8月</td><td>9个</td></tr>
<tr><td>MS16-104</td><td>9月</td><td>10个</td></tr>
<tr><td>MS16-118</td><td>10月</td><td>11个</td></tr>
<tr><td>MS16-142</td><td>11月</td><td>6个</td></tr>
<tr><td>MS16-144</td><td>12月</td><td>8个</td></tr>
</tbody></table></center>   
 看完上述表格，你是否联想到——像筛子一样多的漏洞？而且这还只是 IE 相关的漏洞，Edge 还【没有】算在内哦。  
 在安全圈混了这么多年（20年大概有了），俺的印象是：IE 总是不停地不停地曝光高危漏洞（远程执行代码）。  
   
   
 ## ★八卦一下：为啥 IE 这么烂？
----------------

  
 （本章节是八卦，不想看八卦的请自行略过）  
 凭良心说，微软是一家不错的公司；微软的程序员，平均素质也不算差。那为啥 IE 这么烂捏？  
 考虑到篇幅已经很长，下面俺简单聊一下：  
   
 ### ◇1. Web 引擎本来就很难写

  
 Web 浏览器需要依靠 Web 引擎来渲染网页。网页是用 HTML 编写的。HTML 的语法很灵活，本来就很难处理；而很多网站的写手（Web 程序员）写出来的网页甚至都没有严格遵循 HTML 语法。浏览器的引擎需要尽量智能地处理这些不规范的 HTML 语法。  
 HTML 还允许嵌入样式表（CSS）和脚本（JavaScript）。而 JS 脚本的语法又是出了名的灵活。因此，写一个浏览器的 JS 引擎也是蛮有难度滴（Google 的 V8 引擎能获得如此高的赞誉，就是因为 JS 引擎难写）  
   
 ### ◇2. IE 的开发团队曾经出现长期断档

  
 如果你观察 IE 版本的历史，会发现 IE6 之后停滞了长达 5年 才发布了 IE7。  
 据说 IE6 发布之后，微软把整个 IE 团队都解散了，只留少数几个人负责改 bug。因为当时的微软领导层觉得 IE6 作为浏览器已经很完善了，而且浏览器这个产品本身没有利润，不值得投入太多人。  
 （这是微软领导层的严重失策）  
 这个决策造成了整个团队严重的断档。等到后来重启 IE7 的开发，新加入的程序员，很多都没有经手过前面的开发，完全不知道原有的代码中留下哪些“坑”（技术陷阱）。  
 （如果你曾经管理过程序员团队，对上述这种情况应该深有体会）  
 有些天真的同学会问：老团队虽然解散了，应该还会有文档留下来啊。新团队可以通过文档了解情况嘛。  
 这么问的同学，多半属于“图样图森破”。当软件项目复杂到一定程度，你就不要指望文档是完备的。在这种软件项目里，有相当比例的文档，要么不全，要么不够新（与代码脱节），要么是错的。这不是一两家公司的个案，这是整个软件行业的通病。  
   
 ### ◇3. 过于陈旧的架构

  
 目前 IE 使用的 Trident 引擎是在 1997年 引入 IE4 的（20年之前哦）。1997年是什么年代，年青的程序员可能没体会。俺正好借这个机会倚老卖老一下。  
 （据说 IE 是用 C++ 写的，俺就拿 C++ 来举例）那时候，C++ 尚未标准化（第一次标准化是 C++98）。以现在的眼光看，那年头简直就是 C++ 的洪荒年代。  
 虽然俺没有看过 IE 的源代码，但是可以合理地猜测：在那么久远的年代，设计一个全新的软件（浏览器在当时算是新事物），而且这个软件的需求又超复杂（参见前面提及的“Web 引擎复杂度”），设计出来的架构，其水平会好到哪里去？  
   
 ### ◇4. （对旧架构）只敢修修补补，不敢大改

  
 在长达二十年的时间里，硬件环境有了巨大变化（多核多CPU），Web 标准也有了巨大的变化（更灵活更复杂了）。为了适应环境的变化，IE 的 Trident 引擎早就应该动一些“大手术”，对架构作一些大的调整。但是前面说过，IE6 之后，开发团队出现长达5年的断档（团队被解散）。IE7 之后的那帮 IE 团队的程序员，全都是新人（此处的“新人”是指：对老代码不熟）。所以俺猜测：他们只敢在旧的架构上修修补补，不敢动“大手术”。（如果你在大公司待过，一定明白：多做多出错，少做少出错，不做不出错）  
   
   
 ## ★IE 这么烂，那能指望 Edge 吗？
--------------------

  
 前面费了这么多口水聊 IE，下面用三句话概括一下：  
 从 Win98 到 Win10（甚至下一代的 WinXX），IE 都是无处不在滴（很多软件会调用 IE 组件）；  
 从 Win98 到 Win10（甚至下一代的 WinXX），IE 都是【无法】彻底移除滴；  
 IE 的代码很烂，相关的漏洞非常多。  
   
 前几年，微软高调推出全新的浏览器“Microsoft Edge”。为啥微软要另起炉灶？除了外部的因素（市场营销策略），内部因素恐怕就是俺刚才分析的原因——IE 已经老朽不堪，难以维护了。  
 估计有些同学在默默指望着：用 Edge 彻底替代老朽不堪的 IE。俺劝这些同学别抱太大期望。  
 前面已经提到：很多 Windows 上的应用软件（包括微软自己的软件以及第三方软件）重度依赖 IE 组件。出于兼容性的考虑，微软不可能在短期内彻底抛弃 IE。也就是说：在很长时间内，IE 会与 Edge 并存（Win10 就是一个例证）。  
   
   
 ## ★最后，稍微聊一下：Windows 的“树大招风”
-------------------------

  
 最后来提一下“树大招风”引发的风险。  
 在【桌面系统】的市场份额中，Windows 是毫无疑问的老大。所以，各种黑客与骇客，都会花很多精力来研究如何去入侵 Windows 系统。这就是所谓的——树大招风。  
 关于“树大招风”这点，应该没有太大争议。俺之所以单独写这个章节，是想【反驳】前一篇博文的某条读者留言。  
 该读者认为：御用骇客针对的是高价值目标，而高价值目标用 Linux 的比较多，所以御用骇客会花更多精力研究 Linux 的漏洞，这就导致——使用 Linux 反而容易碰到”被利用的未公开漏洞“。  
   
 **下面是俺的反驳：** 
 上述这个推理过程，第一个前提（御用骇客针对高价值目标），是正确滴。错误发生在第二个前提（高价值目标用 Linux 的比较多）。  
 这个读者混淆了两个不同的概念：高价值目标 和 技术高手（“高价值目标”不一定是“技术高手”，“技术高手”也不一定是“高价值目标”）  
 俺借此机会给大伙儿介绍一下，天朝御用骇客心目中的高价值目标，大概是哪些：  
 
> 重要的外国政治人物  
>  重要的民运人士、政治异议人士  
>  外国政府机构（尤其是涉密机构）的雇员  
>  国外敏感企业（尤其是军工企业）的雇员  
>  从事“分离运动/独立运动”的少数民族组织  
>   上述这些高价值目标，难道他们会去玩 Linux？NO，他们的桌面系统依然是以 Windows 为主，其次是 macOS。所以很自然的，朝廷的御用骇客，也是以 Windows 漏洞的研究为主，macOS 为辅。（当然也有御用骇客在研究 Linux 漏洞，但他们在 Linux 上的投入，远不如 Windows，也不如 macOS）  
   
   
 ## ★结论
---

  
 所以俺早在 N年前 就一直劝周围的同事和朋友，把日常使用的系统切换成别的（Linux、BSD、macOS 都要远远好于 Windows）。  
 切换系统并没有你想象的那么困难。得益于虚拟化软件，你可以先在某个虚拟系统中使用 Linux 或 macOS，慢慢适应，然后慢慢过渡。接下来，俺会写一些关于 Linux 的扫盲教程，帮助技术菜鸟在虚拟机中玩转 Linux。  
   
   
 **俺博客上，和本文相关的帖子（需翻墙）**：  
 [如何防止黑客入侵](https://program-think.blogspot.com/2010/06/howto-prevent-hacker-attack-0.html)  
 [为什么桌面系统装 Linux 可以做到更好的安全性（相比 Windows & macOS 而言）](https://program-think.blogspot.com/2017/03/Why-Linux-Is-More-Secure-Than-Windows-and-macOS.html) 