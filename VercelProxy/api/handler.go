package handler

import (
	"encoding/base64"
	"encoding/json"
	"github.com/wumansgy/goEncrypt"
	"net/http"
	"strconv"
	"time"
)

// Write 输出返回结果
func Write(w http.ResponseWriter, response []byte) {
	//公共的响应头设置
	w.Header().Set("Access-Control-Allow-Origin", "*")
	w.Header().Set("Access-Control-Allow-Headers", "*")
	w.Header().Set("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
	w.Header().Set("Content-Type", "application/json;charset=utf-8")
	w.Header().Set("Content-Length", strconv.Itoa(len(string(response))))
	_, _ = w.Write(response)
	return
}

type EncryptData struct {
	SourceId    int64 `json:"sourceId"`
	Type        int64 `json:"type"`
	EncryptTime int64 `json:"encryptTime"`
}

// Response 是交付层的基本回应
type Response struct {
	Code    int         `json:"code"`    //请求状态代码
	Message interface{} `json:"message"` //请求结果提示
	Data    interface{} `json:"data"`    //请求结果与错误原因
}

// Handler 句柄
func Handler(w http.ResponseWriter, r *http.Request) {
	ef, err := json.Marshal(&EncryptData{
		SourceId:    1003,
		Type:        1,
		EncryptTime: time.Now().UnixNano() / 1e6,
	})

	if err != nil {
		response, _ := json.Marshal(&Response{
			Code:    400,
			Message: "获取参数失败",
			Data:    err,
		})
		Write(w, response)
		return
	}

	response, _ := json.Marshal(&Response{
		Code:    200,
		Message: "ok",
		Data:    base64.StdEncoding.EncodeToString(RSAEncrypt(ef)),
	})

	Write(w, response)
	return
}

func RSAEncrypt(plainText []byte) []byte {
	var publicKey = []byte(`-----BEGIN PUBLIC KEY-----
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCJ6kiv4v8ZcbDiMmyTKvGzxoPR3fTLj/uRuu6dUypy6zDW+EerThAYON172YigluzKslU1PD9+PzPPHLU/cv81q6KYdT+B5w29hlKkk5tNR0PcCAM/aRUQZu9abnl2aAFQow576BRvIS460urnju+Bu1ZtV+oFM+yQu04OSnmOpwIDAQAB
-----END PUBLIC KEY-----`)
	//对明文进行加密
	cipherText, err := goEncrypt.RsaEncrypt(plainText, publicKey)
	if err != nil {
		panic(err)
	}
	//返回密文
	return cipherText
}
