# HeCaiYun

> 依赖两个参数. `Cookie` 和 `Referer`.
> 测试抓包数据由群 [824187964](https://shang.qq.com/wpa/qunwpa?idkey=2c22cb324dc36e260043185618cbe8763ed63dd5a985ee5e181e20ba2390e78a) 内 `@请回答` (1525417489) 提供.
> 抓包关键字 `caiYunSignIn.action`

## 和彩云自动打卡签到云函数(Python版)

> 位于 SignIn.py 文件中, 修改13/14/15行参数后，拷贝到SCF中即可

## 和彩云自动打卡签到云函数(Go语言版)

请修改 `SignIn.go` 文件 17/18/19 行.

> 构建 本地安装golang环境后执行一下命令进行构建

### bash
```bash
GOPROXY=https://goproxy.cn GOOS=linux GOARCH=amd64 go build -o main .
zip main.zip main
```

### cmd
```bash
set GOPROXY=https://goproxy.cn
set GOOS=linux
set GOARCH=amd64
go build -o main .
```
### powershell
```bash
$env:GOPROXY='https://goproxy.cn'
$env:GOOS='linux'
$env:GOARCH='amd64'
go build -o main .
```

注: 请打包生成的 main 文件为 zip，上传到函数代码处即可
