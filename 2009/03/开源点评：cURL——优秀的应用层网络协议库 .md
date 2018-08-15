# 开源点评：cURL——优秀的应用层网络协议库 

-----

 今天来点评一下 [cURL](https://curl.haxx.se/)，这是一个老资格的开源项目，使用它可以基于多种应用层网络协议进行数据传输（包括上传和下载）。它的特点是：支持的协议多、跨平台、支持多种编程语言接口。后面我会针对这些特点作一些简单的介绍。program-think  
 cURL 项目实际上包含两个部分：命令行工具和编程用的库（[libcurl](https://curl.haxx.se/libcurl/)）。两者支持的功能基本相同。由于开发人员更多地是和 libcurl 打交道，所以后面我会主要介绍 libcurl。  
   
   
 ## ★支持多种应用层协议
----------

  
 多种网络协议支持是 cURL 的主要卖点。截至到（写本文时）最新的7.19.4版本，它支持的网络协议至少有：FTP、FTPS、HTTP、HTTPS、[SCP](https://en.wikipedia.org/wiki/Secure_copy)（secure copy）、[SFTP](https://en.wikipedia.org/wiki/SSH_file_transfer_protocol)（SSH FTP）、[TFTP](https://en.wikipedia.org/wiki/Trivial_File_Transfer_Protocol)（trivial FTP）、TELNET、[DICT](https://en.wikipedia.org/wiki/DICT)、[LDAP](https://en.wikipedia.org/wiki/Lightweight_Directory_Access_Protocol)、LDAPS、[FILE](https://en.wikipedia.org/wiki/File:URL)，够全的吧？  
   
 ### ◇HTTP

  
 HTTP 估计是最常用的一种协议，俺简单说一下 cURL 对 HTTP 支持的程度。  
 对于协议版本：cURL 支持 HTTP 1.0 和 HTTP 1.1。  
 对于请求方式：cURL 支持 GET、POST、PUT、File Upload POST。  
 对于代理（Proxy）类型：包括 HTTP Proxy、[SOCKS4](https://en.wikipedia.org/wiki/SOCKS#SOCKS_4_protocol) Proxy、[SOCKS5](https://en.wikipedia.org/wiki/SOCKS#SOCKS_5_protocol) Proxy。  
 另外，还可以设定 HTTP 认证的用户名口令，cookies，referer 等许多杂七杂八的东东。  
   
 ### ◇SSL 加密

  
 假如你要支持某些依赖 [SSL](https://en.wikipedia.org/wiki/Secure_Sockets_Layer)/[TLS](https://en.wikipedia.org/wiki/Transport_Layer_Security)的协议（比如 HTTPS、FTPS），则需要用到 [OpenSSL](https://en.wikipedia.org/wiki/OpenSSL) 库。在 cURL 的[下载页面](https://curl.haxx.se/download.html)上标注有 SSL 标志的压缩包，都内置了 [OpenSSL](https://en.wikipedia.org/wiki/OpenSSL) 的动态库。另外，在cURL 配置 SSL 证书的相关说明，可以参见“[这里](https://curl.haxx.se/docs/sslcerts.html)”。  
   
   
 ## ★跨平台
----

  
 cURL 支持的平台是相当多的。即使是一些冷门的操作系统（比如：DOS、OS/2），它也支持得很好。  
 另外，cURL 官方网站的[下载页面](https://curl.haxx.se/download.html)提供了基于不同平台的、编译好的、二进制文件供大伙儿直接使用。对于 Linux，它还根据不同厂商、不同发行版本，分别提供二进制文件，考虑相当周到。相比某些开源项目只提供源代码（使用者需要自己动手编译），cURL 算是很方便的一个。  
   
   
 ## ★多种编程语言支持
---------

  
 和上次 [点评的SQLite](https://program-think.blogspot.com/2009/03/opensource-review-sqlite-database.html)一样，libcurl 也支持多种编程语言的绑定，而且 cURL 整合的编程语言比 [SQLite](https://en.wikipedia.org/wiki/SQLite) 还要多。下面列了一些比较常见的编程语言和平台提供的cURL接口。  
   
 ### ◇C/C++

  
 cURL 本身是 C 写的，因此 C 和 C++ 都可以直接调用它的 C 接口 API。在 cURL 的源码包中带有很多 C 的示例，大伙儿可以依样画葫芦。  
 喜欢OO的同学，可以使用 [cURLpp](http://curlpp.org/) 提供的 C++ 包装类。这玩意儿使用 MIT 许可协议。  
   
 ### ◇Java

  
 cURL 和 Java 的整合通过 JNI 实现。可以在“[这里](https://curl.haxx.se/libcurl/java/)”下载压缩包，然后自己编译出相关的动态库和 class 文件。那些懒惰的同学可以到“[这里](http://www.gknw.de/mirror/curl/curl_java/)”捡现成。  
   
 ### ◇Python

  
 [pycurl](http://pycurl.sourceforge.net/) 是 cURL 的 Python 包装库。如果你觉得 Python 内置的 [urllib](https://docs.python.org/library/urllib.html) 功能不够，可以考虑用它。（这玩意儿使用双重许可协议：LGPL 和MIT/X）  
   
 ### ◇dotNET

  
 cURL 和 dotNET 的绑定 [libcurl.NET](http://libcurl-net.sourceforge.net/)。这玩意儿只支持 Win32 操作系统。不过不要紧，对于非 Windows 系统，可以使用 cURL 的 [Mono](https://en.wikipedia.org/wiki/Mono_%28software%29) 绑定 [libcurl.mono](http://forge.novell.com/modules/xfmod/project/?libcurl-mono)。  
   
 ### ◇Visual Basic

  
 cURL 和 VB 的绑定 [libcurl.vb](http://libcurl-vb.sourceforge.net/)。这个项目和上述的 [libcurl.NET](http://libcurl-net.sourceforge.net/) 都是由同一个作者维护的。（也都使用MIT许可协议）  
   
 ### ◇PHP

  
 PHP 要支持 cURL 相对简单多了。在 [PHP 官方网站](http://cn.php.net/curl)上有相关的安装/配置说明。  
   
 ### ◇Ruby

  
 cURL 的 Ruby 的绑定 [Curb](http://curb.rubyforge.org/)。（这玩意儿使用 Ruby 许可协议）  
   
 ### ◇Perl

  
 cURL 和 Perl 的绑定 [WWW::Curl::Easy](http://search.cpan.org/%7Ecrisb/WWW-Curl/Easy.pm.in)。（这玩意儿使用 MPL 或 MIT/X 许可协议）  
   
   
 ## ★应用场景举例
-------

  
 前面说了很多 cURL 的特点，下面来随手举几个应用的例子。  
   
 ### ◇传输文件

  
 如果你需要在程序中进行文件的上传、下载，使用 libcurl 会非常方便。由于它支持的协议很多。一旦将来你的应用程序发生需求变更，改用其它协议，你的代码也不用大改。  
   
 ### ◇调用 Web 接口

  
 随着 SOA 风格的流行，很多比较复杂的系统都会提供很多 Web API 接口。如果你要在程序中调用 Web API 接口，可以考虑使用 libcurl 来实现。  
   
 ### ◇Web 测试

  
 还记得之前[善用自动化](https://program-think.blogspot.com/2009/02/7.html#test)的帖子里提到自动测试的好处吗？由于 cURL 对 HTTP 的支持很全。在 HTTP 协议方面，浏览器能干的活它基本上也能干。再加上它可以和很多脚本语言绑定（除了前面提到的，还可以支持 Lua、Tcl、Lisp 等脚本）。所以你可以用“脚本语言 + cURL”的方式，来进行某些自动化的 Web 测试。  
 比如测试某 Web 站点的安全性（是否有 SQL 注入、XSS 跨站脚本等安全漏洞）或者测试某 Web 接口是否符合文档的约定或者测试某些 Web 接口的性能或者......  
   
   
 ## ★其它一些补充说明
---------

  
 如果你想定期了解 cURL 的新版本、新特性、新 Bug，可以订阅[相关的邮件列表](https://curl.haxx.se/mail/)。  
 另外，cURL 使用 MIT/X 衍生协议，可以用于商业软件中。  
   
   
 **俺博客上，和本文相关的帖子（需翻墙）**：  
 [开源点评：SQLite 数据库扫盲](https://program-think.blogspot.com/2009/03/opensource-review-sqlite-database.html)  
 [开源点评：ZeroMQ 简介](https://program-think.blogspot.com/2011/08/opensource-review-zeromq.html)  
 [开源点评：Protocol Buffers 介绍](https://program-think.blogspot.com/2009/05/opensource-review-protocol-buffers.html) 