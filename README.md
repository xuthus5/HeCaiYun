# HeCaiYun

和彩云自动打卡签到云函数(Go语言版)

请修改 `SignIn.go` 文件 17/18/19 行，获取相关参数，具体如何获取，群 [824187964](https://shang.qq.com/wpa/qunwpa?idkey=2c22cb324dc36e260043185618cbe8763ed63dd5a985ee5e181e20ba2390e78a) 内 `@请回答` (1525417489). 抓包数据由其提供.

# bash
```bash
GOOS=linux GOARCH=amd64 go build -o main main.go
zip main.zip main
```

# cmd
```bash
set GOOS=linux
set GOARCH=amd64
go build -o main main.go
```
# powershell
```bash
$env:GOOS=linux
$env:GOARCH=amd64
go build -o main main.go
```