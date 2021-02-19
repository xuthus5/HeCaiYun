package main

type EncryptForm struct {
	SourceId    int64 `json:"sourceId"`
	Type        int64 `json:"type"`
	EncryptTime int64 `json:"encryptTime"`
}

type GetEncryptTime struct {
	Code   int    `json:"code"`
	Msg    string `json:"msg"`
	Result int64  `json:"result"`
}

type SignInResponse struct {
	Code   int    `json:"code"`
	Msg    string `json:"msg"`
	Result struct {
		TodaySignIn   bool `json:"todaySignIn"`
		MonthDays     int  `json:"monthDays"`
		MissionPoints int  `json:"missionPoints"`
		RepayPoints   int  `json:"repayPoints"`
		BackPoints    int  `json:"backPoints"`
		TotalPoints   int  `json:"totalPoints"`
		Notice        int  `json:"notice"`
		RemindStatus  int  `json:"remindStatus"`
		GoTone        bool `json:"goTone"`
		PointsExpire  bool `json:"pointsExpire"`
	} `json:"result"`
}

type SendResult struct {
	Code    int64       `json:"code"`
	Message string      `json:"message"`
	Data    interface{} `json:"data"`
}
