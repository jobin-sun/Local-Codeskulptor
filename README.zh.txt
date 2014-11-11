codeskulptor打包成本地可执行文件说明
快速开始:
1,把codeskulptor python代码放到src文件夹，把入口文件文件名改成codeskulptor.py。
2,双击create.bat,然后脚本会生成一个App文件夹，里面包含有本地可执行文件。
3,点击Run.exe及可运行。
4,压缩App文件夹发送给你的小伙伴玩耍吧:D。

高级应用:
1,在src目录下新增package.json配置文件,实现个性化需求,详见:
  https://github.com/rogerwang/node-webkit/wiki/Manifest-format
2,把资源打包到本地,比如把一网络音频打包到本地:
  1)修改codeskulptor.py网络请求的url地址到本地地址
  例如:
    sound = simplegui.load_sound('http://www.***.com/***/../test.ogg') =>
    sound = simplegui.load_sound('test.ogg')
  2)把test.ogg放到src目录中,返回到上一级目录,双击create.bat.

  暂时只支持ogg,matroska,wav音频.若要支持mp3和H.264等格式,请参阅 https://github.com/rogerwang/node-webkit/wiki/Using-MP3-%26-MP4-%28H.264%29-using-the--video--%26--audio--tags.


本打包工具使用所使用的开源项目:
	node-webkit(https://github.com/rogerwang/node-webkit/),
	skulpt(http://www.skulpt.org/),
	codeskulptor(http://www.codeskulptor.org/),
