//app.js
App({
  onLaunch: function () {
    //调用API从本地缓存中获取数据
    var logs = wx.getStorageSync('logs') || []
    logs.unshift(Date.now())
    wx.setStorageSync('logs', logs)
  },

  getUserInfo: function (cb) {
    var that = this
    if (this.globalData.userInfo) {
      typeof cb == "function" && cb(this.globalData.userInfo)
    } else {
      //调用登录接口
      wx.login({
        success: function () {
          wx.getUserInfo({
            success: function (res) {
              that.globalData.userInfo = res.userInfo
              typeof cb == "function" && cb(that.globalData.userInfo)
            }
          })
        }
      })
    }
  },

  globalData: {
    userInfo: null,
    searchText: "",
    contests: [{
      id: 0,
      name: "IGEM 合成生物学竞赛",
      type: "合成生物学竞赛",
      tag: ["IGEM"],
      timeStart: 9,
      timeEnd: 0,
      participate: true,
      teamAmount: 2,
      show: false,
    },{
      id: 1,
      name: "BBO 英国生物奥赛",
      type: "英国生物奥赛",
      tag: ["BBO"],
      timeStart: 4,
      timeEnd: 0,
      participate: false,
      teamAmount: 1,
      show: false,
    }],
  },

  // module,exports = {
  //   "meta":{"code":200},
  //   "data":{"topwords":[]
  //   }
  // }
})