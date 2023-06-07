// pages/result/result.js
Page({

  /**
   * 页面的初始数据
   */
  data: {
    initialWords:"",
    matchedResultsId: [{message: 'foo'},{message:'bar'},],
    localContests: [],
  },
  showSearch: function(e){
      const app=getApp();
      var searchText = this.data.initialWords;
      console.log(this.data.initialWords);
      var sss = true;
      if(searchText!=""){
        //this.data.historyArray.push(searchText);
        for(var index in app.globalData.contests){
          var num1 = app.globalData.contests[index].name.indexOf(searchText);
          var num2 = app.globalData.contests[index].type.indexOf(searchText);
          var upperText = searchText.toUpperCase();
          var num3 = app.globalData.contests[index].tag[0].toUpperCase().indexOf(upperText);
          if(num1!=-1||num2!=-1||num3!=-1){
            //matchedResultsId.push(app.globalData.contests[index].id);
            sss = false;
            let temp = 'localContests['+index+'].show';
            this.setData({
              [temp]: true,
            })
          }
        }
      }
  },
  /**
   * 生命周期函数--监听页面加载
   */
  onLoad(options) {
    const app=getApp();
    this.setData({
      initialWords: options.q,
      localContests: app.globalData.contests
    })
    console.log(this.data.initialWords);
  },

  /**
   * 生命周期函数--监听页面初次渲染完成
   */
  onReady() {
    this.showSearch();
  },

  /**
   * 生命周期函数--监听页面显示
   */
  onShow() {

  },

  /**
   * 生命周期函数--监听页面隐藏
   */
  onHide() {

  },

  /**
   * 生命周期函数--监听页面卸载
   */
  onUnload() {

  },

  /**
   * 页面相关事件处理函数--监听用户下拉动作
   */
  onPullDownRefresh() {

  },

  /**
   * 页面上拉触底事件的处理函数
   */
  onReachBottom() {

  },

  /**
   * 用户点击右上角分享
   */
  onShareAppMessage() {

  }
})