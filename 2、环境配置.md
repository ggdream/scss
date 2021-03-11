# 环境配置

~~~
less、scss(sass)和stylus代码并不能被浏览器直接解析，所以必须先将它们编译成css代码

现有框架已经提供了css预处理器选项，编译相关配置会自动帮我们生成！所以只有在"练习"情况下才有必要安装该环境
~~~



## 一、安装分类

### 1.不依赖编辑器

~~~shell
# 全局安装scss预处理器，使用终端命令实现编译

a. Node环境下的node-sass模块
b. Node环境下的dart-sass模块
c. Ruby环境下的sass模块
d. Dart环境下的sass模块

# 注：这里的推荐顺序针对的是"练习"场景，而开发环境下推荐使用的是dart-sass
# 本质：某个语言的第三方库或者命令行工具
~~~

### 2.依赖编辑器

~~~
a. IDE代表：Webstrom	前提是安装上述"1"中的命令行编译工具，配置自动命令，另安装一个代码提示插件scss
b. 编辑器代表：vscode   安装Easy Sass（编译）和Sass（代码提示）两个插件
~~~





## 二、安装步骤

### 1.不依赖编辑器

#### 😀 Node环境

##### - node-sass

###### a.安装

~~~shell
1. 安装node  https://nodejs.org(官网) 或 https://npm.taobao.org/mirrors/node(镜像)
2. *安装cnpm(不推荐直接将源换为淘宝镜像!!) $npm i -g cnpm --registry=https://registry.npm.taobao.org
3. 安装node-sass $npm i -g node-sass  或  $cnpm i -g node-sass
4. 检查是否安装成功$node-sass -v
~~~

![image-20200706124420782](https://raw.githubusercontent.com/ggdream/scss/master/sources.assets/image-20200706124420782.png)

![image-20200706132832305](https://raw.githubusercontent.com/ggdream/scss/master/sources.assets/image-20200706132832305.png)

###### b.使用

1. 单文件编译

   ~~~shell
   $node-sass  原有的scss文件 生成的css文件
   $node-sass  原有的scss文件 -o 生成目录
   
   # example:
   $node-sass a.scss b.css
   $node-sass a.scss css_files
   ~~~

2. 多文件编译

   ~~~shell
   $node-sass 原有的scss文件目录 -o 生成的css文件目录
   
   # example:
   $node-sass c -o d
   ~~~

3. 文件监听模式

   ~~~shell
   # 在"1"和"2"的基础上填加"-w"命令行参数即可
   $node-sass -w 原有的scss文件 -o 生成目录
   $node-sass -w 原有的scss文件目录 -o 生成的css文件目录
   
   # example:
   $node-sass -w scss -o css
   
   # 效果：编译进程不结束，监听文件内容
   ~~~

   ![image-20200706134612609](https://raw.githubusercontent.com/ggdream/scss/master/sources.assets/image-20200706134612609.png)



##### - dart-sass

###### a.安装

~~~shell
1. 安装node  https://nodejs.org(官网) 或 https://npm.taobao.org/mirrors/node(镜像)
2. *安装cnpm(不推荐直接将源换为淘宝镜像!!) $npm i -g cnpm --registry=https://registry.npm.taobao.org
3. 安装dart-sass $npm i -g sass  或  $cnpm i -g sass


# 注：该模块为第三方库，所以可以考虑使用cnpm i sass -D(-D == --save-dev)仅对某个小项目当做开发时依赖进行使用
~~~

###### b.使用

~~~js
/* 该模块的官方文档：https://sass-lang.com/documentation/js-api */


const sass = require('sass');

sass.render({file: scss_filename}, function(err, result) { /* ... */ });
// OR
const result = sass.renderSync({file: scss_filename});

// 注：默认情况下renderSync()的速度是render()的两倍以上，这是由于异步回调所带来的开销而导致的
~~~





-----

#### 😀 Ruby环境

##### a.安装

~~~shell
1.安装Ruby	https://rubyinstaller.org/downloads
2.*配置镜像	$gem sources -a https://gems.ruby-china.com/ -r https://rubygems.org/
3.*查看源 $gem sources -l # 确保只有gems.ruby-china.com一个源
4.安装scss $gem install sass
5.检查是否安装成功 $sass -v
~~~

![image-20200706141653304](https://raw.githubusercontent.com/ggdream/scss/master/sources.assets/image-20200706141653304.png)

~~~shell
#注：如果出现了SSL错误，修改 ~/.gemrc 文件，增加 ssl_verify_mode: 0 配置
# ~表示用户根目录，windows的文件位置为C:\Users\用户名\.gemrc

---
:sources:
- https://gems.ruby-china.com
:ssl_verify_mode: 0
~~~

![image-20200706142100322](https://raw.githubusercontent.com/ggdream/scss/master/sources.assets/image-20200706142100322.png)

##### b.使用

~~~shell
# 注：最好带上"-C --sourcemap=none "参数
# 注：Sass 命令行工具根据文件的拓展名判断所使用的语法格式，没有文件名时 sass 命令默认编译 .sass 文件，添加 --scss 选项或者使用 scss 命令编译 SCSS 文件。
~~~

1. 单文件编译

   ~~~shell
   $sass  原有的scss文件[:]生成的css文件
   
   # example:
   $sass a.scss b.css
   ~~~

2. 多文件编译

   ~~~shell
   $sass --watch 原有的scss文件目录:生成的css文件目录
   # 注：必须加"--watch"
   ~~~

3. 文件监听模式

   ~~~shell
   $sass --watch 原有的scss文件:生成的css文件
   $sass --watch 原有的scss文件目录:生成的css文件目录
   
   # example:
   $sass --watch -C --sourcemap=none scss:css
   
   # 效果：编译进程不结束，监听文件内容
   ~~~

   ![image-20200706143409397](https://raw.githubusercontent.com/ggdream/scss/master/sources.assets/image-20200706143409397.png)

   ![image-20200706164519533](https://raw.githubusercontent.com/ggdream/scss/master/sources.assets/image-20200706164519533.png)





------

#### 😀 Dart环境

##### a.安装

~~~shell
1.安装Dart	https://dart.dev/tools/sdk/archive
2.*配置镜像，添加环境变量 https://pub.flutter-io.cn 或 https://mirrors.tuna.tsinghua.edu.cn/dart-pub/
windows打开此电脑,添加系统变量 PUB_HOSTED_URL=https://pub.flutter-io.cn
Linux键入$echo 'export PUB_HOSTED_URL="https://pub.flutter-io.cn"' >> ~/.bashrc 或 /etc/profile

4.安装sass
全局安装：$pub global activate sass				(可执行文件)
项目安装：pubspec.yaml填写好依赖后，执行 $pub get	  (.dart代码)
5.检查是否安装成功$sass -v
~~~

![image-20200706152755791](https://raw.githubusercontent.com/ggdream/scss/master/sources.assets/image-20200706152755791.png)

![image-20200706153705517](https://raw.githubusercontent.com/ggdream/scss/master/sources.assets/image-20200706153705517.png)

##### b.使用

###### 全局安装模式

1. 单文件编译

   ~~~shell
   $sass  原有的scss文件[:]生成的css文件
   
   # example:
   $sass a.scss b.css
   ~~~

2. 多文件编译

   ~~~shell
   $sass 原有的scss文件目录/:生成的css文件目录/
   
   # example:
   $sass scss/:css/
   ~~~

3. 文件监听模式

   ~~~shell
   $sass --watch 原有的scss文件:生成的css文件
   $sass --watch 原有的scss文件目录:生成的css文件目录
   # 注：都必须加上":"
   
   # example:
   $sass --watch scss:css
   
   # 效果：编译进程不结束，监听文件内容
   ~~~

![image-20200706160732312](https://raw.githubusercontent.com/ggdream/scss/master/sources.assets/image-20200706160732312.png)

###### 局部安装模式

~~~dart
2.运行.dart代码
    // 前提是在pubsepc.yaml文件中添加依赖
    // dev_dependencies:
  	//		sass: lastest

// main.dart
import 'package:sass/sass.dart' as sass;

void main(List<String> args) {
  print(sass.compile(args.first));
}
// or
void main(List<String> args) {
  var result = sass.compile(arguments[0]);
  new File(arguments[1]).writeAsStringSync(result);
}
// dart main.dart styles.scss styles.css
~~~







------

### 2.依赖编辑器

#### 😀 WebStrom

- 安装上述命令行工具之一（以node-sass为例演示）
- 依次打开并点击：webstrom -> Settings -> Tools -> Files Watchers -> + -> 选择SCSS文件标识
- Name随意写，供自己看而已
- File Type选择SCSS Style Sheet 
- Scope选择All Places
- Program选择可执行文件的路径（这里以node-sass为例）
- Arguments按需选择（这里以*$FileName$:$FileNameWithoutExtension$.css*为例）
-  Output paths to refresh按需选择（这里以*$FileNameWithoutExtension$.css*为例）
-  点击OK，配置完成



#### 😀 VSCode

- 安装Easy Sass（编译）和Sass（代码提示）两个插件（注意大小写，否则找不到）
- 点击插件右下角的设置图标后点击"扩展设置"，最后点击"在settings.json中编辑"，开始设置关于Easy Sass的配置
- 会自动生成下方图片内的配置

![image-20200706185328878](https://raw.githubusercontent.com/ggdream/scss/master/sources.assets/image-20200706185328878.png)

- 添加*"easysass.targetDir": $path*，可将编译后的css文件放入*$path*路径下(默认为当前路径)。例如生成到css文件下内

![image-20200706185722811](https://raw.githubusercontent.com/ggdream/scss/master/sources.assets/image-20200706185722811.png)