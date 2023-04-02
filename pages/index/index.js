Page({
  data:{
    modalHidden:true,
    welcome:"welcome"
   },
  search(){
    const app=getApp()
    console.log(app.globalData.searchText.detail.value)
  },
  getSearcher(e){
    const app=getApp()
    //console.log(e.detail)
    app.globalData.searchText=e
  },
  modalTap: function (e) {
    var self = this
    // console.log(e.currentTarget.dataset)

    this.setData({
      // modalContent: self.data.data.hotnews[Number(e.currentTarget.dataset.index)],
      modalHidden: false
    })
  },
  modalHide: function(e) {
    this.setData({
      modalHidden: true
    })
  }

  /*data:{
    inputShowed:true,
    inputVal:"",
  },
  onLoad(){
    this.setData({
      search: this.search.bind(this)
    })
  },
  search:function(value){
    return new Promise((resolve,reject)=>{
      setTimeout(()=>{
        resolve([{text:"搜索结果",value:1},{text:"搜索结果2",value:2}])
      },200)
    })
  },
  selectResult:function(e){
    console.log("select result",e.detail)
  },*/
});