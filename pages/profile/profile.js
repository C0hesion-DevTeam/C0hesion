//index.js
//获取应用实例
var app = getApp()
Page({
  data: {
    motto: '活动让生活更美好!',
    userInfo: {
      Name : "",
      avatarUrl : "",
      gender : "",
      province : "",
      city : "",
      system : ""
    }
  },
  //事件处理函数
  bindViewTap: function () {
    wx.navigateTo({
      url: '../logs/logs'
    })
  },

  showUserInfoTap:function(){
    var that = this;
    wx.getUserInfo({
      success: function(res) {
        console.log(res);
        
        var userInfo = res.userInfo
        console.log(userInfo);
        var Name = userInfo.Name
        var avatarUrl = userInfo.avatarUrl
        var gender = userInfo.gender  //性别 0：未知、1：男、2：女
        var province = userInfo.province
        var city = userInfo.city
        var system = userInfo.system
        if(gender==1){
          gender = '男'
        }else if(gender==2){
          gender='女'
        }else{
          gender = '未知'
        }
        that.setData({
          Name : Name,
          avatarUrl : avatarUrl,
          gender : gender,
          system : system,
          province : province
        })
      }
    })
  },

  onLoad: function () {
    app.getUserInfo(userInfo => this.setData({ userInfo }))
  }
})
