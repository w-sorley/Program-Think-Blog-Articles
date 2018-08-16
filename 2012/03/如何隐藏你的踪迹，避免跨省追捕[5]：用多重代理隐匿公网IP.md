# 如何隐藏你的踪迹，避免跨省追捕[5]：用多重代理隐匿公网IP 

-----

 最近，天朝的两会即将通过新版本的刑事诉讼法（在新条款中，党国的爪牙可以**合法地**进行秘密拘捕，大大滴阴险啊）。所以，俺要继续完善[“如何隐藏踪迹”系列](https://program-think.blogspot.com/2010/04/howto-cover-your-tracks-0.html)，帮助大伙儿躲避朝廷的网络追捕。  
 关于多重代理，在前几个月的翻墙贴《[扫盲 VPN 翻墙——以 Hotspot Shield 为例](https://program-think.blogspot.com/2011/09/gfw-vpn-hotspot-shield.html)》中，稍微提到过。今天来完整地介绍一下。program-think  
   
 ## ★什么是多重代理？
---------

  
 先声明一下：本文所说的“代理”是广义的，包括了：“传统意义上的代理”和“VPN”。  
 平时咱们用代理来翻墙，大部分属于一重代理（如下图）。也就是说，不论你用的是 VPN 还是 HTTP Proxy 还是 SOCKS Proxy，当中都只有一个服务器进行中转。  
 ![不见图 请翻墙](images/Rgn4KkxdyjmPB38AzrpvSsbN4fipGKcQ1H0ZuoerIncEbSCABXF23FGZ5xY2qw4RZ24dQv0Dq3gqGnn-pMNXbfb4AyXV1sOht7JCc6Q8hqatkUwaSg)  
 一重代理可以（在一定程度上）保护你的隐私，防范跨省追捕。关于这点，俺在《[如何隐藏你的踪迹，避免跨省追捕[1]：网络方面的防范](https://program-think.blogspot.com/2010/04/howto-cover-your-tracks-1.html)》一文已经介绍过了。但如果你对隐私的防范，要求比较高（比如说，你是六扇门关注的对象），那一重代理的安全性就不太够了——你需要使用多重代理。  
 那多重代理是啥样的捏？为了简单起见，俺画了下面这幅双重代理的示意图。  
 ![不见图 请翻墙](images/3ISXywMCtIOfvEZv9FKqIvqGaRRAHaK0qTUxLGMGzK0_zorEGwwL_bqunsnfwYaTJrbOtLtTvaBzONtO4GuXcIwFTBszoDVO8Bwm3jIPOpIW3cfviA)  
 ## ★需要哪些软件？
--------

  
 ### ◇TOR + 其它翻墙工具

  
 理论上，你可以随便挑选两款翻墙工具，然后搞出一个二级代理。但是这样的效果未必理想。  
 根据俺的经验，最佳组合是：用 TOR（俗称“套”）搭配其它的翻墙工具（比如：赛风、无界、自由门、VPN），组合出多重代理。  
   
 ### ◇为啥要用TOR？

  
 长期翻墙的网友，应该都听说过 TOR 这个老牌的翻墙工具（俺曾经扫盲过“[戴套翻墙](http://program-think.blogspot.com/2009/09/break-through-gfw-with-tor.html)”的技术）。那些从来没听说过 TOR 的网友，可以翻墙看“[这里](https://zh.wikipedia.org/wiki/Tor)”的介绍。  
 其实拿 TOR 来翻墙，颇有杀鸡用牛刀的嫌疑。TOR 的主要强项在于：**提供匿名的网络访问，保护你的隐私**。比如名气很大的[维基解密](https://zh.wikipedia.org/wiki/%E7%B6%AD%E5%9F%BA%E8%A7%A3%E5%AF%86)（WikiLeaks），还有名气很大且很牛B的[匿名黑客组织](https://en.wikipedia.org/wiki/Anonymous_%28group%29)（洋文叫“Anonymous”，最近连续黑掉多个大公司及美国政府部门），他们的成员都是用 TOR 来确保自己的匿名。  
 为啥 TOR 能确保匿名捏？因为 TOR 在全球有很多节点，当你利用 TOR 上网的时候，从你的电脑到某个网站，需要经过若干个 TOR 节点。而且 TOR 的节点之间都是加密传输。所以，被你访问的网站，无从知道你的真实IP地址。请看原理图。  
 ![不见图 请翻墙](images/GJSTx_KBgpvLFpFY5qNc_gkWuMA_KDAmoVBCOXgqTEdoXJsVnsXZRQBPvKTX2_gnJkjzJWZP7D3HcuiqYLAqcuE7VnRuZKQQ9ufP_1GpDpOTtmsqDw)  
 假如你有些悟性，自然会发现：TOR 本身就是一个多重代理！既然这样，为啥还要拿 TOR 跟其它翻墙工具搭配捏？主要因为万恶的 GFW 把全球大部分的 TOR 节点都进行了IP封锁。因此，如果你不幸身处天朝，是很难直接访问到 TOR 节点滴！所以，咱们只好委屈一下，拿 TOR 搭配其它翻墙工具。  
   
 ## ★如何配置？
------

  
 其实配置并不难，只需如下几步：  
   
 ### ◇第1步 - 运行翻墙工具

  
 首先，你需要准备好一个**能用的**翻墙工具——可以是 HTTP 代理（比如[无界](https://program-think.blogspot.com/2011/12/gfw-wujie.html)、[自由门](https://program-think.blogspot.com/2010/03/choose-free-gate.html)），也可以是 SOCKS 代理，还可以是 VPN（比如 [Hotspot Shield](https://program-think.blogspot.com/2011/09/gfw-vpn-hotspot-shield.html)）。先把这个翻墙工具运行起来。  
 这个翻墙工具用来作为 TOR 的前置代理。  
   
 ### ◇第2步 - 安装 TOR

  
 然后，**翻墙**到 TOR 的官方网站，下载一个 TOR 的软件包（洋文叫 Vidalia Bundle），安装到你电脑中（下载页面在“[这里](https://www.torproject.org/download/download.html.en)”）。Vidalia Bundle 支持多种语言的界面（含简体中文），还是比较傻瓜化的。  
   
 ### ◇第3步 - 配置 TOR

  
 本文发布于2012年，那时候 TOR 自带图形界面是 Vidalia。到了2015年，Vidalia 已经停止维护了。所以，本文中关于 Vidalia 的配置说明，已经过时了 :( 大伙儿请移步至另一篇教程，介绍 Vidalia 的替代品——《[扫盲 Arm——Tor 的界面前端（替代已死亡的 Vidalia）](https://program-think.blogspot.com/2015/03/Tor-Arm.html)》  
   
   
 这步是关键。你需要在 Vidalia Bundle 的界面上设置一下，让 TOR 可以利用你现有的翻墙工具，进行联网。考虑到翻墙工具主要有：HTTP 代理、SOCKS 代理、VPN 这三种类型，俺分别说一下。  
   
 **如果你用 VPN 翻墙** 
 你不需要修改任何设置，直接点“启动 Tor”按钮。  
 ![不见图 请翻墙](images/m_gu2SHEwbJmGcYJJOyJmdCF4RI7aNxniKUN-6lUA8kMgbMntNUC1DaMqm3IDVkX2Ddw6_KMdM51nQhQfJv2VnVaAO9hBKe6KBAIHq_wEvlKfezo9A)  
 **如果你用 HTTP 代理翻墙** 
 在 Vidalia Bundle 的主界面上，点“设定”按钮。  
 ![不见图 请翻墙](images/7Pmx0N5PoVFPjJ9S2ZHgjhz53frSdegWYhxKGxhFWSqglf7QfWG7aKWLkC1aLGQ3pAjjkVpiqhQBdWWiC5zEhd736dLomnhjx0Lu-jkVAE5v0MeZLg)  
 这时会出来一个选项对话框，选“网络”这个标签页（请注意图中三处**标红**的地方）。  
 把代理的类型选为“**HTTP / HTTPS**”  
 “Address”这项要注意：  
 如果 HTTP 代理软件跟 TOR 安装在同一个系统，那么就填 **127.0.0.1** 
 如果 HTTP 代理软安装在另一个系统，那么就填那个系统的 IP 地址。  
 “端口”这项如何填，取决于你的翻墙代理软件，开放的端口号是多少。比如：赛.风 开放的是8080端口，无界 开放的是9666端口、自由门 开放的是8580端口  
 ![不见图 请翻墙](images/3Ng5b6CDYswX5qIjsBIbBVklsrJMOfJWrl5J0j3GYW5-9yOzEX0znN1-uQ9xJU6l6hj4160OIJkyHNgQjdqa0_RHT5FD0_ScjzbZE_cYzLXB38ThXA)  
 填写完，点确定。然后就可以启动 Tor 了。  
 ![不见图 请翻墙](images/m_gu2SHEwbJmGcYJJOyJmdCF4RI7aNxniKUN-6lUA8kMgbMntNUC1DaMqm3IDVkX2Ddw6_KMdM51nQhQfJv2VnVaAO9hBKe6KBAIHq_wEvlKfezo9A)  
 **如果你用 SOCKS 代理翻墙** 
 如果你用“SOCKS代理”翻墙，配置的步骤跟“HTTP代理”类似——也要填写代理的地址（同上）和端口（取决于具体的SOCKS代理软件）。唯一的区别在于，选择类型时，要记得选 SOCKS4 或 SOCKS5。（如下图）  
 ![不见图 请翻墙](images/XFnVFfJtEcXOJit5auVowGPBbyaBAouFN-LEzWUl3ek_aYtGt1T3hJEG9g5axaTcONdGMXymYSBM436hav7-KZoZ_1C4aSSrEdhV3eWJO6GxXCHmDQ)  
 ### ◇第4步 - 设置浏览器

  
 当你的 TOR 正常建立网络连接，会显示如下界面。  
 ![不见图 请翻墙](images/GnJs1Nh2NC_osSIFVjdiOH9T5lf6TDwnIeyX6AgK0dMmndPmnYL8TY8FgDJA3-wIiM9CWrySFFFs4LVUck3HPVKR-_vxT8jrsf1RBAopO9Mc_eBXsQ)  
 这时候，只需把浏览器的 HTTP 代理指向 TOR（地址 127.0.0.1 端口 8118），就可以通过 TOR 匿名上网了。  
 **为了保险起见，可以访问 TOR 官网的检查页面（在“[这里](https://check.torproject.org/)”），验证一下你是否真的通过 TOR 上网。** 
   
 ### ◇第5步 - 设置其它网络软件

  
 如果你想让其它的网络软件（比如聊天软件、下载工具）通过 TOR 来隐藏你的IP，也很容易。TOR 支持 SOCKS 代理（地址 127.0.0.1 端口 9050）。以 MSN 为例，只需在 MSN 的网络设置界面填写 TOR 的 SOCKS 代理即可。  
 **为了保险起见，到 Vidalia Bundle 主界面点“性能图形”，看一下 TOR 的网络流量。只要该网络软件使用的时候 TOR 有流量，就说明这些网络软件已经通过 TOR 匿名上网了。** 
   
 ## ★多重代理的好处
--------

  
 ### ◇防范追踪

  
 举个例子：  
 假设你用VPN翻墙并发表一些抨击党国的言论。万一 VPN 提供商在 VPN 服务器上记录了你的网络流量，而党国又逼迫该 VPN 供应商交出这些流量记录。那么，党国的爪牙就**有可能**分析出你的上网行为。  
 用了多重代理之后，任何一个代理服务器记录你的网络流量，都无法对你的流量进行分析。  
 比方说你用的是 TOR + 赛风。虽然赛风服务器知道你的真实IP地址，但是无法知道你访问哪个网站及访问的的内容（因为 TOR 的流量是加密的）；而 TOR 的**最后一个节点**虽然知道你访问了哪个网站以及访问的内容，但是它不知道你来自哪里（不清楚你的真实IP地址）。  
   
 ### ◇伪装国籍

  
 除了上述好处，使用 TOR 还有另一个好处——伪装国籍。比方说，你想让自己看起来像是美国的用户，那你只需要切换 TOR 的链路（在 Vidalia Bundle 主界面点“更换身份”按钮），使得最后一个节点位于美国境内（点“查看网络地图”按钮，可以看你的链路）。这种情况下，你访问的网站就会以为你来自美国。  
   
 ## ★多重代理的坏处
--------

  
 当然啦，有利就有弊。以下是多重代理的一些缺点：  
   
 ### ◇配置复杂

  
 跟单重代理比起来，多重代理显然需要更多的设置。很多网友属于技术门外汉，多半对它望而却步。所以，俺才会专门写这么一篇博文，扫盲多重代理。  
   
 ### ◇性能下降

  
 通常来说，多重代理的性能会比单重代理要差一些。具体差多少，取决于你用的软件。  
 俺个人觉得：赛.风+TOR 的方式，速度很理想；另外，“自由门+TOR”以及“无界+TOR”，速度都还凑合。列位看官如果不信，请看俺电脑上的 TOR 流量截图（基于“赛风+TOR”）。  
 ![不见图 请翻墙](images/99PJcrFDw0ooSRN-JikBLgbK0OTvXMVMV2qcJbkRY3HoJWKKiob6Dt6JApixCjwXTX7HsO5B4-pFRTFiyJKLpKL_umZRDnLC83df4U8Cabs1kI33Pw)  
 [回到本系列的目录](https://program-think.blogspot.com/2010/04/howto-cover-your-tracks-0.html#index)  
   
 **俺博客上，和本文相关的帖子（需翻墙）**：  
 [扫盲 Arm——Tor 的界面前端（替代已死亡的 Vidalia）](https://program-think.blogspot.com/2015/03/Tor-Arm.html)  
 [双管齐下的赛风3](https://program-think.blogspot.com/2011/10/gfw-psiphon.html)  
 [新版本无界——赛风3失效后的另一个选择](https://program-think.blogspot.com/2011/12/gfw-wujie.html)  
 [自由門——TOR 被封之后的另一个选择](https://program-think.blogspot.com/2010/03/choose-free-gate.html)  
 [扫盲 VPN 翻墙——以 Hotspot Shield 为例](https://program-think.blogspot.com/2011/09/gfw-vpn-hotspot-shield.html)  
 [戴“套”翻墻的方法](https://program-think.blogspot.com/2009/09/break-through-gfw-with-tor.html) 